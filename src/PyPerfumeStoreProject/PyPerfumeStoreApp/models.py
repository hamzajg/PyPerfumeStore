from django.db import models

# Create your models here.

class StoreInfo(models.Model):
    storeInfoId = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=50)

class ProductType(models.Model):
    productTypeId = models.AutoField(primary_key=True)
    productTypeName = models.CharField(max_length=80)

class ProductCategory(models.Model):
    productCategoryId = models.AutoField(primary_key=True)
    productCategoryName = models.CharField(max_length=80)

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productCode = models.CharField(max_length=50)
    productName = models.CharField(max_length=80)
    productTypeId = models.ForeignKey(ProductType, on_delete=models.CASCADE)

# class ProductPromo(models.Model):

# class ProductBrand(models.Model):

# class Customer(models.Model):

# class Provider(models.Model):

# class Offers(models.Model):

# class Gift(models.Model):

# class Sale(models.Model):

# class User(models.Model):

# class UserAccount(models.Model):

# class WishList(models.Model):
