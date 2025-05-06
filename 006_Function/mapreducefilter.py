

# l = [10,20,30,40,50,60]
# i = [1,2,3,4,5,6]

# def square(a):
#     return a*a

# for i in l:
#     k = square(i)
#     print(k)

# k = map(square,l)
# print(list(k))

# k = map(pow,l,i)
# print(list(k))

import math

a = [1,2,5,6,7,9,4,11]

def checkeven(a):
    if a%2==0:
        return a
    

# k = filter(checkeven,a)
# k = filter(lambda num:num%2!=0,a)
# print(list(k))


def checkpsquare(a):
     k = math.sqrt(a)
     return k.is_integer()

# for i in a:
#     k = checkpsquare(i)
#     print(k)

# k  =filter(checkpsquare,a)

# k = filter(lambda num : math.sqrt(num).is_integer(),a)
# print(list(k))


# names = ["harsh","kamlesh","pratibha","vishal","vatsal"]

# k = filter(lambda name : name.startswith("v"),names)
# print(list(k))


from functools import reduce

a = [10,20,30,40,50,60]

# def sum(x,y):
#     # print(x,y)
#     return x+y

# k = reduce(sum,a)
# k = reduce(lambda x,y:x+y,a)
k = reduce(lambda x,y: max(x,y),a)
print(k)

