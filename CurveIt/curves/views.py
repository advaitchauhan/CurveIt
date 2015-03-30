from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from curves.models import Course_Specific
from curves.forms import Course_SpecificForm

# Create your views here.
def index(request):
	return render(request, 'curves/index.html')

#return a list of all classes that belong in the department, with links to them
def deptView(request, cdept):
	course_list = get_list_or_404(Course_Specific, dept = cdept)
	context = {'course_list': course_list, 'cdept': cdept}
	return render(request, 'curves/dept.html', context)

def courseSpecificView(request, cdept, cnum, ctime):
	course = get_object_or_404(Course_Specific, dept = cdept, num = cnum, semester = ctime)
	response = Course_Specific.printGrades(course)
	return HttpResponse(response)

def add_data(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = Course_SpecificForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = Course_SpecificForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'curves/add_data.html', {'form': form})
