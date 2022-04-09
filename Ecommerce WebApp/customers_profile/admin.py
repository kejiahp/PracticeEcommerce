from django.contrib import admin
from customers_profile import models

# Register your models here.
admin.site.register(models.profile)

admin.site.register(models.addressInfo)