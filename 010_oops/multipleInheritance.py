
class A:

    def display(self):
        print("runing display of A")
    
    def show(self):
        print("runing show of A")

class B:

    def display(self):
        print("runing display of B")

    

class C(B,A):
    pass


c = C()
c.display()
c.show()