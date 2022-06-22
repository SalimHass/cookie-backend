from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class CookieStand(models.Model):

    location = models.CharField(max_length=255)
    min_cust = models.IntegerField()
    max_cust = models.IntegerField()
    avg_cookies=models.IntegerField()
    
    def __str__(self):
        return self.location