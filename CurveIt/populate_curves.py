import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')

import django
django.setup()

from random import randint

from curves.models import Course_Specific, User

newCourse = Course_Specific(dept="MAT", num="201", name="Multivariable Calculus", prof="Sarkar", semester="Fall 2014")

def addOneGrade():
	num = randint(1,14)
	if num == 1:
		newCourse.addGrade("A+")
	elif num == 2:
		newCourse.addGrade("A")
	elif num == 3:
		newCourse.addGrade("A-")
	elif num == 4:
		newCourse.addGrade("B+")
	elif num == 5:
		newCourse.addGrade("B")
	elif num == 6:
		newCourse.addGrade("B-")
	elif num == 7:
		newCourse.addGrade("C+")
	elif num == 8:
		newCourse.addGrade("C")
	elif num == 9:
		newCourse.addGrade("C-")
	elif num == 10:
		newCourse.addGrade("D_grade")
	elif num == 11:
		newCourse.addGrade("F_grade")
	elif num == 12:
		newCourse.addGrade("P_PDF")
	elif num == 13:
		newCourse.addGrade("D_PDF")
	else:
		newCourse.addGrade("F_PDF")

def populate():
	for i in range(0, 1000):
		addOneGrade()

def showGrades():
	totalGrades = newCourse.getTotalGrades()
	totalPDF = newCourse.getTotalPDF()
	print "A+: " + str(newCourse.num_A_plus)
	print "A: " + str(newCourse.num_A)
	print "A-: " + str(newCourse.num_A_minus)
	print "B+: " + str(newCourse.num_B_plus)
	print "B: " + str(newCourse.num_B)
	print "B-: " + str(newCourse.num_B_minus)
	print "C+: " + str(newCourse.num_C_plus)
	print "C: " + str(newCourse.num_C)
	print "C-: " + str(newCourse.num_C_minus)
	print "D for grade: " + str(newCourse.num_D_grade)
	print "F for grade: " + str(newCourse.num_F_grade)
	print "D PDF: " + str(newCourse.num_D_PDF)
	print "F PDF: " + str(newCourse.num_F_PDF)
	print "P PDF: " + str(newCourse.num_P_PDF)
	print "Total for Grade: " + str(newCourse.getTotalGrades())
	print "Total PDF: " + str(newCourse.getTotalPDF())
	print "Total: " + str(newCourse.getTotalGrades() + newCourse.getTotalPDF())

# Start execution here!
if __name__ == '__main__':
    print "Starting curves population script..."
    print "\n"
    print newCourse
    populate()
    showGrades()
