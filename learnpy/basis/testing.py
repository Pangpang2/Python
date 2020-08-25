#1. Random
import random
random.random() #0-1
random.uniform(1,10) # 1-10 (包括小数)
random.randint(1,10) # 1-10 整数
random.randrange(1,10,2)
lst =[1,2,3,4,5,6,7]
random.choice(lst)
random.sample(lst,2) #[]

#2. string reverse
a = 'abcdefg'
#（1）slice
a[::-1] 
#（2）list
t = list(a)
t.reverse()
print("".join(t))

#3. 判断回文
s ='abcdcba'  
if(s == s[::-1]):
	pass

#4. 随机生成100 个数，然后写入文件
import random
with open('1.txt', 'w') as f:  #1.txt 不存在，创建
	for i in range(1,101):
		n = random.randint(1,100)
		f.write(str(n)+'\n')

#5.给定字典排序
dic = {'a':3,'bc':5,'c':3,'asd':4,'33':56,'d':0}
L= sorted(dic.items(), key= lambda i:i[0])   #sorted(dic, key= lambda i:i[0]) 
print(L)

#6.列表去重
#（1）
a =[1,3,2,2,1,5,5,3]  
print(list(set(a)))  #[1, 2, 3, 5] 注意顺序
#(2)
t = dict.fromkeys(a,0) #{1: 0, 3: 0, 2: 0, 5: 0}
print(list(t))  # or t.keys()
#(3)
for i in a:
	if(a.count(i)) > 1:
		a.remove(i)
print(a)
#7. 去重字符串
s = 'abddaddfd'
list1 = set(s) #{'d', 'b', 'a', 'f'}   不固定
print(list1)
print('#7',''.join(list1)) #'dbaf'

l2 = {}.fromkeys(s).keys() #dict_keys(['a', 'b', 'd', 'f'])
print(list(l2)) #['a', 'b', 'd', 'f']
 

#8.输出
def extend_list(val, list=[]):  # 默认参数必须指向不可变对像（默认参数在函数定义时已经被计算出来）
    list.append(val)
    return list

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print(list1) # list1 = [10, 'a']
print(list2) # list2 = [123]
print(list3) # list3 = [10, 'a']

#9. 输出  
#类变量在内部是作为字典处理的,如果一个变量的名字没有在当前类的字典中发现，将搜索祖先类（比如父类）直到被引用的变量名被找到（如果这个被引用的变量名既没有在自己所在的类又没有在祖先类中找到，会引发一个 AttributeError 异常 ）。

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(dir(Parent))
print(dir(Child1))
print(dir(Child2))

print(Parent.x, Child1.x, Child2.x)  # [1,1,1]
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)  # [1,2,1]
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)  # [3,2,3]

#14.在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
#请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
arr = [[1,4,7,10,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]
def getNum(num, data=None):
	while data:
		if num > data[0][-1]:
			del data[0]
			print(data)
			getNum(num, data)
		elif num < data[0][-1]:
			data = list(zip(*data))
			del data[-1]
			data = list(zip(*data))
			getNum(num, data)
		else: 
			return True
			data.clear()
	return False

print(getNum(4, arr))

#15.获取最大公约数、最小公倍数
a = 36
b = 21
def maxCommon(a,b):
	while b:
		a,b = b, a%b
	return a
				
def minCommon(a,b):
	c = a*b
	while b:
		a,b = b, a%b
	return c//a

print(maxCommon(a,b))
print(minCommon(a,b))

#16. 单例模式
class Singleton(object):
	__instance = None  #_Singleton__instance
	def __init__(self):
		pass

	def __new__(cls, *args, **kwd):
		if Singleton.__instance is None:
			Singleton.__instance = super(Singleton, cls).__new__(cls, *args, **kwd)
		return Singleton.__instance

#17. 根据两个序列创建一个字典
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)

for i in range(1,10):
	print(i)

#18. 一列数的规则如下: 1、1、2、3、5、8..求第30位数是多少，用递归算法实现
def f(n):
 	if n==1 or n == 2:
 		return 1
 	return f(n-1) + f(n-2)

print(f(30))

#19. 冒泡排序

def bubble():
	list1 = [1,4,22,7,8,3,4,5,11]
	#for(i in range(0, len(list1)))

#20.
class A(object):
	def __init__(self):
		pass

	def instancefunc(self):
		pass

	@classmethod
	def classfunc(cls):
		pass

	@staticmethod
	def staticfunc():
		pass

a = A()
a.instancefunc()
A.instancefunc(a)

a.classfunc();
A.classfunc();

a.staticfunc();
a.staticfunc();