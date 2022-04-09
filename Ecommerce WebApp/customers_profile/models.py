from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_image = models.ImageField(default='default.jpeg', upload_to='profile_pics/%Y/%m/%d')

    def __str__(self):
        return f'{self.user.username} profile image'
    
    def save(self):
        super().save()
        img = Image.open(self.profile_image.path)
        if img.height > 120 or img.width > 120:
            img = img.resize((120,120), Image.ANTIALIAS)
            img.save(self.profile_image.path)


class addressInfo(models.Model):
    user_address = models.OneToOneField(User, on_delete=models.CASCADE)
    address_details = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length = 100)
    receiverName = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'ID:{self.id}|||USER:{self.user_address}'
