class Dog:
    @staticmethod
    def run():
        # 如果定义的方法既不访问实例对象的属性,
        # 也不访问类属性,那么就应该被定义为静态方法

        print("小狗狗跑跑")


# 通过类名.方法 来调用静态方法不需要创建对象
Dog.run()


