#--*encoding:utf-8*--
import os
print(os.getcwd())
print(os.urandom(2)) #随机字符串，可以用作加密key


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

#and-or

a='first'
b='second'
print('bool is true:%s'%(1 and a or b))#true
print('bool is false:%s'%(0 and a or b))#second

a=''
print('a is false:%s'%(1 and a or b)) #second