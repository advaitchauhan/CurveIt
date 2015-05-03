from django.db import models

# Represents a course (e.g. 'COS 333 Advanced Programming 
# Techniques' taught by a specific professor during a specific
# semester)
class Course_Specific(models.Model):
	CHOICES = [("A+", "A+"), ("A","A"), ("A-","A-"), ("B+", "B+"), ("B", "B"), ("B-", "B-"), ("C+", "C+"), ("C", "C"), ("C-", "C-"), ("D", "D"), ("F", "F"), ("P", "P")]
	PASTSEMCLASSES = (("COS 333 Advanced Programming Techniques", "COS 333 Advanced Programming Techniques"), ("MAT 201 Multivariable Calculus", "MAT 201 Multivariable Calculus"))
	
	dept = models.CharField(max_length = 40) # e.g. 'COS'
	num = models.CharField(max_length = 40) # e.g. '333'
	name = models.CharField(max_length = 200) # e.g. 'Advanced Programming Techniques'
	prof = models.CharField(max_length = 200) # e.g. 'Brian+Kernighan'
	semester = models.CharField(max_length = 11) # e.g. '2015 Spring' or '2014 Fall'
	num_A_plus = models.IntegerField(default = 0) 
	num_A = models.IntegerField(default = 0)
	num_A_minus = models.IntegerField(default = 0)
	num_B_plus = models.IntegerField(default = 0)
	num_B = models.IntegerField(default = 0)
	num_B_minus = models.IntegerField(default = 0)
	num_C_plus = models.IntegerField(default = 0)
	num_C = models.IntegerField(default = 0)
	num_C_minus = models.IntegerField(default = 0)
	num_D = models.IntegerField(default = 0)
	num_F = models.IntegerField(default = 0)
	num_P = models.IntegerField(default = 0)
	titleString = models.CharField(default = "blank", max_length = 200)
	avg = models.DecimalField(default = 0, max_digits=3, decimal_places=2)

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
		elif grade == "D":
			self.num_D += 1
		elif grade == "F":
			self.num_F += 1
		elif grade == "P":
			self.num_P += 1

	# returns total number of grades (non P)
	def getTotalGrades(self):
		return self.num_A_plus + self.num_A + self.num_A_minus + self.num_B_plus + self.num_B + self.num_B_minus + self.num_C_plus + self.num_C + self.num_C_minus + self.num_D + self.num_F

	# returns a list of all number of grades (A+ to F_PDF)
	def getAllGrades(self):
		allGrades = [self.num_A_plus, self.num_A, self.num_A_minus, self.num_B_plus, self.num_B, self.num_B_minus, self.num_C_plus, self.num_C, self.num_C_minus, self.num_D, self.num_F, self.num_P]
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

	def printFields(self):
		searchList = {}
		# {'prof': ['a', 'b'], 'title': 'a', 'dept': 'COS'}

		#parse out professor strings
		profStrings = []
		profs = self.prof.split("+")
		for p in profs:
			profStrings.append(p.replace('*', ' '))

		#parse out department strings
		depts = self.dept.split("+") 


		#parse out class title
		titleString = "" 
		nums = self.num.split("+")
		# return string in format "COS 126/ EGR 126 General Computer Science"
		for i in range(0, len(depts)):
			if i == (len(depts)-1):
				titleString += depts[i] + " " + nums[i] + ": "
			else:
				titleString += depts[i] + " " + nums[i] + "/" 
		titleString += self.name

		#add them all to the dictionary
		searchList['title'] = titleString
		searchList['depts'] = depts
		searchList['profs'] = profStrings

		return searchList

	def calcAvg(self):
		total = self.num_A_plus * 4 + self.num_A * 4 + self.num_A_minus * 3.7 + self.num_B_plus * 3.3 + self.num_B * 3 + self.num_B_minus * 2.7 + self.num_C_plus * 2.3 + self.num_C * 2 + self.num_C_minus * 1.7 + self.num_D
		self.avg = total / self.getTotalGrades()

	def getAvg(self):
		return self.avg

class QueryList(models.Model):
	qlist = models.TextField(null = True)
	def __unicode__(self):
		return self.qlist

class QueryProfList(models.Model):
	qlist = models.TextField(null = True)
	def __unicode__(self):
		return self.qlist

class QueryDeptList(models.Model):
	qlist = models.TextField(null = True)
	def __unicode__(self):
		return self.qlist

class QueryCourseList(models.Model):
	qlist = models.TextField(null = True)
	def __unicode__(self):
		return self.qlist
		
class Student(models.Model):
	netid = models.CharField(max_length = 50) # e.g. 'tylerh'
	name = models.CharField(max_length = 100, default="")
	year = models.CharField(max_length = 4, default="")
	has_Entered = models.BooleanField(default = False)
	# is_Prof = models.BooleanField(default = False)

	def getNetid(self):
		return self.netid

	def hasAccess(self):
		return self.has_Entered or (self.year == "2018")

	def getYear(self):
		return self.year

	def entered(self):
		self.has_Entered = True

	# def isProf(self):
	# 	self.is_Prof = True

	def __unicode__(self):
		return self.netid
