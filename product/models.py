from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductTable(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    images = models.FileField(upload_to="image")
    is_available = models.BooleanField()
    
    

class Cart_table(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product_id = models.ForeignKey('ProductTable', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

