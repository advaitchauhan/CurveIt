import autocomplete_light
autocomplete_light.autodiscover()

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from curves.models import Course_Specific, Student, QueryList
from curves.forms import Course_SpecificForm
from deptscript import depts
import json

CURRENTSEMESTER = "S2015"
GRADES = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D_grade", "F_grade"]

# Create your views here.
@login_required
def intro(request):
    return render(request, 'curves/intro.html')

@login_required

def index(request):
    if loggedIn(request) == False:
        return redirect('/intro/')
    #code here that goes through all the course-specifics and generates three lists of strings,
    #profs, depts, and courses, and we then pass this on as context to index.html.
    cachedList = QueryList.objects.all()
    if len(cachedList) == 0:
        classes = Course_Specific.objects.all()

        allProfs = []
        allProfsExact = []
        allDepts = []
        allDeptsExact = []
        allTitles = []
        allTitlesExact = []
        allCombined = []

        for c in classes:
            fields = c.printFields()
            if fields['title'] not in allTitlesExact:
                curDict = {}
                curData = {}
                curDict["value"] = fields['title']
                curData["cat"] = "Name"
                curDict["data"] = curData
                allTitles.append(curDict)
                allTitlesExact.append(fields['title'])

            for prof in fields['profs']:
                if prof not in allProfsExact:
                    curDict = {}
                    curData = {}
                    curDict["value"] = prof
                    curData["cat"] = "Professor"
                    curDict["data"] = curData
                    allProfs.append(curDict)
                    allProfsExact.append(prof)

            for dept in fields['depts']:
                if dept not in allDeptsExact:
                    curDict = {}
                    curData = {}
                    curDict["value"] = dept + ": " + depts[dept]
                    curData["cat"] = "Departments"
                    curDict["data"] = curData
                    allDepts.append(curDict)
                    allDeptsExact.append(dept)

        allCombined = allDepts + allTitles + allProfs
        allCombinedJSON = json.dumps(allCombined)

        q = QueryList()
        q.qlist = allCombinedJSON
        q.save()

    else:
        q = cachedList[0]

    context = {'allCombinedJSON': q.qlist}
    return render(request, 'curves/index.html', context)

# returns TRUE if user has a) already entered data OR b) is a freshman; else returns FALSE
def loggedIn(request):
    currentnetid = request.user.username
    thisUser = Student.objects.get(netid=currentnetid)
    return (thisUser.hasAccess())

@login_required 
# ex: curves/COS.  Shows dropdown for all distinct COS classes taught since birth, 
# plot of all time aggregate distribution, links to deptSpecific for each semester.
def deptView(request, cdept):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    # get all courses registered under the department, including those that are cross listed
    course_list = Course_Specific.objects.filter(dept__icontains = cdept) # includes all semesters
    if not course_list:
        return render(request, 'curves/404.html')
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

    cachedList = QueryList.objects.all()
    q = cachedList[0]

    # sem_list sorted in reverse so that they appear in reverse chronological order
    context = {'deptForPrint': depts[cdept.upper()], 'dept': cdept.upper(), 'course_list': uniqueCourse_list, 'dist': dist, 'total': total, 'sem_list': sorted(sem_list, reverse=True), 'allCombinedJSON': q.qlist}
    return render(request, 'curves/dept.html', context)

# ex: curves/COS/S2015.  Shows plot of grade distribution for all COS classes taught
# during the given semester.
@login_required
def deptSpecificView(request, cdept, ctime):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    # list of all classes in the department over all semesters
    allSemAllCourse = get_list_or_404(Course_Specific, dept__contains = cdept)
    # check that the dept exists for the semester
    course_list = Course_Specific.objects.filter(dept__contains = cdept, semester=ctime) # includes all semesters
    if not course_list:
        return render(request, 'curves/404.html')

    # all courses for current semester
    course_list = []
    # all semester for which classes under this dept were taught
    sem_list = []
    # get list of all distinct semesters
    for course in allSemAllCourse:
        # create list of all the classes in the current semester
        if course.semester == ctime:
            course_list.append(course)

        # create a list of all the distinct semesters
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

    cachedList = QueryList.objects.all()
    q = cachedList[0]

    # departments sorted in reverse so they appear like S2015 S2014, etc...
    context = {'deptForPrint': depts[cdept], 'dept': cdept, 'course_list': course_list, 'dist': dist, 'sem': ctime, 'sem_list': sorted(sem_list, reverse=True), 'allCombinedJSON': q.qlist}
    return render(request, 'curves/dept_specific.html', context)


@login_required
# ex: curves/prof/Brian%W.%Kernighan. Plot of all time aggregate distribution, links to
# professorSpecific for each semester, dropdown of all courses taught.
def profView(request, cprof):


    if loggedIn(request) == False:
        return redirect('/add_data/')
    allSemAllCourse = Course_Specific.objects.filter(prof__icontains = cprof)
    if not allSemAllCourse:
        return render(request, 'curves/404.html')
    # check that url is valid -- e.g. shouldn't be able to aggregate over "Douglas"
    uniqueProfs = []
    for a in allSemAllCourse:
        profs = a.prof.split("+")
        for p in profs:
            if p not in uniqueProfs:
                uniqueProfs.append(p)

    for u in uniqueProfs:
        if cprof == u:
            break
    else:
        return render(request, 'curves/404.html')



    sem_list = []
    course_list = []

    for c in allSemAllCourse:
        # get a list of all distinct courses
        for uniqueCourse in course_list:
            if c.num == uniqueCourse.num and c.dept == uniqueCourse.dept:
                break
        else:
            course_list.append(c)

        # get a list of all distinct semesters taught
        for sem in sem_list:
            if c.semester == sem:
                break
        else:
            sem_list.append(c.semester)

    # generate grade distibution across all courses taught
    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)

    cachedList = QueryList.objects.all()
    q = cachedList[0]

    context = {'course_list': course_list, 'sem_list': sorted(sem_list, reverse=True), 'profForPrint': cprof.replace("*", " "), 'prof': cprof, 'dist': dist, 'allCombinedJSON': q.qlist}
    return render(request, 'curves/prof.html', context)

# ex: curves/prof/Brian+W.+Kernighan/S2015.  Shows plot of grade distribution for all COS classes taught
# during the given semester, links to other semesters
def profSpecificView(request, cprof, ctime):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    allSemAllCourse = Course_Specific.objects.filter(prof__icontains = cprof)
    if not allSemAllCourse:
        return render(request, 'curves/404.html')
    # check that the prof data exists for the semester
    checkExists = Course_Specific.objects.filter(prof__icontains = cprof, semester=ctime)
    if not checkExists:
        return render(request, 'curves/404.html')
    # check that url is valid -- e.g. shouldn't be able to aggregate over "Douglas"
    uniqueProfs = []
    for a in allSemAllCourse:
        profs = a.prof.split("+")
        for p in profs:
            if p not in uniqueProfs:
                uniqueProfs.append(p)

    for u in uniqueProfs:
        if cprof == u:
            break
    else:
        return render(request, 'curves/404.html')

    course_list = []
    sem_list = []

    for c in allSemAllCourse:
        # create a list of all classes in the current semester
        if c.semester == ctime:
            course_list.append(c)

        # create a list of all semesters in which professor taught
        for sem in sem_list:
            if c.semester == sem:
                break
        else:
            sem_list.append(c.semester)

    # generate grade distribution across all coureses taught
    numGrades = [0] * len(GRADES);
    for course in course_list:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]

    dist = zip(GRADES, numGrades)

    cachedList = QueryList.objects.all()
    q = cachedList[0]

    context = {'course_list': course_list, 'sem_list': sorted(sem_list, reverse=True), 'profForPrint': cprof.replace("*", " "), 'prof': cprof, 'sem': ctime, 'dist': dist, 'allCombinedJSON': q.qlist}
    return render(request, 'curves/prof_specific.html', context)


@login_required
# ex: curves/COS/333. Plot of all time aggregate distribution, links to 
# courseSpecific for each semester
def courseView(request, cdept, cnum):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    # gets list of this course over all semesters
    course_list = Course_Specific.objects.filter(dept=cdept, num=cnum)
    if not course_list:
        return render(request, 'curves/404.html')

    # list of all semesters this class was taught
    sem_list = []

    # list of all professors who have taught this class
    prof_list = []
    prof_names_list = []

    numGrades = [0] * len(GRADES);
    for course in course_list:
        sem_list.append(course.semester)
        curProf = course.prof
        curProfs = curProf.split("+")
        for c in curProfs:
            for p in prof_list:
                if c == p:
                    break   
            else:
                prof_list.append(c)
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades[i] += grades[i]
    for p in prof_list:
        thisProf = p.replace("*", " ")
        prof_names_list.append(thisProf)

    # in order to pass in name of this class
    curCourse = course_list[0]
    dist = zip(GRADES, numGrades)
    profs = zip(prof_list, prof_names_list)
    total = sum(numGrades) 

    cachedList = QueryList.objects.all()
    q = cachedList[0]

    context = {'sem_list': sorted(sem_list, reverse=True), 'profs': profs, 'dist': dist,'total': total, 'name': curCourse.__unicode__(), 'course': curCourse, 'allCombinedJSON': q.qlist}
    return render(request, 'curves/course.html', context)

@login_required
# ex: curves/COS/333/S2015.  Plot of grade distribution for course taught during
# given semester.  Provide links to all other semesters for the course.  
def courseSpecificView(request, cdept, cnum, ctime):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    # course specific to the semester
    courseList = Course_Specific.objects.filter(dept = cdept, num = cnum, semester = ctime)
    if not courseList:
        return render(request, 'curves/404.html')
    else:
        course = courseList[0]
    # course over all semesters
    course_list = Course_Specific.objects.filter(dept = cdept, num = cnum)
    if not course_list:
        return render(request, 'curves/404.html')   
    # all semesters for which this class was taught
    sem_list = []
    for c in course_list:
        sem_list.append(c.semester)

    numGrades = course.getAllGrades()
    dist = zip(GRADES, numGrades)
    total = sum(numGrades)

    curProfsForPrint = []
    curProfs = []
    profs = course.prof.split("+")
    for p in profs:
        curProfs.append(p)
        curProfsForPrint.append(p.replace("*", " "))
    profs = zip(curProfs, curProfsForPrint)

    cachedList = QueryList.objects.all()
    q = cachedList[0]

    context = {'sem_list': sorted(sem_list, reverse=True), 'course': course, 'name': course.__unicode__(), 'dist': dist, 'total': total, 'profs': profs, 'allCombinedJSON': q.qlist}
    # context = {'course': course, "grades": GRADES, "numGrades": numGrades}
    return render(request, 'curves/course_specific.html', context)

@login_required
# page for user to input class/grade
def add_data(request):
    # if loggedIn(request):
    #     return redirect('/after_data/')

    # A HTTP POST?
    y = range(1,4)
    z = range(4,7)
    currentnetid = request.user.username

    #generate the variable names of values in the form.cleaned_data dictionary
    #pastSemClass1, pastSemClass2... 
    #grade1, grade2...
    requiredClasses = map(lambda x: "pastSemClass" + str(x), y)
    requiredGrades = map(lambda x: "grade" + str(x), y)
    optionalClasses = map(lambda x: "pastSemClass" + str(x), z)
    optionalGrades = map(lambda x: "grade" + str(x), z)


    if request.method == 'POST':
        form = Course_SpecificForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():

            #acknowledge student's adding of data
            thisUser = Student.objects.get(netid=currentnetid)
            thisUser.entered()
            thisUser.save()
            curData = form.cleaned_data #this is the data from the form

            #add grade to class for each class
            try:
                for i in range(0, len(requiredClasses)):
                    c = requiredClasses[i]
                    g = requiredGrades[i]
                    thisClass = curData[c] # i.e. AAS 210/MUS 253: Intro to...
                    thisGrade = curData[g] # gets grade chosen
                    thisClass.addGrade(thisGrade)
                    thisClass.save()
                for i in range(0, len(optionalClasses)):
                    thisClass = curData[optionalClasses[i]] # i.e. AAS 210/MUS 253: Intro to...
                    if thisClass != None:
                        thisGrade = curData[optionalGrades[i]] # gets grade chosen
                        thisClass.addGrade(thisGrade)
                        thisClass.save()
            except Course_Specific.DoesNotExist:
                thisClass = None

            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('/after_data/')
        else:
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = Course_SpecificForm()

    cachedList = QueryList.objects.all()
    q = cachedList[0]
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'curves/add_data.html', {'form': form, 'allCombinedJSON': q.qlist})

@login_required
def after_data(request):
    if loggedIn(request) == False:
        return redirect('/add_data/')

    cachedList = QueryList.objects.all()
    q = cachedList[0]
    context = {'allCombinedJSON': q.qlist}
    return render(request, 'curves/after_data.html', context)       

@login_required
def search(request):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    if 'q' in request.GET and request.GET['q'] and len(request.GET['q']) > 2:
        q = request.GET['q']

        #check if search term exactly matches a Course's unicode print
        for c in Course_Specific.objects.all():
            if unicode(c) == q:
                return courseView(request, c.dept, c.num)

        #check if search term is a department?
        if len(q) == 3:
            classes = Course_Specific.objects.filter(dept__iexact=q)
            if (len(classes) > 0):
                #context = {'classes': classes}
                #return render(request, 'curves/results.html', context)
                aClass = classes[0]
                return deptView(request, aClass.dept)

        if q.find(":") != -1:
            dept = (q.split(":"))[0]
            classes = Course_Specific.objects.filter(dept__iexact=dept)
            if (len(classes) > 0):
                #context = {'classes': classes}
                #return render(request, 'curves/results.html', context)
                aClass = classes[0]
                return deptView(request, aClass.dept)


        #check if the search term is part of a professor?
        qS = q.split(" ")
        classes = Course_Specific.objects.filter(prof__icontains=qS[0])
        for i in range(0, len(qS)):
            classes = classes.filter(prof__icontains=qS[i])
            #context = {'classes': classes}
            #return render(request, 'curves/results.html', context)
            #logic works temporarily, need autocomplete because currently
            #will just display view of the first found professor that matches query!
        if len(classes) > 0:
            profs = classes[0].prof.split("+")
            for p in profs:
                for s in qS:
                    if s.lower() not in p.lower():
                        break
                    else:
                        return profView(request, p)

        #check if search term is a dept/num combo
        #this is currently logically flawed, but i'll fix it later!
        #for example a crosslisted COS306/ELE206 would match ELE306    <-- fixed
        if len(q.split(" ")) == 2:
            qS = q.split(" ")
            classes = Course_Specific.objects.filter(dept__icontains=qS[0], num__icontains=qS[1])
            if (len(classes) > 0):
                #context = {'classes': classes}
                #return render(request, 'curves/results.html', context)
                for c in classes:
                    depts = c.dept.split("+")
                    nums = c.num.split("+")
                    for i in range(0, len(nums)):
                        if (depts[i] == qS[0].upper()) and (nums[i] == qS[1]):
                            return courseView(request, c.dept, c.num)

        #check if the search term is just a number?
        if len(q) <= 4:
            classes = Course_Specific.objects.filter(num__icontains=q)
            if (len(classes) == 1):
                aClass = classes[0]
                return courseView(request, aClass.dept, aClass.num)
            if (len(classes) > 0):
                uniqueClasses = []
                for c in classes:
                    for u in uniqueClasses:
                        if u.dept == c.dept:
                            break
                    else:
                        uniqueClasses.append(c)
                context = {'classes': uniqueClasses}
                return render(request, 'curves/results.html', context)

        #check if search term is part of a class title?
        classes = Course_Specific.objects.filter(name__icontains=q)
        if (len(classes) == 1):
            aClass = classes[0]
            return courseView(request, aClass.dept, aClass.num)
        elif (len(classes) > 0):
            uniqueClasses = []
            for c in classes:
                for u in uniqueClasses:
                    if u.dept == c.dept and u.num == c.num:
                        break
                else:
                    uniqueClasses.append(c)
            cachedList = QueryList.objects.all()
            qc = cachedList[0]
            context = {'classes': uniqueClasses, 'allCombinedJSON': qc.qlist}
            return render(request, 'curves/results.html', context)
        else:
            cachedList = QueryList.objects.all()
            qc = cachedList[0]
            context = {'query': q, 'allCombinedJSON': qc.qlist}
            return render (request, 'curves/invalid.html', context)
    else:
        cachedList = QueryList.objects.all()
        qc = cachedList[0]
        context = {'query': "BLANK", 'allCombinedJSON': qc.qlist}
        return render (request, 'curves/invalid.html', context)

    return HttpResponse(message)

@login_required
def handler404(request):
    cachedList = QueryList.objects.all()
    qc = cachedList[0]
    context = {'allCombinedJSON': qc.qlist}
    response = render(request, 'curves/404.html', context)
    response.status_code = 404
    return response

@login_required
def comparedeptView(request, cdept1, cdept2):
    if loggedIn(request) == False:
        return redirect('/curves/add_data')
    # get all courses registered under the department, including those that are cross listed
    course_list1 = Course_Specific.objects.filter(dept__icontains = cdept1) # includes all semesters
    if not course_list1:
        return render(request, 'curves/404.html')
    # construct list of unique course titles
    uniqueCourse_list1 = []
    # construct a list of all semesters for which we have data
    for course in course_list1:
        # get list of all distinct courses
        for uniqueCourse in uniqueCourse_list1:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list1.append(course)

    # aggregate all time grade distribution
    numGrades1 = [0] * len(GRADES)
    for course in course_list1:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades1[i] += grades[i]

    dist1 = zip(GRADES, numGrades1)
    total1 = sum(numGrades1)


    course_list2 = Course_Specific.objects.filter(dept__icontains = cdept2) # includes all semesters
        
    # construct list of unique course titles
    uniqueCourse_list2 = []
    # construct a list of all semesters for which we have data
    sem_list2 = []
    for course in course_list2:
        # get list of all distinct courses
        for uniqueCourse in uniqueCourse_list2:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list2.append(course)

    # aggregate all time grade distribution
    numGrades2 = [0] * len(GRADES)
    for course in course_list2:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades2[i] += grades[i]

    dist2 = zip(GRADES, numGrades2)
    total2 = sum(numGrades2)

    context = {'dept1ForPrint': depts[cdept1], 'dept1': cdept1, 'course_list1': uniqueCourse_list1, 'dist1': dist1, 'total1': total1, 'dept2ForPrint': depts[cdept2], 'dept2': cdept2, 'course_list2': uniqueCourse_list2, 'dist2': dist2, 'total2': total2}
    return render(request, 'curves/compdepttodept.html', context)


@login_required
# ex: curves/COS/333. Plot of all time aggregate distribution, links to 
# courseSpecific for each semester
def comparecourseView(request, cdept1, cnum1, cdept2, cnum2):
    if loggedIn(request) == False:
        return redirect('/add_data/')
    # gets list of this course over all semesters
    course_list1 = Course_Specific.objects.filter(dept=cdept1, num=cnum1)
    if not course_list1:
        return render(request, 'curves/404.html')

    numGrades1 = [0] * len(GRADES);
    for course in course_list1:
        grades1 = course.getAllGrades()
        for i in range(0, len(grades1)):
            numGrades1[i] += grades1[i]

    # in order to pass in name of this class
    curCourse1 = course_list1[0]
    dist1 = zip(GRADES, numGrades1)
    total1 = sum(numGrades1) 

    cachedList1 = QueryList.objects.all()
    q1 = cachedList1[0]

    #second course
    course_list2 = Course_Specific.objects.filter(dept=cdept2, num=cnum2)
    if not course_list2:
        return render(request, 'curves/404.html')

    numGrades2 = [0] * len(GRADES);
    for course in course_list2:
        grades2 = course.getAllGrades()
        for i in range(0, len(grades2)):
            numGrades2[i] += grades2[i]
<<<<<<< HEAD
    for p in prof_list2:
        thisProf2 = p.replace("*", " ")
        prof_names_list2.append(thisProf2)

=======
>>>>>>> d1d1a9af4b3356a86720794cdd74207647ca78f7
    # in order to pass in name of this class
    curCourse2 = course_list2[0]
    dist2 = zip(GRADES, numGrades2)
    total2 = sum(numGrades2) 

    cachedList2 = QueryList.objects.all()
    q2 = cachedList2[0]

    # condenses name for graph (e.g. COS 333)
    thisName1 = curCourse1.__unicode__();
    simpleName1 = (thisName1.split(":"))[0]
    thisName2 = curCourse2.__unicode__();
    simpleName2 = (thisName2.split(":"))[0]

    context = {'dist1': dist1,'total1': total1, 'simpleName1': simpleName1, 'name1': curCourse1.__unicode__(), 'course1': curCourse1, 'allCombinedJSON1': q1.qlist, 'dist2': dist2,'total2': total2, 'simpleName2': simpleName2, 'name2': curCourse2.__unicode__(), 'course2': curCourse2, 'allCombinedJSON2': q2.qlist, 'cdept1': cdept1, 'cdept2': cdept2, 'cnum1': cnum1, 'cnum2': cnum2}
    return render(request, 'curves/comparecourse.html', context)

@login_required
def compareProfView(request, cprof1, cprof2):
    if loggedIn(request) == False:
        return redirect('/curves/add_data')
    # get all courses registered under the department, including those that are cross listed
    course_list1 = Course_Specific.objects.filter(prof__icontains = cprof1) # includes all semesters
    if not course_list1:
        return render(request, 'curves/404.html')
    # construct list of unique course titles
    uniqueCourse_list1 = []
    # construct a list of all semesters for which we have data
    for course in course_list1:
        # get list of all distinct courses
        for uniqueCourse in uniqueCourse_list1:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list1.append(course)

    # aggregate all time grade distribution
    numGrades1 = [0] * len(GRADES)
    for course in course_list1:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades1[i] += grades[i]

    dist1 = zip(GRADES, numGrades1)
    total1 = sum(numGrades1)


    course_list2 = Course_Specific.objects.filter(prof__icontains = cprof2) # includes all semesters
        
    # construct list of unique course titles
    uniqueCourse_list2 = []
    # construct a list of all semesters for which we have data
    sem_list2 = []
    for course in course_list2:
        # get list of all distinct courses
        for uniqueCourse in uniqueCourse_list2:
            if course.num == uniqueCourse.num:
                break
        else:
            uniqueCourse_list2.append(course)

    # aggregate all time grade distribution
    numGrades2 = [0] * len(GRADES)
    for course in course_list2:
        grades = course.getAllGrades()
        for i in range(0, len(grades)):
            numGrades2[i] += grades[i]

    dist2 = zip(GRADES, numGrades2)
    total2 = sum(numGrades2)

    print dist1
    print dist2

    context = {'prof1ForPrint': cprof1.replace("*", " "), 'prof1': cprof1, 'course_list1': uniqueCourse_list1, 'dist1': dist1, 'total1': total1, 'prof2ForPrint': cprof2.replace("*", " "), 'prof2': cprof2, 'course_list2': uniqueCourse_list2, 'dist2': dist2, 'total2': total2}
    return render(request, 'curves/compareprof.html', context)