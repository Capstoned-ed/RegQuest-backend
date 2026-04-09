from django.db import models

# Create your models here.
class DocumentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    processing_time = models.IntegerField()
