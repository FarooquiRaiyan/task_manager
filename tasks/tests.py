from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Task




class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')


    def test_register(self):
        url = reverse('auth-register-list') # router registered viewset
        data = {'username': 'newuser', 'password': 'newpass123'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)