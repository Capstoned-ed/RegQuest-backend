from django.db import models

# Create your models here.
class Document(models.Model):
    document_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    processing_time_days = models.IntegerField()
