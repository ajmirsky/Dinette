from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class TestDinetteViews(TestCase):
    def setUp(self):
        self.c =Client()
    
    def test_index_page(self):
        """Check that the index page is available to all users"""
        response = self.c.get(reverse('index_page'))
        self.assertEqual(200,response.status_code)