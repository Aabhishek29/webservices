import random

from rest_framework.decorators import api_view

from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
import math
from django.core.mail import send_mail

from .views import isEmail


@api_view(["POST"])
def contactUs(request):
    try:
        data = request.data
        print(data)
        name = data["name"]
        email = data["email"]
        issue = data["issue"]
        phone =  data["phoneNumber"]
        msg = data["msg"]
        if not isEmail(email):
            return Response({"status": "success", "data": "Please send correct email"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"status": "success", "authenticated": "false", "data": e}, status=status.HTTP_400_BAD_REQUEST)

