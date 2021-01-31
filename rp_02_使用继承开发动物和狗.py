# 继承语法
# class 子类(父类)
#       pass
# 术语: 子类,父类 子类从父类中继承 = 派生类, 基类, 派生类从基类中派生
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


# 创建对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()



