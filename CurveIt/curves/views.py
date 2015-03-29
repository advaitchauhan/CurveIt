from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from curves.models import Course_Specific

# Create your views here.
def index(request):
	return HttpResponse("Welcome to Princeton CurveIt. /n To start exploring course and grade distributions, append a 3-letter department code to the URL ")

#return a list of all classes that belong in the department, with links to them
def deptView(request, cdept):
	course_list = get_list_or_404(Course_Specific, dept = cdept)
	context = {'course_list': course_list, 'cdept': cdept}
	return render(request, 'curves/dept.html', context)

def courseSpecificView(request, cdept, cnum, ctime):
	course = get_object_or_404(Course_Specific, dept = cdept, num = cnum, semester = ctime)
	response = Course_Specific.printGrades(course)
	return HttpResponse(response)