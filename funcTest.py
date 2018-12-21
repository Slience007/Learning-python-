#coding:utf-8
def add_func(a,b):
    c =a + b
    print(c)
if __name__ =="__main__":
    add_func(2,3)
 #参数可变化
def add_nums(x,*rgs):
    print("First arg is: %s" %x)
    result = x
    print(rgs)
    for i in rgs:
        result = result + i
    print("Result is :%s" %result)

add_nums(0,1,3,5)

