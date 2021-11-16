import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import apps.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Psychologist",
            fields=[
                (
                    "id",
                    apps.core.fields.UUIDPrimaryKeyField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("full_name", models.CharField(default="", max_length=200)),
                ("cpf", models.CharField(default="", max_length=200)),
                ("rg", models.CharField(default="", max_length=200)),
                ("crp", models.CharField(default="", max_length=14)),
                ("birth_date", models.CharField(default="", max_length=200)),
                ("address", models.CharField(default="", max_length=200)),
                ("whatsapp_phone", models.CharField(max_length=16)),
                ("about", models.TextField(blank=True, null=True)),
                ("picture_url", models.URLField(blank=True, default="")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("evaluation", "Evaluation"),
                            ("unqualified", "Unqualified"),
                            ("ready", "Ready"),
                        ],
                        default="evaluation",
                        max_length=14,
                    ),
                ),
                ("paused", models.BooleanField(default=False)),
                ("blocked", models.BooleanField(default=False)),
                (
                    "blocked_reason",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("no_service", "Psychologist not on service"),
                            ("withdraw", "Psychologist withdrew from the appointments"),
                        ],
                        default="",
                        max_length=64,
                    ),
                ),
                ("last_blocked_on", models.DateTimeField(auto_now_add=True)),
                ("registration_approved_by", models.EmailField(blank=True, max_length=254)),
                ("in_an_appointment", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.category",
                    ),
                ),
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="psychologists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
