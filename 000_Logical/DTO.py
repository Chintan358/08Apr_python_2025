number = 458
ocatal = 0
multipyer = 1
while number !=0:
    rem = number%8
    ocatal = ocatal+(rem*multipyer)
    number//=8
    multipyer*=10

print(ocatal)


