from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    classroom = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name