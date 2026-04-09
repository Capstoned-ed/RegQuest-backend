from django.db import models
from django.conf import settings
from documents.models import Document

# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    document_type = models.ForeignKey(Document, on_delete=models.PROTECT)

    