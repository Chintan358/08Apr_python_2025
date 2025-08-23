from faker import Faker
from myapp.models import *
fake = Faker()
import random

def generate(n=50):
    depts = Dept.objects.all()
    for i in range(n):
        dept = depts[random.randint(0,len(depts)-1)]
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        student_id = StudentId.objects.create(student_id=f"STD_{random.randint(100,999)}")
        
        Student.objects.create(name=name,email=email,phone=phone,dept_name=dept,student_id=student_id)

def marks():
    students = Student.objects.all()
    subjects = Subject.objects.all()

    for student in students:
        for subject in subjects:
            marks = random.randint(1,100)
            Marks.objects.create(student=student,subject=subject,marks=marks)
