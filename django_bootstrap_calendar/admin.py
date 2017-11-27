# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class CalendarEventAdmin(admin.ModelAdmin):
     list_display = ('title', 'url','start','end')

admin.site.register(CalendarEvent,CalendarEventAdmin)
