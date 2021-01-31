class Animal:
    def eat(self):
        print("eat___")

    def drink(self):
        print("drink~~~")

    def run(self):
        print("run***")

    def sleep(self):
        print("睡zzz")


class Dog(Animal):
    # 子类可以继承父类的所有属性和方法
    # def eat(self):
    #     print("eat")
    #
    # def drink(self):
    #     print("drink")
    #
    # def run(self):
    #     print("run")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪汪")


class XiaoTianQuan(Dog):

    def fly(self):
        print("傻了吧, 爷可以飞")

class Cat:

    def catch_mouse(self):
        print("抓老鼠, 哇咔咔")

# 创建对象
wangcai = Dog()
xtq = XiaoTianQuan()


xtq.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
xtq.fly()
xtq.bark()
# 不能调用不在直线父类中的方法
# xtq.catch_mouse()




