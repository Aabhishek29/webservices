from django.urls import path
from .views import RegisteredUser
from . import views

urlpatterns = [
    path('users', RegisteredUser.as_view()),
    path('authenticate',views.authenticate),
    path('forgetPassword', views.forgetPassword)
]