from django.urls import path

from apps.core.api import PsycologistViewSet, RegisterView, LoginView, UserView, LogoutView


app_name = "core"


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('psycologist', PsycologistViewSet.as_view({"get":"list"}), name="psycologist")
    ]
