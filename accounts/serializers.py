from rest_framework import serializers
from .models import User, StudentInfo, StaffInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','univ_id','first_name','middle_name','last_name','role']

class StudentInfoSerializer(serializers.ModelSerializer):
    user  = UserSerializer(read_only=True)
    class Meta:
        model = StudentInfo
        fields = ['user', 'course', 'year_level']

class StaffInfoSerializer(serializers.ModelSerializer):
    user  = UserSerializer(read_only=True)
    class Meta:
        model = StaffInfo
        fields = ['user', 'position']

