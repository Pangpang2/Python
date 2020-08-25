
''' generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。'''

g= (x*x for x in range(10))

#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print(g) #<generator object <genexpr> at 0x006F7DE0>
print(next(g))


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n+1
	return 'done'


f = fib(6)

for n in f:
	print(n)   

f=fib(6)
while True:
	try:
		x = next(f)
		print('f:', x)
	except StopIteration as e:
		print("Generator return value:", e.value)
		break
