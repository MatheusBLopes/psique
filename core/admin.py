from django.contrib import admin

from core.models import Psycologist


@admin.register(Psycologist)
class Psycologist(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
