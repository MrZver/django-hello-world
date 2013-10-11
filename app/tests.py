"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from app.models import User1


class AppTest(TestCase):
    fixtures = ['initial_data.json']

    def test_record_exist(self):
        mainuser = User1.objects.get(pk=1)
        self.assertEqual(bool(mainuser), True)
