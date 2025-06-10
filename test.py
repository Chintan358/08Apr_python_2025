
a = [10,20,30,4,6,9,25,225,100,50,75,80,90,95,99,225,101,102,103,104]


large = a[0] #225
slarge = a[0] #30 100
for i in a:
    if i > large:
        slarge = large
        large = i
    elif i > slarge and i != large:
        slarge = i


# print("The largest number in the list is:", large)

print("The second largest number in the list is:", slarge)