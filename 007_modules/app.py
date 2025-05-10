# import calc
# import calc as c
# from calc import add

# # k = calc.add(10,20)
# # k = c.add(10,20)
# k =add(20,50)
# print(k)


# from maths import calc
# from test import practice

# k = calc.add(10,20)
# print(k)

# practice.hello()

import math

# print(math.sqrt(16))
# print(math.ceil(5.1))
# print(math.floor(5.9))
# print(round(5.6))
# print(math.pow(5,2))

import os

# os.mkdir("Demo")
# os.rmdir("Demo")
# os.abort()
# os.system("shutdown -l")

# import random
# num = random.randint(100,999)
# print(num)

# import datetime

# x = datetime.datetime.now()
# print(x.date())
# print(x.time())

import calendar

# print(calendar.calendar(3050))

# print(calendar.month(2025,5))


import requests

k = requests.get("https://restcountries.com/v3.1/all")
data = k.json()

for i in data : 
    print(i['name']['common'])