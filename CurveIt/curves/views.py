from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from curves.models import Course_Specific
from curves.forms import Course_SpecificForm
import json

CURRENTSEMESTER = "S2015"
GRADES = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D_grade", "F_grade"]

# Create your views here.
@login_required

def index(request):
	return render(request, 'curves/index.html')

@login_required 
#return a list of all classes that belong in the department, with links to them
def deptView(request, cdept):
    course_list = get_list_or_404(Course_Specific, dept = cdept)
    uniqueCourse_list = []
    for course in course_list:
        for uniqueCourse in uniqueCourse_list:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list.append(course)
    numGrades = [0] * len(GRADES)
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)
    total = sum(numGrades)

    context = {'dept': cdept, 'uniqueCourse_list': uniqueCourse_list, 'dist': dist, 'total': total}
    return render(request, 'curves/dept.html', context)

@login_required
#return a list of all classes that are taught by cprof, with links to them
def profView(request, cprof):
    print cprof
    course_list = get_list_or_404(Course_Specific, prof = cprof)
    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    uniqueCourse_list = []
    for course in course_list:
        for uniqueCourse in uniqueCourse_list:
            if course.num == uniqueCourse.num and course.dept == uniqueCourse.dept:
                break
        else:
            uniqueCourse_list.append(course)
    dist = zip(GRADES, numGrades)
    total = sum(numGrades)
    context = {'uniqueCourse_list': uniqueCourse_list, 'cprof': cprof.replace("/", " "), 'dist': dist, 'total': total}
    return render(request, 'curves/prof.html', context)

@login_required
# view associated with a specific course
def courseView(request, cdept, cnum):
    course_list = get_list_or_404(Course_Specific, dept = cdept, num = cnum)
    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    curCourse = course_list[0]
    dist = zip(GRADES, numGrades)
    total = sum(numGrades) 
    context = {'course_list': course_list, 'dist': dist, 'total': total, 'dept': curCourse.dept, 'coursenum': curCourse.num, 'name': curCourse.name}
    return render(request, 'curves/course.html', context)


@login_required
# view associated with a specific course
def courseSpecificView(request, cdept, cnum, ctime):
    course = get_object_or_404(Course_Specific, dept = cdept, num = cnum, semester = ctime)
    course_list = get_list_or_404(Course_Specific, dept = cdept, num = cnum)
    numGrades = course.getAllGrades()
    dist = zip(GRADES, numGrades)
    print dist
    total = sum(numGrades)
    curCourse = course_list[0]
    
    context = {'course_list': course_list,'course': course.name, 'name': curCourse.name, 'prof': course.prof, 'dept': course.dept, 'coursenum': course.num, 'dist': dist, 'total': total}
    # context = {'course': course, "grades": GRADES, "numGrades": numGrades}
    return render(request, 'curves/course_specific.html', context)

@login_required
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
