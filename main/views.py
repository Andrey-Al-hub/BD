from django.shortcuts import render, redirect
from main.models import *

# def indexMain(request):
#     return render(request, 'main/index.html')
# def redirectToHomepage(request):
#     return redirect('main/index.html', permanent=True)

def productSelect(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'main/index.html', context)

def inputIncome(request):
    product_to_change = request.POST.get("income_title", "Undefined")
    price_add = request.POST.get("income_price", "Undefined")

    product = Product.objects.get(title=product_to_change)
    print(product)
    print(product_to_change, price_add)
    product.price = product.price + int(price_add)
    product.save()
    return redirect(request, 'main/layout/redirect.html')