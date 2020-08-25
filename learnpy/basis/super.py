
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")
 
class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")
 
class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")
 
class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")

#super 和父类没有实质性的关联
#python 会计算出一个方法解析顺序（Method Resolution Order MRO）
#super 原理
#def super(cls, inst):
#   mro = inst.__class__.mro()    #获取instance 类的MRO列表
#   return mro[mro.index(cls) +1] #获取MRO列表的下一个类
c = C()
print(C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]



class D(object):
    pass
 
class E(object):
    pass
 
class F(object):
    pass
 
class C(D, F):
    pass
 
class B(E, D):
    pass
 
class A(B, C):
    pass

print(A.mro())
#[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]

#MRO算法 ： 对有向无环图进行排序： 拓扑排序， 
#1.从左到右依次查找入度为0的结点，输出结点
#2.减掉结点相关边，执行步骤1
#MRO 算法解决经典继承方式查找方式（深度优先）的缺点,保证所有的子类都能重写