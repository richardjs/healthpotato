from django.contrib.auth.models import User
from django.test import TestCase

from healthpotato.models import WeightData


class WeightEntryTest(TestCase):
    def setUp(self):
        User.objects.create_user(
           'testuser', 'testuser@example.com', 'password').save()
        self.client.login(username='testuser', password='password')

    def test_get_weight_form(self):
        response = self.client.get('/weight')
        self.assertTrue(b'weight' in response.content)
        self.assertTrue(b'submit' in response.content)

    def test_log_weight(self):
        self.client.post('/weight', {'weight': '150'})
        self.assertEqual(len(WeightData.objects.all()), 1)
        self.client.post('/weight', {'weight': '200'})
        self.assertEqual(len(WeightData.objects.all()), 2)
