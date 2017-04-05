from django.db import models

from department.models import Department

# Create your models here.

class Student(models.Model):
	roll_no = models.IntegerField(null = True, blank=True)
	name = models.CharField(max_length=128)
	course_name = models.CharField(max_length=128, null = True, blank=True)
	Department = models.ForeignKey(Department, null = True, blank=True)