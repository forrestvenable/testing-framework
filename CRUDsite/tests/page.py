from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.page_data = {'name': 'test', 'url': 'http://www.google.com'}
        self.response = self.client.post(
            reverse('create'),
            self.page_data,
            format="json")

    def test_api_can_create_a_page(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)