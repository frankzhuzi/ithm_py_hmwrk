
num = 10


def demo1():

    global num  # invoke global "num" directly
    num = 99
    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()
