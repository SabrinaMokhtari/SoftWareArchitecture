from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.TextField()
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
