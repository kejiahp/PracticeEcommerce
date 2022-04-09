from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class product(models.Model):
    product_name = models.CharField(max_length=150)
    product_category = models.ForeignKey(category, on_delete=models.CASCADE)
    product_image1 = models.ImageField(default = 'default_product.png', upload_to = 'product/%Y/%m/%d')
    product_image2 = models.ImageField(default = 'default_product.png', upload_to = 'product/%Y/%m/%d')
    product_image3 = models.ImageField(default = 'default_product.png', upload_to = 'product/%Y/%m/%d')
    product_price = models.DecimalField(max_digits=7 , decimal_places=2)
    product_description = models.TextField()
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now, blank=True)
    top_sale = models.BooleanField(default= True)

    def __str__(self):
        return f'ID{self.id}|||{self.product_name}'

    def save(self):
        super().save()

        img1 = Image.open(self.product_image1.path)
        if img1.height >300 or img1.width > 300:
            img1 = img1.resize((300,300), Image.ANTIALIAS )
            img1.save(self.product_image1.path)

        img2 = Image.open(self.product_image2.path)
        if img2.height >300 or img2.width > 300:
            img2 = img2.resize((300,300), Image.ANTIALIAS )
            img2.save(self.product_image2.path)

        img3 = Image.open(self.product_image3.path)
        if img3.height >300 or img3.width > 300:
            img3 = img3.resize((300,300), Image.ANTIALIAS )
            img3.save(self.product_image3.path)