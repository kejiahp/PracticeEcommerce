from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from .models import product
from .models import category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order.models import Order,OrderItem
from products.models import product

# Create your views here.
def products_details(request,product_id):
    product_queryset = product.objects.filter(id = product_id).first()
    content = {
        'product_queryset':product_queryset
    }
    return render(request, 'products/product_details.html',content)

def cart_adder(request, prod_id):
    if request.method == 'POST':
        order_number = request.POST['order-number']
        order,created = Order.objects.get_or_create(customer = request.user ,complete = False )
        product1 = product.objects.filter(id = prod_id).first()
        item_add = OrderItem(custProduct = product1, order = order, quantity = order_number)
        item_add.save()
        messages.success(request, 'Cart Updated.')
        return redirect('products-details', prod_id)
    else:
        messages.warning(request, 'Cart was not updated.')
        return redirect('products-details', prod_id)