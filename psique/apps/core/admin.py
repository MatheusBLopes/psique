from django.contrib import admin

from .models import Category, Psychologist


class PsiqueAdmin(admin.ModelAdmin):
    fields = [
        "full_name",
        "cpf",
        "rg",
        "crp",
        "birth_date",
        "address",
        "category",
        "whatsapp_phone",
        "about",
        "picture_url",
        "status",
        "paused",
        "blocked",
        "blocked_reason",
        "registration_approved_by",
    ]
    list_display = ("full_name", "crp", "category", "whatsapp_phone", "blocked", "in_an_appointment")


class CategoryAdmin(admin.ModelAdmin):
    fields = [
        "name",
    ]
    list_display = "name"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Psychologist, PsiqueAdmin)
