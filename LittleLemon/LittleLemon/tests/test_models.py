from django.tests import TestCase
from Restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        menu = Menu.objects.create(title='Ice Cream', price=5, inventory=100)
        self.assertEqual(menu, 'Ice Cream : 5')