#coding = utf-8

#classical - 装饰器
class Person:
	def __init__(self):
		self.first_name = 'Mike'
		self.last_name = 'Driscoll'

	@property
	def full_name(self):
		return '%s %s'%(self.first_name,self.last_name)

obj = Person()
print(obj.full_name)

#new-style - 装饰器
class Goods1(object):
	def __init__(self):
		self.original_price = 100
		self.discount = 0.8

	@property
	def price(self):
		new_price = self.original_price * self.discount
		return new_price
	
	@price.setter
	def price(self, value):
		self.original_price = value

	@price.deleter
	def price(self):
		del self.original_price

obj = Goods1()
obj.price
obj.price = 90
del obj.price

#new-style/classical - 静态字段
class Goods2(object):
	def __init__(self):
		self.original_price = 100
		self.discount = 0.8

	def get_price(self):
		new_price = self.original_price * self.discount
		return new_price

	def set_price(self, value):
		self.original_price = value

	def del_price(self):
		del self.original_price

	PRICE = property(get_price,set_price,del_price,"description: good price")

obj = Goods2()
obj.PRICE
obj.PRICE = 90
#del obj.PRICE
#print(obj.PRICE.__doc__) 