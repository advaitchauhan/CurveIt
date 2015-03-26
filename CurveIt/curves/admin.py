from django.contrib import admin

# Register your models here.
from curves.models import Course_Specific, User

admin.site.register(Course_Specific)
admin.site.register(User)