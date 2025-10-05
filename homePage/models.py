from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(help_text='Price in cents')
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    active = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.name} , $ {self.price/100:.2f}"
    
    @property
    def price_display(self):
        return self.price / 100


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 200)
    amount = models.IntegerField(help_text= 'Price in cents') 
    quantity = models.IntegerField(default = 1)
    stripe_session_id = models.CharField(max_length = 200, unique = True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_name},{self.quantity}"
    
    @property
    def amount_display(self):
        return self.amount / 100


