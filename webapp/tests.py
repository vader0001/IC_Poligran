from django.test import TestCase
from .models import Item

class ItemTestCase(TestCase):

    def test_Items_can_speak(self):
        """Items that can speak are correctly identified"""
        self.assertEqual('Test', 'Generar error sentry')
        