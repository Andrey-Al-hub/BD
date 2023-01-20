from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('homepage.html', loadHomepage, name = 'homepage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

    # path('authentification.html', TemplateView.as_view(template_name='authentification.html'), name='register'),

    # path('income.html', incomeSelect),
    # path('add_income_amount.html', addAmountProduct, name = 'addAmountProduct')
]