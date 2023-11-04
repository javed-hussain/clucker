from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    #overiding the username feild so that it i smax length of 30
    #keyword argument unique specifes that the usernames are all unique
    username = models.CharField(
        max_length=30,
        unique=True,
        validators = [RegexValidator(
            regex= r'^@\w{3,}$',
            message='Username must consist of @symbol followed by at least 3 alphanumericals'
        )]
    )
    #blank keyword denotes if the feild can be blank or not
    first_name = models.CharField(max_length=50, blank = False)
    last_name = models.CharField(max_length=50, blank = False)
    email = models.EmailField(unique=True, blank=False)
    #textFeilds do not enfore max length therefore we use charfeild and will use textfeild widget when displaying
    bio = models.CharField(max_length=520, blank=True)
    