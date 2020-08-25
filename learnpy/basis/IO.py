import logging

#FileIO
try:
	f = open('D:\\test.txt', 'r', encoding ='gbk', errors='ignore')  #'rb'
except FileNotFoundError as e:
	logging.error(e)  #.debug .info .warning .error
else:
	f.read()
	f.close()
finally:
	pass

with open('D:\\test.txt', 'r') as f:
	#f.read(1024)
	#f.read()
	for line in f.readlines():
		print(line.strip()) # 去掉末尾的'\n'

with open('D:\\test.txt', 'w') as f: #'wb' 'w+'(追加写)
	f.write('Hello, world!\n')
	f.writelines(['hihi\n','name\n'])

#StringIO
from io import StringIO
f = StringIO()
f.write('hello')   # 返回5
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
	s = f.readline()
	if s =='':
		break
	print(s.strip())

#BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 返回6
print(f.getvalue())

f= BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()

#file and dictories
import os

os.name #ns(windows)
os.environ
os.environ.get('PATH')

print(os.path.abspath('.')) #D:\pydj\learnpy\basis
print(os.path.join('D:\\', 'test.txt')) #D:\test.txt
if(not os.path.exists('D:\\May')):
	os.mkdir('D:\\May')
os.rmdir('D:\\May')

os.path.split("D:\\test.txt")      #('D:\\', 'test.txt')
os.path.splitext("D:\\test.txt")   #('D:\\test', '.txt')

#os.rename('test.txt', 'test.py')
#os.remove('test.py')

print([x for x in os.listdir('.') if os.path.isfile(x)]) #os.path.isdir(x)

#picking unpicking 把变量从内存中变成可存储或传输的过程称之为序列化
import pickle

d = dict(name='Bob', age =20, score =88)
pickle.dumps(d) #把任意对象序列化成一个bytes
#Or
f = open('D:\\test.txt', 'w')
pickle.dump(d,f)
f.close()

with open('D:\\test.txt', 'rb') as f:
	print(d = pickle.load(f))

