from django.db import models

class Course(models.Model):
	dept = models.CharField(max_length=3)
