from django.test import TestCase
from .models import Item

def trigger_error(request):
    division_by_zero = 1 / 0
    
#TODO fabricar tests unitarios 
class ItemTestCase(TestCase):

    def test_Items_can_speak(self):
        """Items that can speak are correctly identified"""
        self.assertEqual(1,1)
        trigger_error()
        