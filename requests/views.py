from rest_framework import viewsets
from .models import Request
from .serializers import RequestSerializer

# Create your views here.
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
