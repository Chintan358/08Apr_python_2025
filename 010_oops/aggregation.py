
class Sample:

    def display(self):
        print("runnnig display of Sample")

class Demo:

    s = Sample()
    def show(self):
        print("running show of demo")


d = Demo()
d.show()
d.s.display()
