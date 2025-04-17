
a = 153
number  =a
count = 0
while a !=0:
    a//=10
    count+=1

temp = number
sum = 0
while number !=0 :
    rem = number%10
    sum += pow(rem,count)
    number = number//10
   
if temp == sum:
    print("Armstrong")
else : 
    print("Not armstrong")