

# def hello(a):
#     print("Hello",a)
#     a+=1
#     if a<50 :
#         hello(a)

# hello(10)



def factorial(n): #5
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))