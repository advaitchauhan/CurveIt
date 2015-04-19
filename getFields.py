import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')

import django
django.setup()

from curves.models import Course_Specific, User

classes = Course_Specific.objects.all()
for c in classes:
	print c.prof