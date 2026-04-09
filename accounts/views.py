from rest_framework import viewsets
from .models import User, StudentInfo, StaffInfo
from .serializers import UserSerializer, StudentInfoSerializer, StaffInfoSerializer

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentInfoViewSet(viewsets.ModelViewSet):
        queryset = StudentInfo.objects.all()
        serializer_class = StudentInfoSerializer

class StaffInfoViewSet(viewsets.ModelViewSet):
        queryset = StaffInfo.objects.all()
        serializer_class = StaffInfoSerializer