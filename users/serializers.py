from rest_framework import serializers
from .models import RegisterUsers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterUsers
        fields = '__all__'
