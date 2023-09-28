from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Menu
from .views import MenuItemView

class MenuViewTest(TestCase):
    def test_view_item(self):
        item = Menu.objects.create(title="hotdog", price=10, inventory=50)
        response = self.client.get(MenuItemView)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)