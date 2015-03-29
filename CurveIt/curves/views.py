from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from curves.models import Course_Specific

# Create your views here.
def index(request):
	return HttpResponse("Home Page")

def CS(request, cdept, cnum, ctime):
	course = get_object_or_404(Course_Specific, dept = cdept, num = cnum, semester = ctime)
	response = Course_Specific.printGrades(course)
	return HttpResponse(response)