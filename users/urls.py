from django.urls import path
from .views import RegisteredUser


urlpatterns = [
    path('users/', RegisteredUser.as_view()),
]