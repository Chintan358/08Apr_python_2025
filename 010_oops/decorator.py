

# def before(func):
#     def wrapper(*a,**b):
#         print("Before function execution")
#         func(*a,**b)
#         print("After function execution")
#     return wrapper

# @before
# def test(a):
#     print("Test function executed!")


# test(10)

def add(func):
    def wrapper(*a):
        sum = 0
        for i in a:
            sum += i
        print(f"Sum of {a} is {sum}")        
    return wrapper

@add
def calc(a,b):
    pass

calc(10,20)