from django import forms
from curves.models import Course_Specific, User

class Course_SpecificForm(forms.ModelForm):
    CHOICES = ((1, "A+"), (2,"A"), (3,"A-"), (4, "B+"), (5, "B"), (6, "B-"), (7, "C+"), (8, "C"), (9, "C-"), (10, "D_grade"), (11, "F_grade"), (12, "D_PDF"), (13, "F_PDF"), (14, "P_PDF"))
    dept = forms.CharField(max_length = 3, help_text="Dept Name") 
    num = forms.CharField(max_length = 4, help_text="Course Number")
    semester = forms.CharField(max_length = 10 ,help_text="Semester")
    grade = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, help_text="Grade")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('dept', 'num', 'semester', 'grade')
