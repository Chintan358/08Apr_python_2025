

class Demo:

    #data member - variables - attributes - state
    a = 10
    b = "hello"
    #function memeber - functons - methods - behavour
    def disp(self):
        print("disp calling")
        print(self.a,self.b)


d = Demo()
d.a = 50

d1 = Demo()


d.disp()
d1.disp()

