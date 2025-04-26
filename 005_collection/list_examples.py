
# l = [10,20,30,40,50,60,"Python",56.23,False]
# print(l)
# print(len(l))
# print(type(l))

# thelist = list((10,20,30,45))
# print(thelist)


#Access List
# subject = ["Python","Java","Php","Node","Android"]
# print(subject)
# print(subject[4])
# print(subject[-4])
# print(subject[1:3])
# print(subject[2:])
# print("Python" in subject)

#Change the list items
# subject = ["Python","Java","Php","Node","Android"]
# # subject[1] = "React"
# # subject[1:3] = ["A","B","C"]
# subject.insert(1,"React")
# print(subject)

#Add List Items

# thelist = [10,20,30,40,50]
# thelist.append(56)

# dlist = [100,200,300,400]
# thelist.extend(dlist)
# thelist.extend("Hello")
# dlist.extend(thelist)
# print(thelist)
# print(dlist)


#Remove Items
# l = [10,20,30,50,60,90]

# l.remove(10)
# l.pop(4)
# l.clear()
# del l
# print(l)

#Loop list
# l = [1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])
# k = []
# for i in l:
#     if i%2==0:
#         k.append(i)
# k = (x for x in l if x%2==0)
# k = (x*x for x in l)
# print(list(k))

#Sort list

a = [5,4,3,6,7,8,4,1]
# # a.sort(reverse=True)
# a.reverse()
# print(a)

# b = list(a)
# b = a.copy()
# b = a
# b = a[:]
# print(b)

print(a.count(4))
print(a.index(5))  