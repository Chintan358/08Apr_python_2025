

# f = open("test.txt",'w')
# f.write("Something about java")
# f.close()

# f = open("test.txt",'r')
# data = f.read()
# print(data)
# f.close()


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if not data:
#         break
#     print(data)
# f.close()

# f  = open("test.txt",'r')
# k = f.readlines()
# print(k)


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if not data:
#         break
#     # if data.startswith("t"):
#     #  print(data)
#     if data.__contains__("java"):
#         print(data)
    
# f.close()


# f = open("test.txt",'a')
# f.write("\n Hello python")
# f.close()


# with open("test.txt",'r') as f:
#     f.seek(15)
#     print(f.tell())
#     data = f.read()
#     print(data)
#     print(f.tell())

# with open("home.txt",'w+') as f:
#     f.write("Write something")
#     f.seek(0)
#     data = f.read()
#     print(data)


# with open("test.jpg",'rb') as f:
#     data = f.read()
#     print(data)


import json

# data = {
#     "name":"Tops",
#     "email":"tops@gmail.com",
#     "phone":"748596855"
# }

# with open("db.json",'w') as f:
#     json.dump(data,f)


with open("abc.xls",'w') as f:
    f.write("something")