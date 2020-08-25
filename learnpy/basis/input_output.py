print("The quick brown fox", "jumps over", "the lazy dog")


#name = input("please enter your name:")
#print("Hello, %s" %name)

print("His name is %s" % ("Aviad"))
print("His age is %d"  % 25)
print("His height is %f m" %(1.83))
print("His height is %.2f m" % (1.83))
print("Name :%10s Age:%8d Height:%8.2f" % ("Aviad", 25, 1.83))
print("Name :%-10s Age:%-8d Height:%-8.2f" % ("Aviad", 25, 1.83))
print("%4d-%02d-%02d" %(2017, 7, 23))

print("Name:{0} Age:{1} Height:{2:.3} ".format("Avaid", 25 , 1.831))
#< 左对齐（默认） > 右对齐  ^ 中间对齐
print("Name:{0:<10} Age:{1:^10} Height:{2:>.3} ".format("Avaid", 25 , 1.831))


print(format(0.0015, '.2e'))
print(format(0.05152, '.2%'))

user_name='Tutu'
user_age=30
print("This is {name}, age: {age}".format(name=user_name, age=user_age ))