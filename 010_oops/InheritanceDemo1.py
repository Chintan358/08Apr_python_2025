class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        print(self.a,self.b)

class B(A):

    def __init__(self,a,b,c):
        A.__init__(self,a,b)
        self.c = c

    def show(self):
        print(self.a, self.b, self.c)


a = A(10,20)
a.display()

b = B(50,60,70)
b.show()
