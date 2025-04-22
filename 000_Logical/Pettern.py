# *****
# *****
# *****
# *****
# *****

# for j in range(1,10):
#     for i in range(1,8):
#         print("*",end="")
#     print()

# for i in range(5):
#     print("*"*5)

# *
# **
# ***
# ****
# *****


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# lines = 10
# starcount=1
# for i in range(1,lines):
#     for j in range(starcount):
#         print("*",end="")
#     print()
#     starcount+=1


# for i in range(5):
#     print("*"*(i+1))


# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


# lines = 10
# starcount=lines
# for i in range(1,lines+1):
#     for j in range(starcount):
#         print("*",end="")
#     print()
#     starcount-=1


# for i in range(5,0,-1):
#     print("*"*i)

#      *
#     **
#    ***
#   ****
#  *****

# lines = 5
# for i in range(lines,0,-1):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(lines-i+1):
#         print("*",end="")
#     print()


# lines = 6
# spacecount = lines
# starcount=1
# for i in range(1,lines):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,starcount+1):
#         print("*",end="")
#     print()
#     starcount+=1
#     spacecount-=1


# lines = 10
# for i in range(lines,0,-1):
#     print(" "*i,"*"*(lines-i+1))



#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

# lines = 10
# for i in range(lines,0,-1):
#     print(" "*i," *"*(lines-i+1))




lines = 20
for i in range(lines,0,-1):
    print(" "*i,"*"*((lines-i)*2+1))

    

# lines = 6
# spacecount = lines
# starcount=1
# for i in range(1,lines):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,starcount+1):
#         print("*",end="")
#     print()
#     starcount+=2
#     spacecount-=1


#      *
#     * *
#    * * *
#     * * 
#      *