from django.urls import path
from .views import products_details,cart_adder
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('product_details/<int:product_id>/',products_details,name = 'products-details'),
    path('prod_add/<int:prod_id>/',cart_adder,name = 'prod-add'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)