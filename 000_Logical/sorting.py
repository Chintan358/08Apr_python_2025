

a = [10,20,5,64,8,9] #

# 10 5 20 8 9 64
# 5 10 8 9 20
# 5 8 9 10 
# 5 8 9 
# 5 8 
# 5 

for i in range(len(a)):
    for j in range(1,len(a)-i):
        if a[j-1]>a[j]:
            temp = a[j-1]
            a[j-1] = a[j]
            a[j] = temp      
print(a)