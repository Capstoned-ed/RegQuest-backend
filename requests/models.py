from django.db import models
from django.conf import settings
from documents.models import Document

# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    document_type = models.ForeignKey(Document, on_delete=models.PROTECT)
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        PROCESSING = 'processing', 'Processing'
        READY = 'ready', 'Ready'
        CLAIMED = 'claimed', 'Claimed'
    
    status = models.CharField(max_length=15, choices=Status.choices)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    est_release_date = models.DateTimeField()
    processed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='processed_requests'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
