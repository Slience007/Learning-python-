#coding:utf-8
#创建类
__metaclass__ = type

class Human:
    #初始化函数
    def __init__(self,name):
        self.name =name
        print(self)
        print(type(self))
    def getName(self):
        return self.name
    def color(self,color):
        print(" %s is %s"  %(self.name,color) )
gril = Human("Stephen")
gril.color("Black")
