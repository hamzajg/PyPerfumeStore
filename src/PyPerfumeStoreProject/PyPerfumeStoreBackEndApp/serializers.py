from . import models
from rest_framework import serializers

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Provider
        fields = ('ProviderId', 'ProviderFullName', 'ProviderAddress1',
        'ProviderAddress2','ProviderPhoneNum1','ProviderPhoneNum2',)

class ArticleSerializer(serializers.ModelSerializer):
    Provider = ProviderSerializer()

    class Meta:
        model = models.Article
        fields = ('ArticleId', 'ArticleRef','ArticleName','ArticlePrice',
        'ArticleQte','ArticleMinQte','Provider','ArticleType','ArticleUnit',)
