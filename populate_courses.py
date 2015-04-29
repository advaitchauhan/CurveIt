import string
import json
import re
import sys
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')
import django
django.setup()

from curves.models import Course_Specific, Student


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
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2015", num_A_plus=random.randint(0,30), num_A=random.randint(0,30), num_A_minus=random.randint(0,30), num_B_plus=random.randint(0,30), num_B=random.randint(0,30), num_B_minus=random.randint(0,30), num_C_plus=random.randint(0,30), num_C_minus=random.randint(0,30), num_D=random.randint(0,30), num_F=random.randint(0,30)))

  for i in range(0, len(courseSpecifics)):
    courseSpecifics[i].calcAvg()
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
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2014", num_A_plus=random.randint(0,30), num_A=random.randint(0,30), num_A_minus=random.randint(0,30), num_B_plus=random.randint(0,30), num_B=random.randint(0,30), num_B_minus=random.randint(0,30), num_C_plus=random.randint(0,30), num_C=random.randint(0,30), num_C_minus=random.randint(0,30), num_D=random.randint(0,30), num_F=random.randint(0,30)))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].calcAvg()
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
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester="S2013", num_A_plus=random.randint(0,30), num_A=random.randint(0,30), num_A_minus=random.randint(0,30), num_B_plus=random.randint(0,30), num_B=random.randint(0,30), num_B_minus=random.randint(0,30), num_C_plus=random.randint(0,30), num_C=random.randint(0,30), num_D=random.randint(0,30), num_F=random.randint(0,30)))

  for i in range(0, len(courseSpecifics)):
      courseSpecifics[i].calcAvg()
      courseSpecifics[i].save()

main()