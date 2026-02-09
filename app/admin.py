from django.contrib import admin
from app.models import CustomUser, Task
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Task)