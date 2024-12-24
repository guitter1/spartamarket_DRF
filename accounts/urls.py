from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("<str:username>/", views.UserAPIView.as_view()),
    path("", views.UserAPIView.as_view()),
    ]