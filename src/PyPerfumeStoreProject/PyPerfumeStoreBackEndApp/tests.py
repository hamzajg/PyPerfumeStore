from rest_framework import status
from rest_framework.test import APITestCase

from . import models


class ProviderApiTest(APITestCase):
    url = "/management/api/provider"

    def test_lists_providers(self):
        models.Provider.objects.create(
            ProviderFullName="Acme", ProviderAddress1="1 Main St",
            ProviderPhoneNum1="0102030405")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["ProviderFullName"], "Acme")

    def test_creates_a_provider(self):
        response = self.client.post(self.url, {
            "ProviderFullName": "Acme",
            "ProviderAddress1": "1 Main St",
            "ProviderAddress2": "Suite 2",
            "ProviderPhoneNum1": "0102030405",
            "ProviderPhoneNum2": "0607080910",
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Provider.objects.count(), 1)

    def test_rejects_a_provider_without_a_name(self):
        response = self.client.post(self.url, {
            "ProviderAddress1": "1 Main St",
            "ProviderAddress2": "Suite 2",
            "ProviderPhoneNum1": "0102030405",
            "ProviderPhoneNum2": "0607080910",
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("ProviderFullName", response.json())


class ArticleApiTest(APITestCase):
    url = "/management/api/article"

    def setUp(self):
        self.provider = models.Provider.objects.create(
            ProviderFullName="Acme", ProviderAddress1="1 Main St",
            ProviderPhoneNum1="0102030405")
        self.article_type = models.ArticleType.objects.create(
            ArticleTypeName="Perfume", ArticleTypeDesc="Bottled perfume")
        self.article_unit = models.ArticleUnit.objects.create(
            ArticleUnitName="ml", ArticleUnitDesc="Millilitre")

    def test_lists_articles_with_their_provider(self):
        models.Article.objects.create(
            ArticleRef="REF-1", ArticleName="Rose", ArticlePrice=12.5,
            ArticleQte=10, ArticleMinQte=2, Provider=self.provider,
            ArticleType=self.article_type, ArticleUnit=self.article_unit)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        body = response.json()[0]
        self.assertEqual(body["ArticleName"], "Rose")
        self.assertEqual(body["Provider"]["ProviderFullName"], "Acme")

    def test_rejects_an_article_without_a_reference(self):
        response = self.client.post(self.url, {
            "ArticleName": "Rose",
            "ArticlePrice": 12.5,
            "ArticleQte": 10,
            "ArticleMinQte": 2,
        }, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("ArticleRef", response.json())
