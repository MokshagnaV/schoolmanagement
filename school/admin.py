from django.contrib import admin

# Register your models here.
from .models import  student, buddy, school_admin

admin.site.register(student)
admin.site.register(buddy)
admin.site.register(school_admin)