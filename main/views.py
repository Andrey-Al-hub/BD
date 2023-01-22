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
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    def get_context_data(self, *, object_lict=None, **kwargs):
        context = super().get_context_data(**kwargs)
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

    # ВЫВОД НА СТРАНИЦУ
    product = Product.objects.all()
    income_form = AddIncomeForm()
    context = {
        'pr': product,
        'income_form': income_form,
    }
    return render(request, 'main/homepage.html', context)

