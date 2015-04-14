from django import forms
from curves.models import Course_Specific, User

pastSemClasses = []
grades = []

# form to get a class and a grade from a user
class Course_SpecificForm(forms.Form):
    curClasses = Course_Specific.objects.filter(semester="S2015")
    curGradesList = Course_Specific.CHOICES
    curGradesList.insert(0, ("N/A", "N/A"))
    pastSemClass1 = forms.ModelChoiceField(queryset = curClasses, help_text="Class*", required=True, error_messages={'required': 'Please enter class'})
    grade1 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade*")
    pastSemClass2 = forms.ModelChoiceField(queryset = curClasses, help_text="Class*", required=True, error_messages={'required': 'Please enter class'})
    grade2 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade*")
    pastSemClass3 = forms.ModelChoiceField(queryset = curClasses, help_text="Class*", required=True, error_messages={'required': 'Please enter class'})
    grade3 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade*")
    pastSemClass4 = forms.ModelChoiceField(queryset = curClasses, help_text="Class", required=False)
    grade4 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    pastSemClass5 = forms.ModelChoiceField(queryset = curClasses, help_text="Class", required=False)
    grade5 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    pastSemClass6 = forms.ModelChoiceField(queryset = curClasses, help_text="Class", required=False)
    grade6 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    pastSemClass7 = forms.ModelChoiceField(queryset = curClasses, help_text="Class", required=False)
    grade7 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    # pastSemClass = forms.ChoiceField(choices=curClassesList, help_text="Class")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('pastSemClass1', 'grade1', 'pastSemClass2', 'grade2', 'pastSemClass3', 'grade3', 'pastSemClass4', 'grade4', 'pastSemClass5', 'grade5', 'pastSemClass6', 'grade6', 'pastSemClass7', 'grade7')

    # def clean(self):
    #     print "hey there"
    #     for i in range(0, len(pastSemClasses)):
    #         print "yo"
    #         print self.cleaned_data[grades[i]]
    #         grade = self.cleaned_data[grades[i]]
    #         if grade == "N/A":
    #             print "yesiwajgs"
    #             raise forms.ValidationError("Please select a grade")
    #     return self.cleaned_data

    # def clean_grade1(self):
    #     grade = self.cleaned_data["grade1"]
    #     thisClass = self.cleaned_data["pastSemClass1"]
    #     if grade == "N/A" or thisClass == None:
    #         raise forms.ValidationError("Please select a class and a grade")
    #     return grade

    # def clean_grade2(self):
    #     grade = self.cleaned_data["grade2"]
    #     thisClass = self.cleaned_data["pastSemClass2"]
    #     if grade == "N/A" or thisClass == None:
    #         raise forms.ValidationError("Please select a class and a grade")
    #     return grade

    # def clean_grade3(self):
    #     grade = self.cleaned_data["grade3"]
    #     thisClass = self.cleaned_data["pastSemClass3"]
    #     if grade == "N/A" or thisClass == None:
    #         raise forms.ValidationError("Please select a class and a grade")
    #     return grade

    # def clean_grade4(self):
    #     grade = self.cleaned_data["grade4"]
    #     thisClass = self.cleaned_data["pastSemClass4"]
    #     print thisClass
    #     if grade == "N/A" and thisClass != None:
    #         raise forms.ValidationError("Please enter a grade")
    #     elif grade != "N/A" and thisClass == None:
    #         raise forms.ValidationError("Please select a class for this grade")
    #     return grade

    # def clean_grade5(self):
    #     grade = self.cleaned_data["grade5"]
    #     thisClass = self.cleaned_data["pastSemClass5"]
    #     if grade == "N/A" and thisClass != None:
    #         raise forms.ValidationError("Please enter a grade")
    #     elif grade != "N/A" and thisClass == None:
    #         raise forms.ValidationError("Please select a class for this grade")
    #     return grade

    # def clean_grade6(self):
    #     grade = self.cleaned_data["grade6"]
    #     thisClass = self.cleaned_data["pastSemClass6"]
    #     if grade == "N/A" and thisClass != None:
    #         raise forms.ValidationError("Please enter a grade")
    #     elif grade != "N/A" and thisClass == None:
    #         raise forms.ValidationError("Please select a class for this grade")
    #     return grade

    # def clean_grade7(self):
    #     grade = self.cleaned_data["grade7"]
    #     thisClass = self.cleaned_data["pastSemClass7"]
    #     if grade == "N/A" and thisClass != None:
    #         raise forms.ValidationError("Please enter a grade")
    #     elif grade != "N/A" and thisClass == None:
    #         raise forms.ValidationError("Please select a class for this grade")
    #     return grade

    def clean(self):
        cleaned_data = super(Course_SpecificForm, self).clean()
        y = range(1,4)
        requiredClasses = map(lambda x: "pastSemClass" + str(x), y)
        requiredGrades = map(lambda x: "grade" + str(x), y)
        z = range(4, 8)
        optionalClasses = map(lambda x: "pastSemClass" + str(x), z)
        optionalGrades = map(lambda x: "grade" + str(x), z)
        for i in range(0, len(requiredClasses)):
            thisGrade = cleaned_data.get(requiredGrades[i])
            if thisGrade == "N/A":
                self.add_error(requiredGrades[i], "Please enter grade")
        for i in range(0, len(optionalClasses)):
            thisClass = cleaned_data.get(optionalClasses[i])
            thisGrade = cleaned_data.get(optionalGrades[i])
            if thisGrade == "N/A" and thisClass != None:
                self.add_error(optionalGrades[i], "Please enter grade")
            elif thisGrade != "N/A" and thisClass == None:
                self.add_error(optionalClasses[i], "Please enter class")

class SearchForm(forms.Form):
    curClasses = Course_Specific.objects.filter(semester="S2015")
    curClassesList = []
    for j in range (0, len(curClasses)):
        curClass = (curClasses[j].__unicode__(), curClasses[j].__unicode__())
        curClassesList.append(curClass)
    curClassesList.sort()
    curProfs = []
    curDepts = []
    for c in Course_Specific.objects.all():
        if c.prof not in curProfs:
            curProfs.append(c.prof)
        if c.dept not in curDepts:
            curDepts.append(c.dept)
    curProfs.sort()
    curDepts.sort()
    allChoices = curClassesList + curProfs + curDepts
    search = forms.ChoiceField(choices = allChoices, help_text = "Class, Dept, or Professor")