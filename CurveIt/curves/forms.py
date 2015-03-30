from django import forms
from curves.models import Course_Specific, User

class Course_SpecificForm(forms.ModelForm):
    dept = forms.CharField(max_length = 3, help_text="Dept Name") 
    num = forms.CharField(max_length = 4, help_text="Course Number")
    name = forms.CharField(max_length = 100, help_text="Course Name")
    prof = forms.CharField(max_length = 50, help_text="Prof Name")
    semester = forms.CharField(max_length = 5 ,help_text="Semester")
    num_A_plus = forms.IntegerField(help_text="num A+")
    # grade = forms.CharField(max_length = 6, help_text="Grade")
    # num_A_plus = forms.CharField(widget=forms.HiddenInput())
    # num_A = forms.CharField(widget=forms.HiddenInput())
    # num_A_minus = forms.CharField(widget=forms.HiddenInput())
    # num_B_plus = forms.CharField(widget=forms.HiddenInput())
    # num_B = forms.CharField(widget=forms.HiddenInput())
    # num_B_minus = forms.CharField(widget=forms.HiddenInput())
    # num_C_plus = forms.CharField(widget=forms.HiddenInput())
    # num_C = forms.CharField(widget=forms.HiddenInput())
    # num_C_minus = forms.CharField(widget=forms.HiddenInput())
    # num_D_grade = forms.CharField(widget=forms.HiddenInput())
    # num_F_grade = forms.CharField(widget=forms.HiddenInput())
    # num_D_PDF = forms.CharField(widget=forms.HiddenInput())
    # num_F_PDF = forms.CharField(widget=forms.HiddenInput())
    # num_P_PDF = forms.CharField(widget=forms.HiddenInput())
    # if grade == "A+":
    #     num_A_plus = 1
    # elif grade == "A":
    #     num_A = 1
    # elif grade == "A-":
    #     num_A_minus = 1
    # elif grade == "B+":
    #     num_B_plus = 1
    # elif grade == "B":
    #     num_B = 1
    # elif grade == "B-":
    #     num_B_minus = 1
    # elif grade == "C+":
    #     num_C_plus = 1
    # elif grade == "C":
    #     num_C = 1
    # elif grade == "C-":
    #     num_C_minus = 1
    # elif grade == "D_grade":
    #     num_D_grade = 1
    # if grade == "F_grade":
    #     num_F_grade = 1
    # elif grade == "P_PDF":
    #     num_P_PDF = 1
    # if grade == "D_PDF":
    #     num_D_PDF = 1
    # elif grade == "F_PDF":
    #     num_F_PDF = 1

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('dept', 'num', 'name', 'prof', 'num_A_plus')
