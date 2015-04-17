import string
import json
import re
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')
import django
django.setup()

from curves.models import Course_Specific, User


def main():
  courses = []
  courseSpecifics = []
  Course_Specific.objects.all().delete()
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
  
  for course in courses:
    profs = course["profs"]
    thisProf = ""
    for i in range(0, len(profs)):
      curProf = (profs[i])["name"]
      names = curProf.replace(" ", "*")
      if i < (len(profs) - 1):
        thisProf += names + "+" 
      else:
        thisProf += names
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
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2015", num_A_plus=20, num_A=30, num_A_minus=35, num_B_plus=20, num_B=11, num_B_minus=8, num_C_plus=4, num_C_minus=8))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].save()

  courses = []
  courseSpecifics = []
  jsonFile = open("reg4.json");
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
  
  for course in courses:
    profs = course["profs"]
    thisProf = ""
    for i in range(0, len(profs)):
      curProf = (profs[i])["name"]
      names = curProf.replace(" ", "*")
      if i < (len(profs) - 1):
        thisProf += names + "+" 
      else:
        thisProf += names
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
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2014", num_A_plus=1, num_A=9, num_A_minus=26, num_B_plus=20, num_B=28, num_B_minus=29, num_C_plus=35, num_C=20, num_C_minus=19, num_D_grade=18, num_F_grade=10))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].save()

  courses = []
  courseSpecifics = []
  jsonFile = open("reg6.json");
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
  
  for course in courses:
    profs = course["profs"]
    thisProf = ""
    for i in range(0, len(profs)):
      curProf = (profs[i])["name"]
      names = curProf.replace(" ", "*")
      if i < (len(profs) - 1):
        thisProf += names + "+" 
      else:
        thisProf += names
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
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2013", num_A_plus=10, num_A=9, num_A_minus=43, num_B_plus=40, num_B=50, num_B_minus=27, num_C_plus=8, num_C=19, num_D_grade=16, num_F_grade=7))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].save()

main()