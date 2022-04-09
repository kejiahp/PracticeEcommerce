from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
    path('',views.home,name='home-page'),
    path('register/',views.register_page,name = 'register-page'),
    path('register-val/',views.register_form,name='register-form'),
    path('login/',views.login_page,name='login-page'),
    path('login-val/',views.login_form,name='login-form'),
    path('logout/',views.logout_control,name='logout-control'),
    path('search-product/',views.serach_for_product,name = "search-product"),
    path('search-category/',views.search_by_category,name = "search-category"),
]