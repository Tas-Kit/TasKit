# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """User's profile object, an extension to the User model.

    Attributes:
        image (TYPE): url
        user (TYPE): Description
    """

    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        """string description.

        Returns:
            TYPE: String
        """
        return self.user.username


def create_profile(sender, **kwags):
    """Create User Profile when a user register.

    Args:
        sender (TYPE): User
        **kwags: arguments for creating the user profile
    """
    if kwags['created']:
        UserProfile.objects.create(user=kwags['instance'])

post_save.connect(create_profile, sender=User)
