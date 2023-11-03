from django.contrib import admin

from .models import *


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Suhbat)
class SuhbatAdmin(admin.ModelAdmin):
    list_display = ['sarlavha']
