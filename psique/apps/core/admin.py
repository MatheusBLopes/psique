from django.contrib import admin

from .models import Category, Psychologist

admin.site.register(Category)


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
    # readonly_fields = ("original_error",)


admin.site.register(Psychologist, PsiqueAdmin)
