from django.contrib import admin
from .models import User, StudentInfo, StaffInfo

# Register your models here.
admin.site.register(User)
admin.site.register(StudentInfo)
admin.site.register(StaffInfo)