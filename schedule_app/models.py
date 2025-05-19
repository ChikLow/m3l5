from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'name of subject:{self.name}'

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'name of teacher:{self.name}'

class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=1)

    def __str__(self):
        return f'name of class:{self.name}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'name of student:{self.name}'
    
class Schedule(models.Model):
    day = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'schedule:{self.day}, {self.hour}'
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return f'grade:{self.grade}'