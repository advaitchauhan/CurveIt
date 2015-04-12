from django.db import models

# Represents a course (e.g. 'COS 333 Advanced Programming 
# Techniques' taught by a specific professor during a specific
# semester)
class Course_Specific(models.Model):
	CHOICES = [("A+", "A+"), ("A","A"), ("A-","A-"), ("B+", "B+"), ("B", "B"), ("B-", "B-"), ("C+", "C+"), ("C", "C"), ("C-", "C-"), ("D_grade", "D_grade"), ("F_grade", "F_grade"), ("D_PDF", "D_PDF"), ("F_PDF", "F_PDF"), ("P_PDF", "P_PDF")]
	PASTSEMCLASSES = (("COS 333 Advanced Programming Techniques", "COS 333 Advanced Programming Techniques"), ("MAT 201 Multivariable Calculus", "MAT 201 Multivariable Calculus"))
	dept = models.CharField(max_length = 40) # e.g. 'COS'
	num = models.CharField(max_length = 40) # e.g. '333'
	name = models.CharField(max_length = 100) # e.g. 'Advanced Programming Techniques'
	prof = models.CharField(max_length = 60) # e.g. 'Brian+Kernighan'
	semester = models.CharField(max_length = 5) # e.g. 'S2015' or 'F2015'
	num_A_plus = models.IntegerField(default = 0) 
	num_A = models.IntegerField(default = 0)
	num_A_minus = models.IntegerField(default = 0)
	num_B_plus = models.IntegerField(default = 0)
	num_B = models.IntegerField(default = 0)
	num_B_minus = models.IntegerField(default = 0)
	num_C_plus = models.IntegerField(default = 0)
	num_C = models.IntegerField(default = 0)
	num_C_minus = models.IntegerField(default = 0)
	num_D_grade = models.IntegerField(default = 0)
	num_F_grade = models.IntegerField(default = 0)
	num_D_PDF = models.IntegerField(default = 0)
	num_F_PDF = models.IntegerField(default = 0)
	num_P_PDF = models.IntegerField(default = 0)

	# increment grade counter for string grade (e.g. "A, B-, etc")
	def addGrade(self, grade):
		if grade == "A+":
			self.num_A_plus += 1
		elif grade == "A":
			self.num_A += 1
		elif grade == "A-":
			self.num_A_minus += 1
		elif grade == "B+":
			self.num_B_plus += 1
		elif grade == "B":
			self.num_B += 1
		elif grade == "B-":
			self.num_B_minus += 1
		elif grade == "C+":
			self.num_C_plus += 1
		elif grade == "C":
			self.num_C += 1
		elif grade == "C-":
			self.num_C_minus += 1
		elif grade == "D_grade":
			self.num_D_grade += 1
		elif grade == "F_grade":
			self.num_F_grade += 1
		elif grade == "D_PDF":
			self.num_D_PDF += 1
		elif grade == "F_PDF":
			self.num_F_PDF += 1
		elif grade == "P_PDF":
			self.num_P_PDF += 1

	# returns total number of grades (non PDF)
	def getTotalGrades(self):
		return self.num_A_plus + self.num_A + self.num_A_minus + self.num_B_plus + self.num_B + self.num_B_minus + self.num_C_plus + self.num_C + self.num_C_minus + self.num_D_grade + self.num_F_grade

	# returns total number of PDF grades
	def getTotalPDF(self):
		return self.num_P_PDF + self.num_D_PDF + self.num_F_PDF

	# returns a list of all number of grades (A+ to F_PDF)
	def getAllGrades(self):
		allGrades = [self.num_A_plus, self.num_A, self.num_A_minus, self.num_B_plus, self.num_B, self.num_B_minus, self.num_C_plus, self.num_C, self.num_C_minus, self.num_D_grade, self.num_F_grade]
		return allGrades
	
	def __unicode__(self): 
		result = ""
		depts = self.dept.split("+")  
		nums = self.num.split("+")
		# return string in format "COS 126/ EGR 126 General Computer Science"
		for i in range(0, len(depts)):
			if i == (len(depts)-1):
				result += depts[i] + " " + nums[i] + ": "
			else:
				result += depts[i] + " " + nums[i] + "/"         
		return result + self.name
		
class User(models.Model):
	netid = models.CharField(max_length = 20) # e.g. 'tylerh'
	has_Entered = models.BooleanField(default = False)

	def __unicode__(self):
		return self.netid + ": " + self.has_Entered
