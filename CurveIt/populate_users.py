import json
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')
import django
django.setup()
from curves.models import User

def main():
	Users = []
	User.objects.all().delete()
	jsonFile = open("students.json")
	studentList = json.loads(jsonFile.readline())
	for student in studentList:
		studentDict = {}
		name = student[0]
		year = student[1]
		email = student[2]
		netid = email[0:email.index("@")]
		Users.append(User(netid=netid, name=name, year=year))

	for user in Users:
		user.save()

main()