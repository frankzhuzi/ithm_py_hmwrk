def input_pswd():

    pwd = input("Enter your password: ")

    if len(pwd) >= 8:
        return pwd

    print("Error")

    ex = Exception("Length not enough")

    raise ex

try:
    print(input_pswd())
except Exception as result:
    print(result)
    