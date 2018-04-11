# -*- coding: utf-8 -*-
"""This script contains models required by the basic app."""
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

    def __unicode__(self):
        """Unicode of the UserProfile Model.

        Returns:
            TYPE: String
        """
        return self.user.username.encode('utf-8')

    def __str__(self):
        """string description.

        Returns:
            TYPE: String
        """
        return unicode(self)


# pylint: disable=unused-argument
def create_profile(sender, **kwags):
    """Create User Profile when a user register.

    Args:
        sender (TYPE): User
        **kwags: arguments for creating the user profile
    """
    if kwags['created']:
        UserProfile.objects.create(user=kwags['instance'])

post_save.connect(create_profile, sender=User)
