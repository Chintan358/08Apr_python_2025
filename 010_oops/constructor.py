import sys
import gc
class Student:

    __clg = "drstc"
   
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def display(self):
        print(self.id, self.name,self.clg)
    
    @classmethod
    def test(cls):
        cls.clg = "abc"
        print("test calling...")
    
    @staticmethod
    def show():
        print("Show calling...")


# c = gc.collect()
# print(c)
# s = Student(10,"Vishal")
# s.display()


# s1 = Student(20,"tops")
# s1.display()

# print(Student.clg)

# s.test()
# s.show()



# Student.show()
# def xyz(a):
#     print(a)

# c  =gc.collect()
# print(c)

# for i in range(10):
#     xyz(i)

# print(sys.getrefcount(s))
# k  = gc.collect()
# print(k)

Student.__clg = "test"

import keyword

print(len(keyword.kwlist))
