#--*encoding:utf-8*--

classmates = ['Michael', 'Bob', 'Tracy', 25]
len(classmates)
# index 超出会越界
classmates[0]   
classmates[-1]

classmates.append('Adma')
classmates.insert(1, 'Jack')

classmates.pop()
classmates.pop(1)

for name in classmates:
	print('------------------')
	print(name)

if 'Bob' in classmates:
	print('Bob is my classmate')

if 'Lucy' not in classmates:
	print('Lucy is not my classmate')

classmates[0:2]   #[0,2)
classmates[-2:]

L = list(range(100))  #0-99
L[:10]
L[-10:]
L[:10:2]
L[:]
L[0:1000]  # 可越界
'ABCD'[:3]
L.reverse()


for i ,value in enumerate(classmates):
	print(i, value)

t = ('Michael', 'Bob', 'Tracy', 25)
t = ()
t = (1,)