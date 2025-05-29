
class Test:

    def __init__(self,*a):
        print("Default constructor called")
    
    # def __init__(self, a, b):
    #     print("Parameterized constructor called with values:", a, b)

    def __str__(self):
        return "This is a Test object"

t = Test(10,20)
t1 = Test(10,30)

print(t)

