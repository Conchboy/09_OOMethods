class Tool(object):

    # 使用赋值语句定义类属性,记录所有工具对象的数量
    count = 0
    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        """

        :type name: object
        """
        self.name = name

        # 让属性的值+1; 记录和类相关的特征
        Tool.count += 1


# 创建工具对象
tool1 = Tool("飞机")
tool2 = Tool("大炮")
tool3 = Tool("航母")

# 调用工具数量显示方法
Tool.show_tool_count()
