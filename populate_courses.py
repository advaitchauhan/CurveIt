import string
import json
import re
import sys
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')
import django
django.setup()

from curves.models import Course_Specific, Student, QueryList, QueryCourseList, QueryProfList, QueryDeptList

# return a dictionary containing grade distribution for a course-specific
def distributeGrades():
  dist = {'P': 0, 'F': 0, 'D': 0, 'C-': 0, 'C': 0, 'C+': 0, 'B-': 0, 'B': 0, 'B+': 0, 'A-': 0, 'A': 0, 'A+': 0}

  # probability 1/3 professor is easy, 1/3 professor is avg, 1/3 professor is harsh
  difficulty = random.randint(0, 2)
  for i in range(0, 100):
    # Pass/D/Fail with probability 0.1 < p < 0.2
    p = random.uniform(0.1, 0.2)
    x = random.random()
    if x < p:
      dist['P'] +=1
    # otherwise, take for a grade
    else:
      # Average difficulty
      if difficulty == 0:
        z = random.normalvariate(0, 1)
        if z < -2.5:
          dist['F'] += 1
        elif z < -2:
          dist['D'] += 1
        elif z < -1.5:
          dist['C-'] += 1
        elif z < -1:
          dist['C'] += 1
        elif z < -0.5:
          dist['C+'] += 1
        elif z < 0:
          dist['B-'] += 1
        elif z < 0.5:
          dist['B'] += 1
        elif z < 1:
          dist['B+'] += 1
        elif z < 1.5:
          dist['A-'] += 1
        elif z < 2:
          dist['A'] += 1
        else:
          dist['A+'] += 1
      # Easy difficulty
      elif difficulty == 1:
        z = 0 - random.expovariate(0.4)
        if z < -10:
          dist['F'] += 1
        elif z < -9:
          dist['D'] += 1
        elif z < -8:
          dist['C-'] += 1
        elif z < -7:
          dist['C'] += 1
        elif z < -6:
          dist['C+'] += 1
        elif z < -5:
          dist['B-'] += 1
        elif z < -4:
          dist['B'] += 1
        elif z < -3:
          dist['B+'] += 1
        elif z < -2:
          dist['A-'] += 1
        elif z < -1:
          dist['A'] += 1
        else:
          dist['A+'] += 1
      # Hard difficulty
      elif difficulty == 2:
        z = random.expovariate(0.4)
        if z > 10:
          dist['A+'] += 1
        elif z > 9:
          dist['A'] += 1
        elif z > 8:
          dist['A-'] += 1
        elif z > 7:
          dist['B+'] += 1
        elif z > 6:
          dist['B'] += 1
        elif z > 5:
          dist['B-'] += 1
        elif z > 4:
          dist['C+'] += 1
        elif z > 3:
          dist['C'] += 1
        elif z > 2:
          dist['C-'] += 1
        elif z > 1:
          dist['D'] += 1
        else:
          dist['F'] += 1
  return dist

def populate(filename, sem):
  courses = []
  courseSpecifics = []
  # Spring 2015
  jsonFile = open(filename);

  # read past first line
  line = jsonFile.readline();

  line = jsonFile.readline();
  # while line isn't empty...
  while (len(line) > 0):
    # deal with commas in middle of course name (Registrar issue)
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
    # for each professor of the course
    for i in range(0, len(profs)):
      profname = (profs[i])["name"]

      # deal with commas in middle of prof name (Registrar issue)
      index = profname.find(",")
      if index != -1:
        profname = profname[0:index]

      # add a space between first, middle, last names of professor
      names = profname.replace(" ", "*")

      # if there's another professor after this one, add a plus between their names
      if i < (len(profs) - 1):
        thisProf += names + "+" 
      else:
        thisProf += names

    # get department + reference number listings (e.g. COS 333)
    listings = course["listings"]
    theseDepts = []
    theseNums = []
    # account for cross-listed classes
    if len(listings) > 0:
      for listing in listings:
        theseDepts.append(listing["dept"])
        theseNums.append(listing["number"]) 

    thisDept = ""
    thisNum = ""
    # add a '+' between all departments in which the course is listed
    for i in range(0, len(theseDepts)):
      if i == (len(theseDepts) - 1):
        thisDept += theseDepts[i]
      else:
        thisDept += theseDepts[i] + "+"  

    # add a '+' between all reference numbers under which the course is listed
    for i in range(0, len(theseNums)):
      if i == (len(theseNums) - 1):
        thisNum += theseNums[i]
      else:
        thisNum += theseNums[i] + "+"    

    # (e.g. Advanced Programming Techniques)
    thisTitle = course["title"]

    # Randomly generate grade distribution for this class
    dist = distributeGrades()

    # add the course specific to the model
    courseSpecifics.append(Course_Specific(dept=thisDept, num=thisNum, name=thisTitle, prof=thisProf, semester=sem, num_A_plus=dist['A+'], num_A=dist['A'], num_A_minus=dist['A-'], num_B_plus=dist['B+'], num_B=dist['B'], num_B_minus=dist['B-'], num_C_plus=dist['C+'], num_C=dist['C'], num_C_minus=dist['C-'], num_D=dist['D'], num_F=dist['F'], num_P=dist['P']))

  # calculate the grade average for the course and save it in the course-specific model
  for i in range(0, len(courseSpecifics)):
    courseSpecifics[i].calcAvg()
    courseSpecifics[i].save()

def main():
  # clear database
  Course_Specific.objects.all().delete()
  QueryList.objects.all().delete()
  QueryCourseList.objects.all().delete() 
  QueryProfList.objects.all().delete()
  QueryDeptList.objects.all().delete()
  
  sem = "2015 Spring"
  filename = "reg2.json"
  populate(filename, sem)

  sem = "2014 Spring"
  filename = "reg4.json"
  populate(filename, sem)

  sem = "2013 Spring"
  filename = "reg6.json"
  populate(filename, sem)

  # Add in titleString field -- necessary for autocomplete
  courses = Course_Specific.objects.all()
  for c in courses:
    titleString = "" 
    depts = c.dept.split("+") 
    nums = c.num.split("+")
    
    #create string in format "COS 126/EGR 126: General Computer Science"
    for i in range(0, len(depts)):
      if i == (len(depts)-1):
        titleString += depts[i] + " " + nums[i] + ": "
      else:
        titleString += depts[i] + " " + nums[i] + "/" 
    titleString += c.name
    c.titleString = titleString
    c.save()

main()

