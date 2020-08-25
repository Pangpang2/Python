import math
from math import sqrt

#i = math.floor(32.9)
i = int(32.9)
i = sqrt(9)
i = "hello world"

print(i)

print(''' this
	is''')

print("Hello.\
	world !")

print(1+2+\
	4+5)
path = r'c:\abc'
print(path)

hu=['huhu',25]
chongshi = ['chongshi', 32]
database = [hu,chongshi]
print(database)


sentence = 'haha! this is my box'

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print(' '* left_margin + '+' + '-'*(box_width-2) + '+')
print(' '* left_margin + '|' + ' '*(box_width-2) + '|')
print(' '* left_margin + '|  ' + sentence + '  |')
print(' '* left_margin + '|' + ' '*(box_width-2) + '|')
print(' '* left_margin + '+' + '-'*(box_width-2) + '+')

