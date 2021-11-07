from django.contrib.auth.models import User
from django.test import TestCase

from healthpotato.models import ExerciseData, FoodData, WeightData


# Putting abstract test classes under GenericTests keeps them from being run
class GenericTests:
    class UserTest(TestCase):
        def setUp(self):
            User.objects.create_user(
               'testuser', 'testuser@example.com', 'password').save()
            self.client.login(username='testuser', password='password')


    class DataEntryTest(UserTest):
        def setUp(self):
            User.objects.create_user(
               'testuser', 'testuser@example.com', 'password').save()
            self.client.login(username='testuser', password='password')

        def test_get_form(self):
            response = self.client.get(self.path)
            self.assertTrue(b'<form' in response.content)
            self.assertTrue(b'submit' in response.content)

        def test_enter_data(self):
            self.client.post(self.path, self.entry)
            self.assertEqual(len(self.model.objects.all()), 1)
            self.client.post(self.path, self.entry)
            self.assertEqual(len(self.model.objects.all()), 2)

        def test_login_required(self):
            response = self.client.get(self.path)
            self.assertEqual(response.status_code, 200)
            self.client.logout()
            response = self.client.get(self.path)
            self.assertNotEqual(response.status_code, 200)


class HomeTest(GenericTests.UserTest):
    def test_weight_reminder(self):
        response = self.client.get('/')
        self.assertTrue(b'You have not entered weight data for today' in response.content)

        self.client.post('/weight', {'weight': '150', 'clothing': 1,
            'timestamp': '1900-11-06T20:35:30' })
        response = self.client.get('/')
        self.assertTrue(b'You have not entered weight data for today' in response.content)

        self.client.post('/weight', {'weight': '150', 'clothing': 1})
        response = self.client.get('/')
        self.assertFalse(b'You have not entered weight data for today' in response.content)


class ExerciseEntryTest(GenericTests.DataEntryTest):
    model = ExerciseData
    path = '/exercise'
    entry = {'type': '0', 'effort': '3'}


class FoodEntryTest(GenericTests.DataEntryTest):
    model = FoodData
    path = '/food'
    entry = {'nutrition': '3', 'amount': '3'}


class WeightEntryTest(GenericTests.DataEntryTest):
    model = WeightData
    path = '/weight'
    entry = {'weight': '150', 'clothing': 1}
