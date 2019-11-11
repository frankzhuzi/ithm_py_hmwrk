class A:

    def test(self):
        print("A")


class B:

    def demo(self):
        print("B")


class C(A, B):

    pass


celar = C()
celar.demo()
celar.test()

