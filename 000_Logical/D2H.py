number = 458
hexa = ""

while number !=0:
    k=""
    rem = number%16
    if rem >=10:
        rem+=55
        k = "A"
    else :
        k=rem
    hexa = str(k)+hexa
    number//=16
  

print(hexa)


