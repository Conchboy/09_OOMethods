class A:
    def test(self):
        print("这是爸爸 test方法")


class B:
    def demo(self):
        print("这是妈妈 demo方法")


class C(A, B):
    """多继承可以让子类对象,同时具有多个父类的特点"""
    def test3(self):
        self.test()
        self.demo()


cat = C()

cat.test()
cat.demo()

