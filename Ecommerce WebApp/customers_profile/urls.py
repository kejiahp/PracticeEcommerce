from os import name
from django.urls import path
from customers_profile import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customer_page/',views.customers_page,name = 'customer-page'),
    path('prof_img_change/',views.change_image,name='profile-img-change'),
    path('address_info/<int:user_pk>/',views.address_info_page,name = 'address-info-page'),
    path('login_needed/',views.login_req,name = 'login-req'),
    path('address-val/<int:user_pk>/',views.address_change_val,name = 'address-validation'),
    path('prof_update/',views.profile_update,name='profile-update'),
    path('address_update/<int:user_pk>/',views.update_address,name='update-address-info'),
    path('update_address_val/<int:user_pk>/',views.update_address_val,name='update-address-validation'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)