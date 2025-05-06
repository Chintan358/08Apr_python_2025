
def test():
    print("test")
    

def message():
    return "Hello, World!"

def add(a, b):
    return a + b

# test()
# c = message()
# print(c)

# a = add(1, 2)
# print(a)




# def person(name,age=25,email="test@gmail.com"):
#     print("Name:", name)
#     print("Age:", age)
#     print("Email:", email)

# # person("harsh",25,"harsh@gmail.com")
# person("abc",email="abc@gmail.com")


# def add(*a):
#     print(a)

# def data(**kwargs):
   
#     print(kwargs)


# add(1,2,3,4,5,6,7,8,9)
# data(abc="123",xyz="456",pqr="789")



    
# a = lambda x,y: x+y
# square = lambda x: x*x

# print(square(5))
# print(a(1,2))




a = 20
def test():
    global a
    a = 25
    print(a)


print(a)
test()
print(a)


#prime number

# def is_prime(n):
#     if n <= 1:                    
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def prime_numbers(n):
#     primes = []
#     for i in range(2, n + 1):



#*
#**
#***
#****
#*****

# def print_star(n):
#     for i in range(n):    
#         for j in range(i+1):
#             print("*",end="")
#         print()
#     return primes
