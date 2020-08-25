# 动态创建类
class Foo(object):
	bar = True

def echo_bar(self):
	print(self.bar)

bar = 'coffe'
FooChild = type('FooChild', (Foo,), {'echo_bar':echo_bar})  #type(classname, (class,), {'funcname': func})
hasattr(Foo, 'echo_bar') #False
hasattr(FooChild, 'echo_bar') #True
my_foo = FooChild()
my_foo.echo_bar()
print(my_foo.__class__) #<class '__main__.FooChild'>
print(my_foo.__class__.__class__) #<class 'type'>

#python 中的类也是对象，元类就是用来创建类（对象）的
#元类的主要目的就是为了创建类时能够自动地改变类
class Bar(object):
	pass
class Foo(Bar):
	__metaclass__ = echo_bar
#Foo中有__metaclass__这个属性吗？
#如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
#如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
#如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
	#  选择所有不以'__'开头的属性
	attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
	uppercase_attr = dict((name.upper(), value) for name, value in attrs)

	return type(future_class_name, future_class_parents, uppercase_attr)

class Foo(object):
	__metaclass__ = upper_attr
	bar = 'bip'

print(hasattr(Foo, 'bar'))  #True
print(hasattr(Foo, 'BAR'))  #False

f = Foo()
print(f.BAR)