#picking unpicking 把变量从内存中变成可存储或传输的过程称之为序列化
#pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。
import pickle
f = open('D:\\test.txt', 'wb')

d = dict(name='Bob', age =20, score =88)
_bytes = pickle.dumps(d) #把任意对象序列化成一个bytes
f.write(_bytes)
#Or
pickle.dump(d,f)  # 包括write()

f.close()

with open('D:\\test.txt', 'rb') as f:
	print(pickle.load(f))


#JSON
import json
d = dict(name='Bob', age =20, score =88)
_str = json.dumps(d)    # 序列化成string
print(_str)

_dict = json.loads(_str)
print(_dict)

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {
		'name' : std.name,
		'age': std.age,
		'score': std.score
	}

s = Student('Bob', 20, 88)
print(json.dumps(s, default = student2dict))
json_str = json.dumps(s, default = lambda object: object.__dict__)

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook = dict2student))