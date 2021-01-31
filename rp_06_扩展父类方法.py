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
        # 1. 针对子类特有的需求, 编写代码
        print("神一样的叫唤...")
        # 2. 使用super().调用原本在父类中封装的方法
        # super().bark()
        # 父类名.方法(self)
        Dog.bark(self)
        # 注意: 如果使用子类调用方法, 会出现递归调用 --"死循环"
        # XiaoTianQuan.bark(self)
        # 3. 增加其他子类的代码
        print("&*#%*%(@*!@#($*")


xtq = XiaoTianQuan()
xtq.bark()
