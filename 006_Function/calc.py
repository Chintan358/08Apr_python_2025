

def add(a, b):
    return a + b

def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def power(a, b):
    return a ** b
def floor_div(a, b):
    return a // b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = input("Enter choice: ")

if choice ==  '+':
    print(add(a, b))
elif choice == '-':
    print(sub(a, b))
elif choice == '*':
    print(mul(a, b))
elif choice == '/':
    print(div(a, b))
elif choice == '%':
    print(mod(a, b))
elif choice == '**':
    print(power(a, b))
elif choice == '//':
    print(floor_div(a, b))



