try:
    num = int(input("Enter an int"))
    result = 8 / num

    print("-" * 30)

    print(result)
except ZeroDivisionError:
    print("'0'is illegal")
except ValueError:
    print("Not a string please!")

