import string
import json
import re
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')
import django
django.setup()

from curves.models import Course_Specific, User

courses = []
courseSpecifics = []


def main():
  jsonFile = open("reg2.json");
  line = jsonFile.readline();
  line = jsonFile.readline();
  while (len(line) > 0):
    if line[len(line)-2] == ',':
      line = line[0:len(line)-2]
    else:
      line = line[0:len(line)-1]
    j = json.loads(line)
    courses.append(j)
    line = jsonFile.readline();

  Course_Specific.objects.all().delete()
  
  for course in courses:
    profs = course["profs"]
    if len(profs) > 0:
      thisProf = (profs[0])["name"]
      names = thisProf.split()
      thisProf = names[len(names)-1]
      print thisProf
    else:
      thisProf = ""
    listings = course["listings"]
    if len(listings) > 0:
      thisDept = (listings[0])["dept"]
      thisNum = (listings[0])["number"]
    else:
      thisDept = ""
      thisNum = ""    
    thisTitle = course["title"]
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2015", num_A_plus=20, num_A=23, num_A_minus=35, num_B_plus=41, num_B=30, num_B_minus=26, num_C_plus=18, num_C=20, num_C_minus=12, num_D_grade=50, num_F_grade=52,))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].save()



main()