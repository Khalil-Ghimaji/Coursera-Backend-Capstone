from django.test import TestCase

from littleLemonAPI.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=5.99, inventory=100)
        Menu.objects.create(title="Pizza", price=8.99, inventory=50)
        Menu.objects.create(title="Burger", price=6.99, inventory=75)
        Menu.objects.create(title="Pasta", price=7.99, inventory=30)

    def test_getall(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

        # # if  you want to run this test please clean your database or update the ids to match your database
        # self.assertEqual(response.json(), [
        #     {'id': 1, 'title': 'Ice Cream', 'price': '5.99', 'inventory': 100},
        #     {'id': 2, 'title': 'Pizza', 'price': '8.99', 'inventory': 50},
        #     {'id': 3, 'title': 'Burger', 'price': '6.99', 'inventory': 75},
        #     {'id': 4, 'title': 'Pasta', 'price': '7.99', 'inventory': 30}
        # ])