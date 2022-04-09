from django.urls import path
from .views import cart,checkout,item_removal_cart,item_removal_checkout,your_orders,check_order,ordered_item_details,email_page,orders_email,paystacktest

urlpatterns = [
    path('cart_page/',cart, name = 'cart-page'),
    path('checkout_page/',checkout,name = 'checkout-page'),
    path('item_remove_cart/<int:item_id>/',item_removal_cart,name = 'item-remove-cart'),
    path('item_remove_checkout/<int:item_id>/',item_removal_checkout,name = 'item-remove-checkout'),
    path('orders/',your_orders,name='your-orders'),
    path('on_checkout/<int:order_id>/',check_order,name = "on-checkout"),
    path('orders_details/<int:item_id>/',ordered_item_details,name="orders-details"),
    path('email_approved/',email_page,name='email-approved'),
    path('email_sender/<int:order_id>',orders_email,name="email-sender"),
    path('support_creator/',paystacktest,name = 'pay-stacktest'),
]