# -*- coding: utf-8 -*-
"""Admin for Basic App."""

from __future__ import unicode_literals

from django.contrib import admin
from basic.models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.site_header = 'TasKit'
