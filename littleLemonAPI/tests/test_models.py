from django.test import TestCase

from littleLemonAPI.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=5.99, inventory=100)
        print(item)
        self.assertEqual(str(item),'Ice Cream : 5.99 (100 in stock)')
