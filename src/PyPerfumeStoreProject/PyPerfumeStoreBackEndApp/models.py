from django.db import models

# Create your models here.

class ArticleType(models.Model):
    ArticleTypeId = models.AutoField(primary_key=True)
    ArticleTypeName = models.CharField(max_length=20)
    ArticleTypeDesc = models.CharField(max_length=80)

    class Meta:
        db_table = "ArticleType"

class ArticleUnit(models.Model):
    ArticleUnitId = models.AutoField(primary_key=True)
    ArticleUnitName = models.CharField(max_length=20)
    ArticleUnitDesc = models.CharField(max_length=80)

    class Meta:
        db_table = "ArticleUnit"

class Provider(models.Model):
    ProviderId = models.AutoField(primary_key=True)
    ArticleFullName = models.CharField(max_length=50)
    ArticleAddress1 = models.CharField(max_length=80)
    ArticleAddress2 = models.CharField(max_length=80)
    ArticlePhoneNum1 = models.CharField(max_length=10)
    ArticlePhoneNum2 = models.CharField(max_length=10)

    class Meta:
        db_table = "Provider"

class Article(models.Model):
    ArticleId = models.AutoField(primary_key=True)
    ArticleRef = models.CharField(max_length=50)
    ArticleName = models.CharField(max_length=50)
    ArticlePrice = models.FloatField()
    ArticleUnit = models.ForeignKey(ArticleUnit, on_delete=models.CASCADE, null=True)
    ArticleType = models.ForeignKey(ArticleType, on_delete=models.CASCADE, null=True)
    Provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "Article"


class StoreInfo(models.Model):
    storeInfoId = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=50)

    class Meta:
        db_table = "StoreInfo"
class ProductType(models.Model):
    productTypeId = models.AutoField(primary_key=True)
    productTypeName = models.CharField(max_length=80)

    class Meta:
        db_table = "ProductType"

class ProductCategory(models.Model):
    productCategoryId = models.AutoField(primary_key=True)
    productCategoryName = models.CharField(max_length=80)

    class Meta:
        db_table = "ProductCategory"

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productCode = models.CharField(max_length=50)
    productName = models.CharField(max_length=80)
    productTypeId = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"

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
