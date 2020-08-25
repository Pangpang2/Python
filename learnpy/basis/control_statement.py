
height = 1.75
weight = 80.5

BMI = weight / (height * height)

if BMI < 18.5:
	print("below light")
elif BMI <=18.5 and BMI >= 25:
	print("normal")
else:
	print("fat")


L = ['Bart', 'Lisa', 'Adam']

for x in range(len(L)):
	print(L[x])

for x in L:
	print(x)

n = len(L) - 1
while n >= 0:
	print(L[n])
	n -=1