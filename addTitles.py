import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')
import django
django.setup()

from curves.models import Course_Specific, Student

courses = Course_Specific.objects.all()

for c in courses:
	titleString = "" 
	depts = c.dept.split("+") 
	nums = c.num.split("+")
	
	#create string in format "COS 126/ EGR 126 General Computer Science"
	for i in range(0, len(depts)):
		if i == (len(depts)-1):
			titleString += depts[i] + " " + nums[i] + ": "
		else:
			titleString += depts[i] + " " + nums[i] + "/" 
	titleString += c.name
	print titleString
	print c.titleString
	c.titleString = titleString
	c.save()

