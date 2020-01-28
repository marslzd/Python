# 字典 key:value
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur. ')

spam = {12345: 'Luggage Combination', 42: 'The Answer'}

spam = ['cats', 'dogs', 'mouse']
bacon = ['dogs', 'mouse', 'cats']
print(spam == bacon)

eggs = {'name':'Zophine', 'species':'cat', 'age':'8'}
ham = {'species':'cat', 'age':'8', 'name':'Zophine'}
print(eggs == ham)

spam = {'name': 'Zophine','age':7}
spam['color'] = 'grey'
print(spam)

# birthday
birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday ?')
        bday = input
        birthdays[name] = bday
        print('Birthdays database updated')

spam = {'color':'red', 'age':42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

# 检查字典中是否存在key或value
spam = {'name':'Zophie', 'age':5}
print('name' in spam.keys())
print(7 in spam.values())

# get()
picnicItems = {'apples':5, 'cups':2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# setdefault()
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)

spam.setdefault('color', 'white')
print(spam)

# characterCount
message = 'It was a bright cold day in April, and the locks were striking thirteen. '
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

# beautiful print => pprint
import pprint
pprint.pprint(count)

print('######################\n')
# 使用数据结构对真实世界建模
# 井字键盘
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)
print('\n')

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
printBoard(theBoard)
print(theBoard.keys())

# 允许玩家输入他们的玩法
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     print("choose('top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R')")
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# 嵌套字典和lsit
allGuests = {'Alice': {'apple':5, 'pretzels':12 },
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups':12, 'apple pies': 1}
             }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought : ')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple pies ' + str(totalBrought(allGuests, 'apple pies')))

# 习题5.6.1 好玩游戏的物品清单

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(player):
    print('Inventory:')
    total_num = 0
    for i in player.keys():
        print(' ' + str(player[i]) +  ' ' +i )
        total_num = total_num + player[i]

    print('total number of items:' + str(total_num))

displayInventory(stuff)

# 习题5.6.2 list to tuple 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def displayInventory(player):
    print('Inventory:')
    total_num = 0
    for i in player.keys():
        print(' ' + str(player[i]) +  ' ' +i )
        total_num = total_num + player[i]

    print('total number of items:' + str(total_num))

def addToInventory(inventory, addItems):
    for i in range(len(addItems)):
        print(addItems[i])
        if addItems[i] in inventory.keys():   # 判断list中的值与tuple的keys
            print('In keys',addItems[i])
            inventory[addItems[i]] += 1       # upadat conunt 
        else:
            inventory[addItems[i]] = 1
    
    return inventory

## 采用tuple性质优化代码
def addToInventory(inventory, addItems):

    for i in range(len(addItems)):
        print(addItems[i])
        inventory.setdefault(addItems[i], 0)  # 判断list中的值与tuple的keys
        inventory[addItems[i]] += 1           # upadat conunt 
    
    return inventory

inv = addToInventory(inv, dragonLoot)
# print(inv)
displayInventory(inv)