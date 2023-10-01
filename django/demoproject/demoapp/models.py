from django.db import models

# Create your models here.
class college(models.Model):
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 50)
    strength = models.IntegerField()
    website = models.URLField()

class Principal(models.Model):
    CollegeID = models.OneToOneField(college, on_delete=models.CASCADE)
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Subject(models.Model):
    Subjectcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.IntegerField()

class Teacher(models.Model):
    TeacherID = models.IntegerField(primary_key=True)
    subjectcode = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)