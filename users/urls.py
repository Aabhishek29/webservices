from django.urls import path
from .views import RegisteredUser
from . import views
from . import bookingsupport

urlpatterns = [
    path('users', RegisteredUser.as_view()),
    path('authenticate', views.authenticate),
    path('forgetPassword', views.forgetPassword),
    path('contact_us', bookingsupport.contactUs),
    path('sendFormToBookingSupport', bookingsupport.sendFormToBookingSupport)
]
