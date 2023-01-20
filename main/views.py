from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import *
from .models import *

def redirect_from_host_to_homepage(request):
    return redirect('homepage', permanent=True)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('homepage')
    def get_context_data(self, *, object_lict=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()))

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('homepage')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    def get_context_data(self, *, object_lict=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()))
    def get_success_url (self):
        return reverse_lazy('homepage')


def logout_user(request):
    logout(request)
    return redirect('login')


def loadHomepage(request):

    product_to_change = request.POST.get("income_title", "")
    if product_to_change != '':
        amount_add = request.POST.get("income_amount", "")
        product_db = Product.objects.get(title=product_to_change)
        product_db.amount = product_db.amount + int(amount_add)
        product_db.save()
        print('ТОВАР ДОБАВЛЕН')
        return redirect('homepage.html')

    product_to_write_off = request.POST.get("write_off_title", "")
    if product_to_write_off != '':
        amount_write_off = request.POST.get("write_off_amount", "")
        product_db = Product.objects.get(title=product_to_write_off)
        product_db.amount = product_db.amount - int(amount_write_off)
        product_db.save()
        print('ТОВАР СПИСАН')
        return redirect('homepage.html')

    if request.method == "POST":
        income_form = AddIncomeForm(request.POST, request.FILES)
        if income_form.is_valid():
            manuf_title = request.POST.get("new_manufacturer", "")
            if manuf_title != '':
                manuf_db = Manufacturer()
                manuf_db.manufacturer = manuf_title
                manuf_db.city = request.POST.get("new_manufacturer_city", "")
                manuf_db.save()

                product_db = Product()
                product_db.title = income_form.cleaned_data['title']
                product_db.category = income_form.cleaned_data['category']
                product_db.price = income_form.cleaned_data['price']
                product_db.amount = income_form.cleaned_data['amount']
                product_db.expiration_date = income_form.cleaned_data['expiration_date']
                product_db.image = income_form.cleaned_data['image']
                product_db.description = income_form.cleaned_data['description']
                product_db.manufacturer_id = manuf_db.id
                product_db.save()
                print('СОЗДАНО С НОВЫМ ПРОИЗВОДИТЕЛЕМ')
                return redirect('homepage.html')
            else:
                income_form.save()
                print('СОЗДАНО БЕЗ НОВОГО ПРОИЗВОДИТЕЛЯ')
                return redirect('homepage.html')
            # except:
            #     income_form.add_error(None, "Ошибка добавления товара")

    # ВЫВОД НА СТРАНИЦУ
    product = Product.objects.all()
    income_form = AddIncomeForm()
    # manufacturer = AddManufacturerForm()
    context = {
        'pr': product,
        'income_form': income_form,
        # 'manuf_form': manufacturer
    }
    return render(request, 'main/homepage.html', context)

# def addAmountProduct(request):
#     product = Product.objects.all()
#     context = {
#         'pr': product }
#     product_to_change = request.POST.get("income_title", "")
#     if product_to_change != '':
#         amount_add = request.POST.get("income_amount", "")
#         product = Product.objects.get(title=product_to_change)
#         print(product_to_change, amount_add)
#         product.amount = product.amount + int(amount_add)
#         product.save()
#     return render(request, 'main/add_income_amount.html', context)
#
# def addNewProduct(request):
#     income_form = AddIncomeForm(request.POST)
#     if income_form.is_valid():
#         try:
#             income_form.save()
#             return redirect('homepage.html')
#         except:
#             income_form.add_error(None, "Ошибка добавления товара")

# def incomeInput(request):
#     product_to_change = request.POST.get("income_title", "Undefined")
#     amount_add = request.POST.get("income_amount", "Undefined")
#
#     product = Product.objects.get(title=product_to_change)
#     print(product)
#     print(product_to_change, amount_add)
#     product.amount = product.amount + int(amount_add)
#     product.save()
#     return render(request, 'main/homepage.html')

# if request.POST.get('income_price'):
#
# def useForms(self, request, *args, **kwargs):
#     print('yes')
#     product_to_change = request.POST.get("income_title", "Undefined")
#     amount_add = request.POST.get("income_amount", "Undefined")
#     if product_to_change != 'Undefined':
#         product = Product.objects.get(title=product_to_change)
#         print(product)
#         print(product_to_change, amount_add)
#         product.amount = product.amount + int(amount_add)
#         product.save()


    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.save()
    #     return redirect(obj.get_absolute_url())
    # return render(request, 'main/layout/operations.html')

# def recipe_c(request):
#     if request.method=='POST':
#         if request.POST.get(''):
#             form_select = SelectOperationForm()
#             form_income = InputIncomeForm()

# def addSelectOperationForm(request):
#     form = SelectOperationForm()
#     return render(request, 'main/layout/select_operation.html', {'form': form})
#
# def addInputIncomeForm(request):
#     form = InputIncomeForm()
#     # product_to_change = request.POST.get("income_title", "Undefined")
#     # amount_add = request.POST.get("income_amount", "Undefined")
#     #
#     # product = Product.objects.get(title=product_to_change)
#     # print(product)
#     # print(product_to_change, amount_add)
#     # product.amount = product.amount + int(amount_add)
#     # product.save()
#     return render(request, 'main/layout/income.html', {'form': form})

# def (request):
#     if request.method=='POST':
#         if request.POST.get(''):
#             form_select = SelectOperationForm()
#             form_income = InputIncomeForm()


# #
# def addInputIncomeForm(request):
#     form_select = SelectOperationForm(request.POST or None)
#     form_income = InputIncomeForm(request.POST or None)
#     context = {
#         'form_select': form_select,
#         'form_income': form_income
#     }
#     if all([form_select.is_valid(), form_income.is_valid()]):
#         form_select.save(commit=False)
#         form_income.save(commit=False)
#     # return render(request, 'main/layout/select_operation.html', context)
#     # product_to_change = request.POST.get("income_title", "Undefined")
#     # amount_add = request.POST.get("income_amount", "Undefined")
#     #
#     # product = Product.objects.get(title=product_to_change)
#     # print(product)
#     # print(product_to_change, amount_add)
#     # product.amount = product.amount + int(amount_add)
#     # product.save()
#     return render(request, 'main/layout/income.html', context)