import random

from rest_framework.decorators import api_view

from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterUsers
import re
import math
from django.core.mail import send_mail

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# Create your views here.


class RegisteredUser(APIView):
    """
    hello
    """
    def get(self, request, *args, **kwargs):
        result = RegisterUsers.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        print(request.data)
        serializer = None
        try:
            if not isEmail(request.data['email']):
                return Response({"status": "error", "data": "Invalid Email"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                "status": "Error in webservices",
                "data": serializer.errors
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def isEmail(mail):
    if re.fullmatch(regex, mail):
        return True
    else:
        return False

@api_view(['POST'])
def authenticate(request):
    try:
        data = request.data
        name = data["userName"]
        password = data["password"]
        if isEmail(name):
            registered = RegisterUsers.objects.filter(email=name).values()
        else:
            registered = RegisterUsers.objects.filter(userName=name).values()
        if registered:
            pswd = registered[0].get('password', None)
            if pswd == password:
                return Response({"status": "success","authenticated": "true", "data": registered}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "success","authenticated": "false", "data": "incorrect username or password"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success","authenticated": "false", "data": "User not found"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "success","authenticated": "false", "data": e}, status=status.HTTP_400_BAD_REQUEST)


def sendOTP(email, digit):
    try:
        digits = "0123456789"
        OTP = ""
        for i in range(int(digit)):
            OTP += digits[math.floor(random.random() * 10)]
        print(OTP)
        htmlgen = f'<p>Your OTP is <strong>{OTP}</p>'
        reciptent_email = []
        reciptent_email.append(email)
        return send_mail('OTP request', OTP, 'indzzwebservices@gmail.com', reciptent_email , fail_silently=False,
                  html_message=htmlgen)
    except Exception as e:
        print("error is ", e)



def verifyOTP(request):
    pass


@api_view(["POST"])
def forgetPassword(request):
    try:
        data = request.data
        name = data["email"]
        digit = data["digit"]
        if not isEmail(name):
            return Response({"status": "success","authenticated": "false", "data": "Please send correct email"}, status=status.HTTP_200_OK)
        registered = RegisterUsers.objects.filter(email=name).values()
        if True:
            sendOTP(name, digit)
            return Response({"status": "success", "data": f"OTP send to the {name}"},
                            status=status.HTTP_200_OK)
        # else:
        #     return Response({"status": "success", "authenticated": "false", "data": "User not found"},
        #                     status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "success", "authenticated": "false", "data": e}, status=status.HTTP_400_BAD_REQUEST)



