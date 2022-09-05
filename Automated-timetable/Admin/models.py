from django.db import models

# Create your models here.

class Timetable(models.Model):
	course_name = models.CharField(max_length=50)
	Program_name = models.CharField(max_length=100)

