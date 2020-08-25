
# list comprehensions to create list

list = [x*x for x in range(1,11)]

list=[]
for x in range(1,11):
    list.append(x*x)

list = [x*x for x in range(1,11) if x%2 ==0 ]

list = [ m+n for m in 'ABC' for n in 'XYZ']

L = ['Hello', 'World', 18, 'Apple', None]
list = [ s.lower() for s in L if isinstance(s, str) ]

print(list)

f