import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CurveIt.settings')

import django
django.setup()

import sys

from curves.models import Course_Specific, Student

courses = []
coursesFound = []
total_A_plus = 0
total_A = 0
total_A_minus = 0
total_B_plus = 0
total_B = 0
total_B_minus = 0
total_C_plus = 0
total_C = 0
total_C_minus = 0
total_D_grade = 0
total_F_grade = 0
total_D_PDF = 0
total_F_PDF = 0
total_P_PDF = 0

def search(dept):
	global total_A_plus
	global total_A
	global total_A_minus
	global total_B_plus
	global total_B
	global total_B_minus
	global total_C_plus
	global total_C
	global total_C_minus
	global total_D_grade
	global total_F_grade
	global total_D_PDF
	global total_F_PDF
	global total_P_PDF
	for i in range(0, len(courses)):
		if courses[i].dept == dept:
			coursesFound.append(courses[i])
			total_A_plus += int(courses[i].num_A_plus)
			total_A += int(courses[i].num_A)
			total_A_minus += int(courses[i].num_A_minus)
			total_B_plus += int(courses[i].num_B_plus)
			total_B += int(courses[i].num_B)
			total_B_minus += int(courses[i].num_B_minus)
			total_C_plus += int(courses[i].num_C_plus)
			total_C += int(courses[i].num_C)
			total_C_minus += int(courses[i].num_C_minus)
			total_D_grade += int(courses[i].num_D_grade)
			total_F_grade += int(courses[i].num_F_grade)
			total_D_PDF += int(courses[i].num_D_PDF)
			total_F_PDF += int(courses[i].num_F_PDF)
			total_P_PDF += int(courses[i].num_P_PDF)

# Enter department as command line argument, and 
# this program will list the distribution of grades
# in this department
if __name__ == '__main__':
    print "Searching by Department"
    print ""
    courses = Course_Specific.objects.all()
    search(sys.argv[1])
    for i in range(0, len(coursesFound)):
    	print coursesFound[i]
    print "Total A+: " + str(total_A_plus)
    print "Total A: " + str(total_A)
    print "Total A-: " + str(total_A_minus)
    print "Total B+: " + str(total_B_plus)
    print "Total B: " + str(total_B)
    print "Total B-: " + str(total_B_minus)
    print "Total C+: " + str(total_C_plus)
    print "Total C: " + str(total_C)
    print "Total C-: " + str(total_C_minus)
    print "Total D for grade: " + str(total_D_grade)
    print "Total F for grade: " + str(total_F_grade)
    print "Total D PDF: " + str(total_D_PDF)
    print "Total F PDF: " + str(total_F_PDF)
    print "Total P PDF: " + str(total_P_PDF)
