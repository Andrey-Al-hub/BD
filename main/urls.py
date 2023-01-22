from django.urls import path, include
from .views import *

urlpatterns = [
    path('homepage.html', loadHomepage, name = 'homepage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]