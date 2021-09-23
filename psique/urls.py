from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.views import PsycologistViewSet

router = routers.DefaultRouter()
router.register('psycologist', PsycologistViewSet, basename="Psycologist")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
