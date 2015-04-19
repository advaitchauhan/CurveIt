from curves.models import Course_Specific, User

classes = Course_Specific.objects.all()
for c in classes:
	print c.prof