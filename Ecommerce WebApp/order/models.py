from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from products.models import product
from customers_profile.models import addressInfo
from django.utils.timezone import now

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)
    complete = models.BooleanField(default = False)
    transactio_id = models.CharField(max_length=100, null = True)

    def __str__(self):
        return str(self.id)

    @property
    def total_checkout_price(self):
        total = 0
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            total = total + float(item.total_product_price)
        return total

    @property
    def total_item_count(self):
        total = 0
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            total = total + item.quantity
        return total

class OrderItem(models.Model):
    custProduct = models.ForeignKey(product, on_delete= models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total_product_price(self):
        product_price = self.custProduct.product_price
        product_quantity = self.quantity
        total = product_price * product_quantity
        return str(total)

    def __str__(self):
        return str(self.id)

class Ordered(models.Model):
    order_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_used = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(default = now, blank=True)

    def __str__(self):
        return str(self.id)

class ShippingDetails(models.Model):
    ship_to_order = models.OneToOneField(Ordered, on_delete=models.SET_NULL, null=True)
    address_details = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length = 100)
    receiverName = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'ID:{self.id}|||USER:{self.receiverName}'