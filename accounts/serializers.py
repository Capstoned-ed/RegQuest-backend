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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'role', 'username']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'username': {'required': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
    
        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email'].split('@')[0]
            
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
