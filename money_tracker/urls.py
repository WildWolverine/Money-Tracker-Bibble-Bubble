from tkinter.font import names

from django.urls import path
from . import views
urlpatterns = [
    path('home',views.get_home, name='home'),
    path('register',views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('add',views.add_expense,name='add')
]