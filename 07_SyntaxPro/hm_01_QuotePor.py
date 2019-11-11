

def test(num):

    print("inner function %d stays in address %d" % (num, id(num)))


a = 10
print("variable a's address is %d" % id(a))

test(a)