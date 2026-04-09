from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import User, StudentInfo, StaffInfo
from .serializers import UserSerializer, StudentInfoSerializer, StaffInfoSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentInfoViewSet(viewsets.ModelViewSet):
        queryset = StudentInfo.objects.all()
        serializer_class = StudentInfoSerializer

class StaffInfoViewSet(viewsets.ModelViewSet):
        queryset = StaffInfo.objects.all()
        serializer_class = StaffInfoSerializer