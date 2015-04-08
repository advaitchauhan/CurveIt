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
      names = thisProf.replace(" ", "/")
      print thisProf
    else:
      thisProf = ""
    listings = course["listings"]
    theseDepts = []
    theseNums = []
    if len(listings) > 0:
      for listing in listings:
        theseDepts.append(listing["dept"])
        theseNums.append(listing["number"]) 
    thisDept = ""
    thisNum = ""
    for i in range(0, len(theseDepts)):
      if i == (len(theseDepts) - 1):
        thisDept += theseDepts[i]
      else:
        thisDept += theseDepts[i] + "+"  
    for i in range(0, len(theseNums)):
      if i == (len(theseNums) - 1):
        thisNum += theseNums[i]
      else:
        thisNum += theseNums[i] + "+"    
    thisTitle = course["title"]
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=names, semester="S2015", num_A_plus=20))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].save()



main()