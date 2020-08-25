#函数名其实就是指向函数的变量
f =abs
f(-10)

#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x,y,f):
	return f(x) + f(y)

print(add(-5, 6, abs))

def f(x):
	return x*x
r = map(f, [1,2,3,4,5,6,7,8,9])   #map(function, IIterable) 返回iterator 
print(list(r))

from functools import reduce
def fn(x,y):
	return x*10 +y

print(reduce(fn, [1,3,5,7,9]))  # reduce(function,iterable) 结果继续和序列下一个元素做累计运算

#模拟 int()
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
	return reduce(lambda x,y: x*10+y, map(char2num, s))
print(str2int('13579'))


def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key= lambda t: t[0], reverse = False)  #sorted(object, key=function, reverse=) 返回List
print(L2)