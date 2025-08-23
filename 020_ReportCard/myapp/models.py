from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_name=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.dept_name

class StudentId(models.Model):
    student_id=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.student_id

class Student(models.Model):
    dept_name = models.ForeignKey(Dept, on_delete=models.CASCADE)
    student_id= models.ForeignKey(StudentId,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


class Subject(models.Model):
    subject_name=models.CharField(max_length=20)

    # def __str__(self):
    #     return self.subject_name

class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()
