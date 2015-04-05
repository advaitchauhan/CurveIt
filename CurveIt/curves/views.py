from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from curves.models import Course_Specific
from curves.forms import Course_SpecificForm
import json

CURRENTSEMESTER = "S2015"
GRADES = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D_grade", "F_grade", "P_PDF", "D_PDF", "F_PDF"]

def index(request):
	return render(request, 'curves/index.html')

#return a list of all classes that belong in the department, with links to them
def deptView(request, cdept):
    course_list = get_list_or_404(Course_Specific, dept = cdept)
    numGrades = [0] * len(GRADES)
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)
    total = sum(numGrades)

    context = {'dept': cdept, 'course_list': course_list, 'dist': dist, 'total': total}
    return render(request, 'curves/dept.html', context)

#return a list of all classes that are taught by cprof, with links to them
def profView(request, cprof):
    course_list = get_list_or_404(Course_Specific, prof = cprof)
    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    dist = zip(GRADES, numGrades)
    total = sum(numGrades)
    context = {'course_list': course_list, 'cprof': cprof, 'dist': dist, 'total': total}
    return render(request, 'curves/prof.html', context)

# view associated with a specific course
def courseSpecificView(request, cdept, cnum, ctime):
    course = get_object_or_404(Course_Specific, dept = cdept, num = cnum, semester = ctime)
    numGrades = course.getAllGrades()
    dist = zip(GRADES, numGrades)
    total = sum(numGrades)
    
    context = {'course': course.name, 'prof': course.prof, 'dept': course.dept, 'coursenum': course.num, 'dist': dist, 'total': total}
    # context = {'course': course, "grades": GRADES, "numGrades": numGrades}
    return render(request, 'curves/course_specific.html', context)

# page for user to input class/grade
def add_data(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = Course_SpecificForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            curData = form.cleaned_data
            try:
                thisClass = curData["pastSemClass"]
                thisClassInfo = thisClass.split()
                thisDept = thisClassInfo[0]
                thisNum = thisClassInfo[1]
                thisClass = Course_Specific.objects.get(dept=thisDept, num=thisNum, semester=CURRENTSEMESTER)
                thisGrade = curData["grade"]

                thisClass.addGrade(thisGrade)
                thisClass.save()
            except Course_Specific.DoesNotExist:
                thisClass = None

            # Now call the index() view.
            # The user will be shown the homepage.
            return courseSpecificView(request, thisDept, thisNum, CURRENTSEMESTER)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = Course_SpecificForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'curves/add_data.html', {'form': form})
