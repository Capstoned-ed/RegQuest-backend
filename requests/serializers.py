from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        read_only_fields = ['user', 'status', 'created_at', 'updated_at', 'processed_by']