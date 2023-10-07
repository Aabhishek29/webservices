from rest_framework.decorators import api_view

from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RegisterUsers


# Create your views here.


class RegisteredUser(APIView):
    """
    this class I use to get and register users details in database
    """
    def get(self, request, *args, **kwargs):
        result = RegisterUsers.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        print(request.data)
        serializer = None
        try:
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


@api_view(['POST'])
def authenticate(request):
    try:
        data = request.data
        name = data["userName"]
        password = data["password"]
        registerModel = RegisterUsers.objects.filter(userName=name).values()
        if registerModel:
            pswd = registerModel[0].get('password', None)
            if pswd == password:
                return Response({"status": "success","authenticated": "true", "data": registerModel}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "success","authenticated": "false", "data": "incorrect username or password"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success","authenticated": "false", "data": "User not found"}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"status": "success","authenticated": "false", "data": e}, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def forgetPassword(request):
    pass