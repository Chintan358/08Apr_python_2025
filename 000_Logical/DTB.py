number = 458
binary = 0
multipyer = 1
while number !=0:
    rem = number%2
    binary = binary+(rem*multipyer)
    number//=2
    multipyer*=10

print(binary)


