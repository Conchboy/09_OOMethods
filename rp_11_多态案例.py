class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳地玩耍" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 神一样地飞着玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, cat):
        print("%s 和 %s 快乐滴玩耍" %
              (self.name, cat.name))

        # 让狗玩耍
        cat.game()


# 1. 创建一个狗对象
# wangcai= Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3.让小明和旺财玩
xiaoming.game_with_dog(wangcai)
