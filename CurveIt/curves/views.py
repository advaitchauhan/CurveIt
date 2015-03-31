from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from curves.models import Course_Specific
from curves.forms import Course_SpecificForm

# Create your views here.
def index(request):
	return render(request, 'curves/index.html')

#return a list of all classes that belong in the department, with links to them
def deptView(request, cdept):
	course_list = get_list_or_404(Course_Specific, dept = cdept)
	context = {'course_list': course_list, 'cdept': cdept}
	return render(request, 'curves/dept.html', context)

def courseSpecificView(request, cdept, cnum, ctime):
	course = get_object_or_404(Course_Specific, dept = cdept, num = cnum, semester = ctime)
	response = Course_Specific.printGrades(course)
	return HttpResponse(response)

def add_data(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = Course_SpecificForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            curData = form.cleaned_data
            try:
                thisClass = Course_Specific.objects.get(dept=curData["dept"], num=curData["num"], semester=curData["semester"])
                thisGrade = curData["grade"]
                if thisGrade == "1":
                    thisClass.addGrade("A+")
                elif thisGrade == "2":
                    thisClass.addGrade("A")
                elif thisGrade == "3":
                    thisClass.addGrade("A-")
                elif thisGrade == "4":
                    thisClass.addGrade("B+")
                elif thisGrade == "5":
                    thisClass.addGrade("B")
                elif thisGrade == "6":
                    thisClass.addGrade("B-")
                elif thisGrade == "7":
                    thisClass.addGrade("C+")
                elif thisGrade == "8":
                    thisClass.addGrade("C")
                elif thisGrade == "9":
                    thisClass.addGrade("C-")
                elif thisGrade == "10":
                    thisClass.addGrade("D_grade")
                elif thisGrade == "11":
                    thisClass.addGrade("F_grade")
                elif thisGrade == "12":
                    thisClass.addGrade("D_PDF")
                elif thisGrade == "13":
                    thisClass.addGrade("F_PDF")
                elif thisGrade == "14":
                    thisClass.addGrade("P_PDF")
                thisClass.save()
            except Course_Specific.DoesNotExist:
                thisClass = None

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = Course_SpecificForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'curves/add_data.html', {'form': form})
