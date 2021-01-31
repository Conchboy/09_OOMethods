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
    # 如果在子类中, 重写了父类中定义的方法
    # 在使用子类对象调用的方法, 就会使用子类中重写的方法
    def bark(self):
        print("嘤嘤嘤")


xtq = XiaoTianQuan()
xtq.bark()
