from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class test_for_all(TestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_tepmlate(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'pages/home.html')