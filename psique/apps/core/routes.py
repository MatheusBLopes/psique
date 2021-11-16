from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from apps.core.api import (
    AcceptConsultationView,
    CategoryViewSet,
    CloseConsultationView,
    LoginView,
    LogoutAndBlacklistRefreshTokenForUserView,
    PsychologistViewSet,
    RegisterView,
    RequestConsultationView,
)

app_name = "core"

router = DefaultRouter()
router.register("psychologist", PsychologistViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="create_user"),
    path("login/", LoginView.as_view(), name="login"),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name="blacklist"),
    path("request-consultation/", RequestConsultationView.as_view(), name="request-consultation"),
    path(
        r"accept-consultation/<uuid:psychologist_id>/",
        AcceptConsultationView.as_view(),
        name="accept-consultation",
    ),
    path("end-consultation/", CloseConsultationView.as_view(), name="free-for-consultation"),
]

urlpatterns += router.urls
