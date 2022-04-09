from customers_profile.models import profile as cust_profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = cust_profile.objects.create(user = instance)
        profile.save()