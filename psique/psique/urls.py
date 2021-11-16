from django.conf.urls import url
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^v1/", include("apps.core.routes")),
    url("admin/", admin.site.urls),
]
