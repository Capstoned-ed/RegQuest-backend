from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    univ_id =  models.CharField(unique=True, max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True)

    class Roles(models.TextChoices):
        STUDENT = 'student', 'Student'
        STAFF = 'staff', 'Staff'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=10, choices=Roles.choices)

class StudentInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    year_level = models.IntegerField()


class StaffInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)