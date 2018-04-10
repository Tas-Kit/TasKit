# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your tests here.


class LoginViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create_user(username='testclient', password='password', email='testclient@example.com')
        cls.u3 = User.objects.create_user(username='staff', password='password', email='staffmember@example.com')

    def test_view(self):
        response = self.client.get(reverse('basic:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basic/login.html')
        self.assertTemplateUsed(response, 'base.html')
        form = response.context['form']

        self.assertIsInstance(form, AuthenticationForm)
