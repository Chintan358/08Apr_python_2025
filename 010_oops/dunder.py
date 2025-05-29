# class Calc:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def __add__(self, other):
#         return self.a + other.a, self.b + other.b

#     def __eq__(self, value):
#         return self.a == value.a and self.b == value.b


# c1 = Calc(10,20)
# c2 = Calc(10,30)
# c3 = Calc(10,20)


# k = c1+c2
# print(k)  # Should print "Calc(40, 60)"

# print(c1==c2)

class Demo:

    def __init__(self, a):
        self.a = a

    def __getitem__(self, index):
        return self.a[index]
    
    def __setitem__(self, index, value):
        self.a[index] = value
    
d = Demo([1, 2, 3])
d[1] = 10
print(d[1])
print(d.a)
    