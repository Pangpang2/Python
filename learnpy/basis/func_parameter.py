abs(-20) # 绝对值
max(1,2,6,9)
int('123')
float("12.34")
str(1.23)
bool(1) # True
'AC'.lower()

#起别名
 #a = abs
 #a(-1)

hex(1)  # 十进制转十六进制

#1、位置参数
def power(x,n):
	s =1 
	while n>0:
		s = s*x
		n = n-1
	return s

#2、默认参数(必须在后,可无顺序，必须指向不变对象)
def power(x, n=2, m =4):
	pass 

power(5)
power(5,3)
power(5, m=4)
print(power(5,m =4,n=3))


#默认参数必须指向不变对象，否则(函数在定义时，默认值已经被计算出来)
def add_end(L =[]):
	L.append('End')
	print(L)

add_end()  # ['End']
add_end()  #['End', 'End']


#3、可变参数( 封装成tuple)
def calc(*args):
	sum = 0
	for n in args:
		sum = sum + n*n
	return sum
calc()
calc(1,2)
nums = [1,2,3]
calc(*nums)

#4、关键字参数(封装成dict)
def person(name, age , **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing', addr ='Chaoyang')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24 ,**extra)

#5、命名关键字参数(限制关键字参数名字,必须传入参数名)
def person(name, age, *, city, job):
	print(name,age,city,job)

person('Jack', 24, city='Beijing', job = 'Engineer')

def person(name, age, *args, city, job):  # 有可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
	pass


#参数顺序： 必选参数 默认参数 可变参数 命名关键字参数 关键字参数