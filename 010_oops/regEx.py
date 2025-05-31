import re

# r  =re.search('\S',"hello  python")
# r  =re.search('\d',"hello 12 python")

# r = re.match("\d","1Hello python 123")


# number = input("Enter number : ")
# r = re.match("[0-9]{10}",number)
# if r is None:
#     print("Invalid number")
# else : 
#     print("success")

# email = "test@gmail.com"
# pettenr = "^[a-zA-Z0-9]+@[a-zA-Z]+\\.[a-z]{1,3}$"

# r = re.match(pettenr,email)
# print(r)


# r= re.split("\d","Hello 1 python Hello tops")

# r= re.sub("[A-Z]","k","Hello 1 python Hello tops")

r= re.findall("H[a-z]*o","Hello Hfdfdffdo 1 python Hello tops Heo")

print(r)