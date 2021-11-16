from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

from .fields import UUIDPrimaryKeyField

BLOCKED_REASON_CHOICES = (
    ("no_service", "Psychologist not on service"),
    ("withdraw", "Psychologist withdrew from the appointments"),
)

STATUS_CHOICES = (
    ("evaluation", "Evaluation"),
    ("unqualified", "Unqualified"),
    ("ready", "Ready"),
)


class BaseModel(models.Model):
    class Meta:
        abstract = True


class UUIDModel(BaseModel):
    class Meta:
        abstract = True

    id = UUIDPrimaryKeyField()


class TimestampedModel(BaseModel):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class AbstractBaseUser(DjangoAbstractBaseUser):
#     email = models.EmailField(("e-mail"), max_length=255, unique=True)
#     password = models.CharField(("password"), max_length=256)

#     is_active = models.BooleanField(("active"), default=True)

#     USERNAME_FIELD = "email"

#     class Meta(DjangoAbstractBaseUser.Meta):
#         abstract = True

#     def get_short_name(self):
#         return self.email


# class AbstractUser(UUIDModel, AbstractBaseUser, TimestampedModel):
#     name = models.CharField(max_length=255)

#     class Meta(AbstractBaseUser.Meta):
#         verbose_name = "user"
#         verbose_name_plural = "users"
#         abstract = True

#     def get_full_name(self):
#         return self.name

#     def __str__(self):
#         return f"{self.email}"


# class User(AbstractUser):
#     serializer = "apps.core.serializers.UserSerializer"

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()
#     class Meta(AbstractUser.Meta):
#         swappable = "AUTH_USER_MODEL"

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin


class Category(models.Model):
    name = CharField(max_length=200)


class Psychologist(UUIDModel):
    full_name = CharField(max_length=200, default="")
    cpf = CharField(max_length=200, default="")
    rg = CharField(max_length=200, default="")
    crp = CharField(max_length=14, default="")  # only numbers
    birth_date = CharField(max_length=200, default="")
    address = CharField(max_length=200, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    whatsapp_phone = models.CharField(max_length=16)
    about = models.TextField(null=True, blank=True)
    picture_url = models.URLField(blank=True, default="")
    user_id = models.OneToOneField(User, related_name="psychologists", on_delete=models.CASCADE)

    status = CharField(max_length=14, choices=STATUS_CHOICES, default="evaluation")
    paused = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    blocked_reason = CharField(max_length=64, blank=True, default="", choices=BLOCKED_REASON_CHOICES)
    last_blocked_on = models.DateTimeField(auto_now_add=True)
    registration_approved_by = models.EmailField(blank=True)

    in_an_appointment = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"
