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
    # construct a list of all semesters for which we have data
    sem_list = []
    for course in course_list:
        # get list of all distinct courses
        for uniqueCourse in uniqueCourse_list:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list.append(course)
        # get list of all distinct semesters
        for sem in sem_list:
            if course.semester == sem:
                break
        else:
            sem_list.append(course.semester)

    # aggregate all time grade distribution
    numGrades = [0] * len(GRADES)
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)
    total = sum(numGrades)

    # sem_list sorted in reverse so that they appear in reverse chronological order
    context = {'dept': cdept, 'course_list': uniqueCourse_list, 'dist': dist, 'total': total, 'sem_list': sorted(sem_list, reverse=True)}
    return render(request, 'curves/dept.html', context)

# ex: curves/COS/S2015.  Shows plot of grade distribution for all COS classes taught
# during the given semester.
def deptSpecificView(request, cdept, ctime):
    # list of all classes in the department over all semesters
    allSemAllCourse = get_list_or_404(Course_Specific, dept__contains = cdept)

    # all courses for current semester
    course_list = []
    # all semester for which classes under this dept were taught
    sem_list = []
    # get list of all distinct semesters
    for course in allSemAllCourse:
        if course.semester == ctime:
            course_list.append(course)
        for sem in sem_list:
            if course.semester == sem:
                break
        else:
            sem_list.append(course.semester)

    numGrades = [0] * len(GRADES)
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)

    # departments sorted in reverse so they appear like S2015 S2014, etc...
    context = {'dept': cdept, 'course_list': course_list, 'dist': dist, 'sem': ctime, 'sem_list': sorted(sem_list, reverse=True)}
    return render(request, 'curves/dept_specific.html', context)


@login_required
# ex: curves/prof/Brian+W.+Kernighan
def profView(request, cprof):
    # All courses over all semesters for which this prof was teacher
    course_list = get_list_or_404(Course_Specific, prof__contains = cprof)
    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    # creates unique list of courses (will be overlap because course_list is all semester)
    uniqueCourse_list = []
    for course in course_list:
        for uniqueCourse in uniqueCourse_list:
            if course.num == uniqueCourse.num and course.dept == uniqueCourse.dept:
                break
        else:
            uniqueCourse_list.append(course)

    dist = zip(GRADES, numGrades)
    total = sum(numGrades)
    context = {'uniqueCourse_list': uniqueCourse_list, 'cprof': cprof.replace("+", " "), 'dist': dist, 'total': total}
    return render(request, 'curves/prof.html', context)

@login_required
# ex: curves/COS/333. Plot of all time aggregate distribution, links to 
# courseSpecific for each semester
def courseView(request, cdept, cnum):
    # gets list of this course over all semesters
    course_list = get_list_or_404(Course_Specific, dept=cdept, num=cnum)

    # list of all semesters this class was taught
    sem_list = []

    numGrades = [0] * len(GRADES);
    for course in course_list:
        sem_list.append(course.semester)
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    # in order to pass in name of this class
    curCourse = course_list[0]
    dist = zip(GRADES, numGrades)
    total = sum(numGrades) 
    context = {'sem_list': sorted(sem_list, reverse=True), 'dist': dist,'total': total, 'name': curCourse.__unicode__(), 'course': curCourse}
    return render(request, 'curves/course.html', context)

@login_required
# ex: curves/COS/333/S2015.  Plot of grade distribution for course taught during
# given semester.  Provide links to all other semesters for the course.  
def courseSpecificView(request, cdept, cnum, ctime):
    # course specific to the semester
    course = Course_Specific.objects.get(dept = cdept, num = cnum, semester = ctime)
    # course over all semesters
    course_list = get_list_or_404(Course_Specific, dept = cdept, num = cnum)    
    # all semesters for which this class was taught
    sem_list = []
    for c in course_list:
        sem_list.append(c.semester)

    numGrades = course.getAllGrades()
    dist = zip(GRADES, numGrades)
    print dist
    total = sum(numGrades)
    
    context = {'sem_list': sorted(sem_list, reverse=True), 'course': course, 'name': course.__unicode__(), 'dist': dist, 'total': total, 'profForPrint': course.prof.replace("+", " "), 'prof': course.prof}
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
                thisGrade = curData["grade"] # gets grade chosen
                thisClassInfo = thisClass.split("/") # i.e. ["AAS 210", "MUS 253: Intro to..."]
                lastString = thisClassInfo[len(thisClassInfo)-1]
                lastDept = (lastString)[0:lastString.index(":")] # gets department i.e. "MUS 253"
                thisName = (lastString)[(lastString.index(":") + 2):] # gets name i.e. "Intro to...""

                # now thisClassInfo is a list of all dist/num pairs
                thisClassInfo = thisClassInfo[:-1] 
                thisClassInfo.append(lastDept) # i.e. ["AAS 210", "MUS 253"]

                # will be a list of depts in format AAS+MUS
                depts = ""
                # will be a list of nums 210+253
                nums = ""

                for i in range(0, len(thisClassInfo)):
                    curListings = thisClassInfo[i].split()
                    thisDept = curListings[0]
                    thisNum = curListings[1]
                    if i == (len(thisClassInfo) - 1):
                        depts += thisDept
                        nums += thisNum
                    else:
                        depts += thisDept + "+"
                        nums += thisNum + "+"

                thisClass = get_object_or_404(Course_Specific, dept=depts, num=nums, semester=CURRENTSEMESTER)

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
