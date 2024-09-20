from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop_item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(max_length=1000)
    on_sale = models.BooleanField(default=False)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_items = models.ForeignKey(Shop_item, on_delete=models.CASCADE)
