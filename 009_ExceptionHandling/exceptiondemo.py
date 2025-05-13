

print("Program started...")

try :
    a = 10
    b = a/1
    print(b)
except Exception as e:
    # print(e)
    pass
else:
    print("No errors")
finally:
    print("Execute final block..")


print("program ended")