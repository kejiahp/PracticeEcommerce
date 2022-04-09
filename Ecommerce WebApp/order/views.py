from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from order.models import Order
from order.models import OrderItem,Ordered,ShippingDetails
from customers_profile.models import addressInfo
from itertools import chain
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from smtplib import SMTPException

# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        content = {
            'items':items,
            'order':order
        }
    return render(request, 'order/cart_page.html',content)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        addr = addressInfo.objects.filter(id = request.user.id).first()

    content = {
        'addr':addr,
        'order':order,
        'items':items
    }
    return render(request, "order/checkout_page.html",content)

def item_removal_cart(request, item_id):
    order = OrderItem.objects.filter(id = item_id)
    order.delete()
    messages.success(request, 'Item Removed.')
    return redirect('cart-page')

def item_removal_checkout(request, item_id):
    order = OrderItem.objects.filter(id = item_id)
    order.delete()
    messages.success(request, 'Item Removed.')
    return redirect('checkout-page')

def your_orders(request):
    if Ordered.objects.filter(order_owner = request.user.id).exists():
        order_owner = Ordered.objects.filter(order_owner = request.user.id).all()
        #creating an emtpy queryset to hold the other order items collected from the for loop
        x = QuerySet(model=OrderItem)
        for i in order_owner:
            ord = i.order_used
            ordd = ord.orderitem_set.all()
            x.union(ordd)
        ordd = x
        content = {
            'ordd':ordd
        }
        return render(request, 'order/ordered_items.html',content)
    else:
        return redirect('home-page')

def check_order(request, order_id):
    #SUBMITTING THE INDIVIDUALS ORDER
    if Order.objects.filter(id = order_id).exists():
        order = Order.objects.get(id = order_id)
        addr = addressInfo.objects.filter(id = request.user.id).first()
        order.complete = True
        order.save()
        orders = Ordered(order_owner = request.user, order_used = order)
        orders.save()
        order_shipping = ShippingDetails(ship_to_order = orders, address_details= addr.address_details , city = addr.city, state= addr.state, receiverName= addr.receiverName, phone1= addr.phone1, phone2= addr.phone2)
        order_shipping.save()

        return redirect('your-orders')
    else:
        return redirect('checkout-page')
    
def ordered_item_details(request, item_id):
    order_item = OrderItem.objects.filter(id = item_id).first()
    order_used = order_item.order.id
    # order = Order.objects.filter(id = order_used).first()
    ordered_used = Ordered.objects.filter(order_used = order_used)
    ordered_used_specified = ordered_used.first()
    ordered_shipping_address = ShippingDetails.objects.filter(ship_to_order = ordered_used.first().id).first()
    print(ordered_shipping_address)
    content = {
        'ordered_used_specified':ordered_used_specified,
        'ordered_used':ordered_used,
        'order_item':order_item,
        'ordered_shipping_address':ordered_shipping_address
    }
    return render(request, "order/ordered_items_details.html",content)

def email_page(request):
    return render(request, 'order/email_approved.html')

def orders_email(request,order_id):
    orders = Order.objects.filter(id = order_id).first()
    orderitems = orders.orderitem_set.all()
    text_content = []
    content = {
        "orderitems":orderitems,
        "username":orders.customer
    }
    for i in orderitems:
        text_content.append({"productName":i.custProduct.product_name, "productQuantity":i.quantity,"productTotal":i.total_product_price})
    subject = "Order Information"
    from_email = "popoolakejiah@gmail.com"
    to_email = "dimeji_popoola@yahoo.com"
    text_content = str(text_content)
    html_content = render_to_string('email_approved.html',content, request=request)

    try:
        msg = EmailMultiAlternatives(subject,text_content,from_email, [to_email])
        msg.attach_alternative(html_content,"text/html")
        msg.send(fail_silently=False)
    except SMTPException as e:
        print("There was an execption:  ",e)

    return redirect('checkout-page')

def paystacktest(request):
    return render(request, 'order/paymentForm.html')