# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


class TestUserProfile(TestCase):

    def setUp(self):
        User.objects.create_user
        self.user = User.objects.create_user(username='test user',
                                             email='test@taskit.com',
                                             password='test password'
                                             )
        self.userprofile = self.user.userprofile

    def test__string__(self):
        self.assertEqual(self.user.username, self.userprofile.__str__())
