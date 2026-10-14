def function1():
    try:
        l = [1, 5, 6, 7, 6, 4]
        i = int(input("Enter the Index: "))
        print(l[i])
        return 1
    except:
        print("Some error Occurred!")
        return 0
    finally:
        print("I am always executed, regardless of Errors.")


x = function1()
print(x)
