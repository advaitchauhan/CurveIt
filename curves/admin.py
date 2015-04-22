from django.contrib import admin

# Register your models here.
from curves.models import Course_Specific, Student, QueryList

class Course_Specific_Admin(admin.ModelAdmin):
	search_fields = ['semester', 'prof', 'dept', 'num', 'name']

class Student_Admin(admin.ModelAdmin):
	search_fields = ['netid', 'name', 'year']

admin.site.register(Course_Specific, Course_Specific_Admin)
admin.site.register(Student, Student_Admin)
admin.site.register(QueryList)