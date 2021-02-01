class Tool(object):

    # 使用赋值语句定义类属性,记录所有工具对象的数量
    count = 0
    list = []

    def __init__(self, name):
        self.name = name

        # 让属性的值+1; 记录和类相关的特征
        Tool.count += 1
        list.append(name)


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
tool4 = Tool("类属性")

# 2. 输出工具对象的总数
print("工具对象总数 %d" % tool1.count)
print(tool2.list)
