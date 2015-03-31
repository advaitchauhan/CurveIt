from django import forms
from curves.models import Course_Specific, User

class Course_SpecificForm(forms.ModelForm):
    curClasses = Course_Specific.objects.all()
    curClassesList = []
    for j in range (0, len(curClasses)):
        curClass = (curClasses[j].__unicode__(), curClasses[j].__unicode__())
        curClassesList.append(curClass)
    print curClassesList
    pastSemClass = forms.ChoiceField(widget=forms.RadioSelect, choices=curClassesList, help_text="Class")
    grade = forms.ChoiceField(widget=forms.RadioSelect, choices=Course_Specific.CHOICES, help_text="Grade")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('pastSemClass', 'grade')
