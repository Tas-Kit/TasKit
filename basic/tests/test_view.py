# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from basic.forms import SignUpForm
# Create your tests here.


class TestLoginView(TestCase):

    def setUp(self):
        self.url = reverse('basic:login')
        self.username = 'testclient'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_get_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basic/login.html')
        self.assertTemplateUsed(response, 'base.html')
        form = response.context['form']
        self.assertIsInstance(form, AuthenticationForm)

    def test_login_success(self):
        response = self.client.post(self.url, data={
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('basic:home'))
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)

    def test_already_login(self):
        self.client.post(self.url, data={
            'username': self.username,
            'password': self.password
        })
        response = self.client.get(self.url)
        self.assertEqual(response.url, reverse('basic:home'))

    def test_login_fail(self):
        response = self.client.post(self.url, data={
            'username': 'badusername',
            'password': 'badpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basic/login.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_login_redirect(self):
        test_url = '/admin/'
        response = self.client.get(test_url)
        self.assertRedirects(response, self.url + '?next=/admin/')
        response = self.client.post(response.url, data={
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, test_url)


class TestSignUpView(TestCase):

    def setUp(self):
        self.url = reverse('basic:signup')
        self.sample_data = {
            'username': 'test_user2',
            'first_name': 'test first',
            'last_name': 'test last',
            'email': 'tes1@taskit.com',
            'password1': '1g8f18934hfd8g12',
            'password2': '1g8f18934hfd8g12',
        }

    def test_get_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basic/signup.html')
        self.assertTemplateUsed(response, 'base.html')
        form = response.context['form']
        self.assertIsInstance(form, SignUpForm)

    def test_sign_up_success(self):
        response = self.client.post(self.url, data=self.sample_data)
        self.assertRedirects(response, reverse('basic:home'))
        self.assertIn('_auth_user_id', self.client.session)

    def test_sign_up_fail(self):
        bad_data = dict(self.sample_data)
        bad_data['password2'] += '2'
        response = self.client.post(self.url, data=bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basic/signup.html')
        self.assertTemplateUsed(response, 'base.html')
