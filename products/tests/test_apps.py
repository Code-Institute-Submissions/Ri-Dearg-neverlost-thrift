from django.apps import apps
from django.test import TestCase
from products.apps import ProductsConfig


class TestProductsConfig(TestCase):
    """Tests the Django app config."""
    def test_app(self):
        self.assertEqual('products', ProductsConfig.name)
        self.assertEqual('products', apps.get_app_config('products').name)
