# from multipledispatch import dispatch
# class Sample:

#     @dispatch(int, int)
#     def add(self, a, b):
#         print(a + b)
    
#     @dispatch(int, int, int)
#     def add(self, a, b, c):
#         print(a + b + c)


# s1 = Sample()
# s1.add(1, 2) 
# s1.add(10,20,30) # This will raise an error because the second add method overrides the first one

class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"  # Calls the speak method of the parent class


d = Dog()
print(d.speak(10,20))  # Output: Animal speaks