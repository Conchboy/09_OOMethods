class A:
    def test(self):
        print("这是爸爸 test方法---A")

    def demo(self):
        print("这是妈妈 demo方法---A")

class B:
    def demo(self):
        print("这是妈妈 demo方法---B")

    def test(self):
        print("这是爸爸 test方法---B")


class C(B, A):  # 在前的父类, 在有同名的方法时, 被优先调用
    """多继承可以让子类对象,同时具有多个父类的特点"""
    def test3(self):
        self.test()
        self.demo()


cat = C()

cat.test()
cat.demo()
cat.test3()

# 确定C类对象调用的方法的顺序, 从左往右
print(C.__mro__)
