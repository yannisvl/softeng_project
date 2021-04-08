import datetime
from django.test import TestCase
from django.utils import timezone

from energy.models import *

class EurogroupTests(TestCase):
    
	def test_database_health(self):
             print("Hello")
             self.assertIs(True)
	

