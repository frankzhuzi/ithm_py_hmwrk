try:
    num = int(input("Enter an int"))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("'0'is illegal")
except Exception as result:
    print("Unknown Error %s" % result)
else:
    print("Success!")
finally:
    print("-" * 50)