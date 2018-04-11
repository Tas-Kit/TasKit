# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from basic.forms import SignUpForm

# Create your tests here.


class TestSignUpForm(TestCase):

    def test_save(self):
        username = 'test_user'
        data = {
            'username': username,
            'email': 'test@taskit.com',
            'first_name': 'TestFirst',
            'last_name': 'TestLast',
            'password1': '1g8f18934hfd8g12',
            'password2': '1g8f18934hfd8g12'
        }
        form = SignUpForm(data=data)
        self.assertIsNone(form.save(commit=False))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username=username)
        user = form.save()
        self.assertIsNotNone(user)
        user2 = User.objects.get(username=username)
        self.assertEqual(user, user2)
