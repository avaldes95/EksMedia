from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    # Create relationship
    # first name, last name, email, username
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes
    profile_pic = models.ImageField(upload_to='eksapp/profile_pics',blank=True)

    def __str__(self):
        return self.user.username
