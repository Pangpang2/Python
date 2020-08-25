#--*encoding:utf-8*--
d = {'Michael':95, 'Bob':75, 'Tracy':'98'}

d['Michael'] = 100
d['Lucy'] = 70
# d.pop('Bob')
del d['Lucy']

d.update({'NewInset': 1,
		  'Michael': 17})

if 'Bob' in d:
	print('--------------')
	print('Bob:' ,d['Bob'])

if d.get('Lucy') == None:
	print('Lucy \'s score is not found')
else:
	print('Lucy:', d['Lucy'])

if d.get('Lily', -1) == -1:
	print('Lily \'s score is not found')

# 遍历
for i in d:  #  等同于 for i in d.keys()
	print('d[%s]='%i, d[i])

for key in d.keys():
	print(key);

for value in d.values():
	print(value);

for (key,value) in d.items():
	print('{0}:{1}'.format(key,value))


#set和dict的唯一区别仅在于没有存储对应的value
s1 = set([1,2,3,4])
s1.add(4)   # s1 ={1,2,3,4} 不含重复值
s2 = set([2,3])
print(s1&s2)
print(s1|s2)