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
# ex: curves/COS.  Shows dropdown for all distinct COS classes taught since birth, 
# plot of all time aggregate distribution, links to deptSpecific for each semester.
def deptView(request, cdept):
    # get all courses registered under the department, including those that are cross listed
    course_list = get_list_or_404(Course_Specific, dept__contains = cdept) # includes all semesters
    # construct list of unique course titles
    uniqueCourse_list = []
    for course in course_list:
        for uniqueCourse in uniqueCourse_list:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list.append(course)

    # aggregate all time grade distribution
    numGrades = [0] * len(GRADES)
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)
    total = sum(numGrades)

    context = {'dept': cdept, 'uniqueCourse_list': uniqueCourse_list, 'dist': dist, 'total': total}
    return render(request, 'curves/dept.html', context)

# ex: curves/COS/S2015.  Shows plot of grade distribution for all COS classes taught
# during the given semester.
def deptSpecific(request, cdept, ctime):
    pass


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
# ex: curves/COS/333. Plot of all time aggregate distribution, links to 
# courseSpecific for each semester
def courseView(request, cdept, cnum):
    course_list = get_list_or_404(Course_Specific, dept = cdept, num = cnum)

    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    print numGrades
    curCourse = course_list[0]
    dist = zip(GRADES, numGrades)
    total = sum(numGrades) 
    context = {'course_list': course_list, 'dist': dist,'total': total, 'name': curCourse.__unicode__(), 'course': curCourse}
    return render(request, 'curves/course.html', context)

# Further narrow query on our side.  Ex: query for WWWS 598 would return 
# WWS 590/POL 598, WWS 598/POP 508.  Narrow it down to the latter.
def narrowList(potentialClasses):
    thisClass = potentialClasses[0]
    for c in potentialClasses:
        if c.name == thisName:
            thisClass = c
            break
    return thisClass


@login_required
# ex: curves/COS/333/S2015.  Plot of grade distribution for course taught during
# given semester.  Provide links to all other semesters for the course.  
def courseSpecificView(request, cdept, cnum, ctime):
    # course specific to the semester
    course = Course_Specific.objects.get(dept = cdept, num = cnum, semester = ctime)
    # all semesters of the course
    course_list = get_list_or_404(Course_Specific, dept = cdept, num = cnum)

    

    numGrades = course.getAllGrades()
    dist = zip(GRADES, numGrades)
    print dist
    total = sum(numGrades)
    curCourse = course_list[0]
    
    context = {'course_list': course_list,'course': curCourse, 'name': curCourse.__unicode__(), 'dist': dist, 'total': total}
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
                thisClass = curData["pastSemClass"] # i.e. AAS 210/MUS 253: Intro to...
                thisClassInfo = thisClass.split("/") # i.e. ["AAS 210", "MUS 253: Intro to..."]
                lastString = thisClassInfo[len(thisClassInfo)-1]
                lastDept = (lastString)[0:lastString.index(":")] # gets department i.e. "MUS 253"
                thisName = (lastString)[(lastString.index(":") + 2):] # gets name i.e. "Intro to...""
                # now thisClassInfo is a list of all dist/num pairs
                thisClassInfo = thisClassInfo[:-1] 
                thisClassInfo.append(lastDept) # i.e. ["AAS 210", "MUS 253"]

                curClass = thisClassInfo[0] # first listing
                curListings = curClass.split()
                thisDept = curListings[0] # department of first listing
                thisNum = curListings[1] # number of first listing
                potentialClasses = get_list_or_404(Course_Specific, dept__contains=thisDept, num__contains=thisNum, semester=CURRENTSEMESTER)

                thisClass = potentialClasses[0] # initialize
                for c in potentialClasses:
                    if c.name == thisName:
                        thisClass = c
                        break

                thisGrade = curData["grade"]

                thisClass.addGrade(thisGrade)
                thisClass.save()
            except Course_Specific.DoesNotExist:
                thisClass = None

            # Now call the index() view.
            # The user will be shown the homepage.
            return courseSpecificView(request, thisClass.dept, thisClass.num, CURRENTSEMESTER)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = Course_SpecificForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'curves/add_data.html', {'form': form})
