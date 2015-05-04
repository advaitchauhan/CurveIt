from django import forms
from curves.models import Course_Specific, Student
from deptscript import depts

pastSemClasses = []
grades = []

def isCourse(courseString):
    print "checking if it is a course!"
    for c in Course_Specific.objects.all():
        # print courseString
        # print c.titleString
        if c.titleString == courseString:
            return True
    return False

# form to get a class and a grade from a user
class Course_SpecificForm(forms.Form):
    curClasses = Course_Specific.objects.filter(semester="2015 Spring")
    curGradesList = Course_Specific.CHOICES
    curGradesList.insert(0, ("N/A", "Enter Grade"))
    pastSemClass1 = forms.CharField(required=True)
    grade1 = forms.ChoiceField(choices=Course_Specific.CHOICES, label = "gradeInput", help_text="Grade*")
    pastSemClass2 = forms.CharField(required=True)
    grade2 = forms.ChoiceField(choices=Course_Specific.CHOICES, label = "gradeInput", help_text="Grade*")
    pastSemClass3 = forms.CharField(required=True)
    grade3 = forms.ChoiceField(choices=Course_Specific.CHOICES, label = "gradeInput",  help_text="Grade*")
    pastSemClass4 = forms.CharField(required = False)
    grade4 = forms.ChoiceField(choices=Course_Specific.CHOICES, label = "gradeInput", help_text="Grade")
    pastSemClass5 = forms.CharField(required = False)
    grade5 = forms.ChoiceField(choices=Course_Specific.CHOICES, label = "gradeInput", help_text="Grade")
    pastSemClass6 = forms.CharField(required = False)
    grade6 = forms.ChoiceField(choices=Course_Specific.CHOICES, label = "gradeInput", help_text="Grade")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('pastSemClass1', 'grade1', 'pastSemClass2', 'grade2', 'pastSemClass3', 'grade3', 'pastSemClass4', 'grade4', 'pastSemClass5', 'grade5', 'pastSemClass6', 'grade6')


    #method for ERROR CHECKING
    def clean(self):
        cleaned_data = super(Course_SpecificForm, self).clean()
        y = range(1,4)
        required_Courses = []
        optional_Courses = []

        #CREATE list of names of objects in the cleaned_data.form
        #pastSemClass1, pastSemClass2... (names of)
        #grade1, grade2...
        requiredClasses = map(lambda x: "pastSemClass" + str(x), y)
        requiredGrades = map(lambda x: "grade" + str(x), y)
        z = range(4, 7)
        optionalClasses = map(lambda x: "pastSemClass" + str(x), z)
        optionalGrades = map(lambda x: "grade" + str(x), z)


        #grab the required classes
        for i in range(0, len(requiredClasses)):
            thisGrade = cleaned_data.get(requiredGrades[i])
            thisClass = cleaned_data.get(requiredClasses[i])
            if not isCourse(thisClass):
                self.add_error(requiredClasses[i], "Please select a valid class")

            required_Courses.append(thisClass)
            if thisGrade == "N/A" or thisClass == None:
                self.add_error(requiredGrades[i], "Please enter both a class and a grade")

        #grab the optional classes, perform error checking with the grabbed classes
        for i in range(0, len(optionalClasses)):
            thisClass = cleaned_data.get(optionalClasses[i])
            if not isCourse(thisClass):
                self.add_error(requiredClasses[i], "Please select a valid class")

            optional_Courses.append(thisClass)
            thisGrade = cleaned_data.get(optionalGrades[i])
            if thisGrade == "N/A" and thisClass != None:
                self.add_error(optionalGrades[i], "Please enter grade.")
            elif thisGrade != "N/A" and thisClass == None:
                self.add_error(optionalClasses[i], "Please enter class.")

        all_Courses = required_Courses + optional_Courses
        errors = [False]*6
        # checks that a class has not been selected more than once
        for i in range(0, len(all_Courses)):
            for j in range(0, len(all_Courses)):
                if i != j:
                    if all_Courses[i] != None and all_Courses[j] != None:
                        if errors[j] == False:
                            if all_Courses[i] == all_Courses[j]:
                                if j < len(required_Courses):
                                    self.add_error(requiredClasses[j], "Please do not select a class more than once.")
                                    errors[j] = True
                                else:
                                    self.add_error(optionalClasses[j - len(required_Courses)], "Please do not select a class more than once.")
                                    errors[j] = True

class compProfForm(forms.Form):
    prof1 = forms.CharField(required=True)
    prof2 = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super(compProfForm, self).clean()
        p1 = cleaned_data.get("prof1")
        p2 = cleaned_data.get("prof2")
        if p1 == None:
            pass;
        else:
            p1 = p1.replace(" ", "*")
            allSemAllCourse = Course_Specific.objects.filter(prof__icontains = p1)
            # check that url is valid -- e.g. shouldn't be able to aggregate over "Douglas"
            uniqueProfs1 = []
            for a in allSemAllCourse:
                profs = a.prof.split("+")
                for p in profs:
                    if p not in uniqueProfs1:
                        uniqueProfs1.append(p)

            for u in uniqueProfs1:
                if p1 == u:
                    break
            else:
                self.add_error("prof1", "Please select a valid professor")

        if p2 == None:
            pass;
        else:
            p2 = p2.replace(" ", "*")
            allSemAllCourse = Course_Specific.objects.filter(prof__icontains = p2)
            # check that url is valid -- e.g. shouldn't be able to aggregate over "Douglas"
            uniqueProfs2 = []
            p2 = p2.replace(" ", "*")
            for a in allSemAllCourse:
                profs = a.prof.split("+")
                for p in profs:
                    if p not in uniqueProfs2:
                        uniqueProfs2.append(p)

            for u in uniqueProfs2:
                if p2 == u:
                    break
            else:
                self.add_error("prof2", "Please select a valid professor")
        if (p1 == p2):
            self.add_error("prof1", "Please select two different professors.")
            self.add_error("prof2", "Please select two different professors.")

class compDeptForm(forms.Form):
    dept1 = forms.CharField(required=True)
    dept2 = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super(compDeptForm, self).clean()
        d1s = cleaned_data.get("dept1")
        d2s = cleaned_data.get("dept2")
        if d1s == None:
            pass;
        else:
            d1s = d1s.split(":")
            d1 = d1s[0]

            allSemAllCourse = Course_Specific.objects.filter(dept__icontains = d1)
            # check that url is valid -- e.g. shouldn't be able to aggregate over "Douglas"
            uniqueDepts1 = []
            for a in allSemAllCourse:
                deps = a.dept.split("+")
                for d in deps:
                    if d not in uniqueDepts1:
                        uniqueDepts1.append(d)

            for u in uniqueDepts1:
                if d1 == u:
                    break
            else:
                self.add_error("dept1", "Please select a valid Department")
        if d2s == None:
            pass;
        else:
            d2s = d2s.split(":")
            d2 = d2s[0]
            allSemAllCourse = Course_Specific.objects.filter(dept__icontains = d2)
            # check that url is valid -- e.g. shouldn't be able to aggregate over "Douglas"
            uniqueDepts2 = []
            for a in allSemAllCourse:
                deps = a.dept.split("+")
                for d in deps:
                    if d not in uniqueDepts2:
                        uniqueDepts2.append(d)

            for u in uniqueDepts2:
                if d2 == u:
                    break
            else:
                self.add_error("dept2", "Please select a valid Department")
        if d1s != None and d2s != None:
            if (d1 == d2):
                self.add_error("dept1", "Please select two different departments.")
                self.add_error("dept2", "Please select two different departments.")

class compCourseForm(forms.Form):
    course1 = forms.CharField(required=True)
    course2 = forms.CharField(required=True)

    def clean(self):
        allSemAllCourse = Course_Specific.objects.all()
        cleaned_data = super(compCourseForm, self).clean()
        c1 = cleaned_data.get("course1")
        c2 = cleaned_data.get("course2")
        if c1 == None:
            pass;
        else:
            for a in allSemAllCourse:
                if a.__unicode__() == c1:
                    break
            else:
                self.add_error("course1", "Please select a valid course")
        if c2 == None:
            pass;
        else:
            for a in allSemAllCourse:
                if a.__unicode__() == c2:
                    break
            else:
                self.add_error("course2", "Please select a valid course")
        if (c1 != None and c2 != None):
            if (c1 == c2):
                self.add_error("course1", "Please select two different courses.")
                self.add_error("course2", "Please select two different courses.")