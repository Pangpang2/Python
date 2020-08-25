import pickle

dict1 = {'a':100,
         'b':200,
         'c': 300}

list1 = [400,
         500,
         600]


print dict1
print list1

output = open("save1.pkl", 'wb')
pickle.dump(dict1, output)
pickle.dump(list1, output)

output.close()

print '-------'


input = open("save1.pkl", 'rb')
dict2 = pickle.load(input)
list2 = pickle.load(input)

input.close()

print dict2
print list2



class Player:
    def __init__(self, id, name, health, items):
        self.id = id
        self.name = name
        self.health = health
        self.items = items

    def __str__(self):
        return " My ID: " + str(self.id) + \
                "\n My Name: " + self.name + \
                "\n My Health: " + str(self.health) + \
                "\n My Items: " + str(self.items) + "."

items = ["axe", "sword", "gun"]
myObj = Player(1, "JACKs", 100.00, items)
print myObj

with open("save2.pkl", "wb") as outfile:
    pickle.dump(myObj, outfile)

print "---------------------------------"

newObj = None
with open("save2.pkl", 'rb') as infile:
    newObj = pickle.load(infile)

print newObj
