from django.test import TestCase


class StoreFrontTest(TestCase):
    def test_the_store_front_page_renders(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class ManagementIndexTest(TestCase):
    def test_the_management_page_renders(self):
        response = self.client.get("/management/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/index.html")
