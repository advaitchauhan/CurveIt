import autocomplete_light
autocomplete_light.autodiscover()

from django import forms
from curves.models import Course_Specific, Student

pastSemClasses = []
grades = []

# form to get a class and a grade from a user
class Course_SpecificForm(forms.Form):
    curClasses = Course_Specific.objects.filter(semester="S2015")
    curGradesList = Course_Specific.CHOICES
    curGradesList.insert(0, ("N/A", "N/A"))
    pastSemClass1 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=True)
    grade1 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade*")
    pastSemClass2 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=True)
    grade2 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade*")
    pastSemClass3 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=True)
    grade3 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade*")
    pastSemClass4 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=False)
    grade4 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    pastSemClass5 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=False)
    grade5 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    pastSemClass6 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=False)
    grade6 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    pastSemClass7 = forms.ModelChoiceField(queryset = curClasses, widget=autocomplete_light.ChoiceWidget('Course_SpecificAutocomplete'), help_text="Class*", required=False)
    grade7 = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    # pastSemClass = forms.ChoiceField(choices=curClassesList, help_text="Class")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('pastSemClass1', 'grade1', 'pastSemClass2', 'grade2', 'pastSemClass3', 'grade3', 'pastSemClass4', 'grade4', 'pastSemClass5', 'grade5', 'pastSemClass6', 'grade6', 'pastSemClass7', 'grade7')

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
        z = range(4, 8)
        optionalClasses = map(lambda x: "pastSemClass" + str(x), z)
        optionalGrades = map(lambda x: "grade" + str(x), z)


        #grab the required classes
        for i in range(0, len(requiredClasses)):
            thisGrade = cleaned_data.get(requiredGrades[i])
            thisClass = cleaned_data.get(requiredClasses[i])
            required_Courses.append(thisClass)
            if thisGrade == "N/A":
                self.add_error(requiredGrades[i], "This field is required.")

        #grab the optional classes, perform error checking with the grabbed classes
        for i in range(0, len(optionalClasses)):
            thisClass = cleaned_data.get(optionalClasses[i])
            optional_Courses.append(thisClass)
            thisGrade = cleaned_data.get(optionalGrades[i])
            if thisGrade == "N/A" and thisClass != None:
                self.add_error(optionalGrades[i], "Please enter grade.")
            elif thisGrade != "N/A" and thisClass == None:
                self.add_error(optionalClasses[i], "Please enter class.")
        for i in range(0, len(required_Courses)):
            for j in range(0, len(required_Courses)):
                if i != j:
                    if required_Courses[i] != None and required_Courses[j] != None:
                        if required_Courses[i] == required_Courses[j]:
                            self.add_error(requiredClasses[j], "Please do not select a class more than once.")
        for i in range(0, len(optional_Courses)):
            for j in range(0, len(optional_Courses)):
                if i != j:
                    if optional_Courses[i] != None and optional_Courses[j] != None:
                        if optional_Courses[i] == optional_Courses[j]:
                            self.add_error(optionalClasses[j], "Please do not select a class more than once")
