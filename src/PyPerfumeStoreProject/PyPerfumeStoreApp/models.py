from django.db import models

# Create your models here.

class ProductType(models.Model):
    productTypeId = models.AutoField(primary_key=True)
    productTypeName = models.CharField(max_length=80)
    
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productCode = models.CharField(max_length=50)
    productName = models.CharField(max_length=80)
    productTypeId = ForeignKey(model=ProductType)
