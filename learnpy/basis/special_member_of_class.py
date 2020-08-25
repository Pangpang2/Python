from property import Goods1

class Province(object):
	""" Description info: """
	country = 'China'

	def __init__(self, name, count): 
		self.name = name
		self.count = count

	#解释器在进行垃圾回收时自动触发
	def __del__(self):
		pass

	#对象() 或 类()()
	def __call__(self, *args, **kwargs):
		print('Province : %s %d'%(self.name, self.count))


print(Province.__doc__)

g = Goods1()
print(g.__module__)
print(g.__class__)

#__call__
Province('HeNan', 25000)()
p = Province('HeBei', 10000)
p()

print(Province.__dict__)