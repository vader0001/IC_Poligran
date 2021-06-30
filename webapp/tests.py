from django.test import TestCase
from .models import Item

def trigger_error():
    division_by_zero = 1 / 0
    
#TODO fabricar tests unitarios 
class ItemTestCase(TestCase):

    def test_prueba(self):
        self.assertEqual(1,1)
