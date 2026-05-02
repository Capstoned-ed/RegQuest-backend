from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    document_name = serializers.CharField(source='document_type.document_name', read_only=True)
    processing_time_days = serializers.IntegerField(source='document_type.processing_time_days', read_only=True)
    class Meta:
        model = Request
        fields = '__all__'
        read_only_fields = ['user', 'status', 'created_at', 'updated_at', 'processed_by', 'tracking_number']