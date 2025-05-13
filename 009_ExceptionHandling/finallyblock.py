
def test():
    try : 
        a = int(input("enter number : "))
        print(a)
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("print something after executon")

k = test()
print(k)