from django.urls import path
from .views import productSelect, inputIncome
    # , redirectToHomepage

urlpatterns = [
    # path('main/index.html', indexMain, name='index'),
    # path('main/index.html', redirectToHomepage, name = 'redirect'),
    path('main/index.html', productSelect),
    path('main/index.html', inputIncome, name = 'inputIncome'),
    # path('hidden_page/', inputIncome, name = 'hidden_page')
]