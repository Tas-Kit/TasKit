# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse


class TestLoginRequireMiddleware(TestCase):

    def test_go_to_exempt_url(self):
        response = self.client.get(reverse('basic:reset_password'))
        self.assertEqual(response.code, 200)
        self.assertTemplateUsed(response, 'basic/reset_password.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_go_to_login_required_url(self):
        response = self.client.get(reverse('basic:home'))
        self.assertEqual(response.code, 200)
        self.assertTemplateUsed(response, 'basic/login.html')
        self.assertTemplateUsed(response, 'base.html')
