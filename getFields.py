import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')

import django
django.setup()

from curves.models import Course_Specific, User

classes = Course_Specific.objects.all()

allProfs = []
allDepts = []
allTitles = []

for c in classes:
	fields = c.printFields()
	if not fields['title'] in allTitles:
		allTitles.append(fields['title'])

	for prof in fields['profs']:
		if not prof in allProfs:
			allProfs.append(prof)

	for dept in fields['depts']:
		if not dept in allDepts:
			allDepts.append(dept)

allSearchFields = allProfs + allDepts + allTitles

for title in allTitles:
	print title

print "*******************************"
for prof in allProfs:
	print prof

print "*******************************"
for dept in allDepts:
	print dept



