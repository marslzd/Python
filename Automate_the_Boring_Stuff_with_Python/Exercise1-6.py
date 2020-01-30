# 课后实践项目1-6
######### 习题1.8 ###########
bacon = 20
bacon + 1
print(bacon)  # 20

print('spam'+'spamspam')
print('spam' * 3)

######### 习题2.11 ##########
spam = 6
if spam == 1 :
    print("Hello")
elif spam == 2 :
    print("howdy")
else:
    print("Greetings! ")


spam = True
print(spam)

############### 习题3.11.1 Collatz序列 ############
def collatz(number):
    """
    collatz 序列
    """
    if number >= 0:
        if number % 2 == 0:  # number is 偶数
            print(number // 2)
            return number // 2
        if number % 2 == 1:  # number is 奇数
            print(number*3 + 1)
            return number*3 + 1
    else:
        print("The number is not a ZHENGSHU")

print("Please Enter a number : ")
while True:
    User_input = input()
    try:
        User_input = int(User_input)
        collatz(User_input)
    except ValueError:
        print("You must input a 整数")
        break

########### 习题4.10.1 逗号代码 ###############
spam = ['apples', 'bananas', 'tofu', 'cats']

def List_process(spam):
    """
    将list处理成字符串
    """
    for i in range(len(spam)):
        if i == (len(spam) - 1):
            print('and ' + spam[i])
            break
        print(spam[i] + ', ' , end='')

spam = ['A', 'B', 'C', 'D']
List_process(spam)

############## 习题4.10.2 字符图网格 ############

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(len(grid))
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('\n', end='')

################## 习题5.6.1 好玩游戏的物品清单 ###########################

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(player):
    """
    清单建模的数据结构，keys为字符串，描述清单中物品；
    values为整数，描述物品的数量
    """
    print('Inventory:')
    total_num = 0
    for i in player.keys():
        print(' ' + str(player[i]) +  ' ' +i )
        total_num = total_num + player[i]

    print('total number of items:' + str(total_num))

displayInventory(stuff)

############# 习题5.6.2 list to tuple #################################
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def displayInventory(player):
    """
    清单建模的数据结构，keys为字符串，描述清单中物品；
    values为整数，描述物品的数量
    """
    print('Inventory:')
    total_num = 0
    for i in player.keys():
        print(' ' + str(player[i]) +  ' ' +i )
        total_num = total_num + player[i]

    print('total number of items:' + str(total_num))

def addToInventory(inventory, addItems):
    """
    参数inventory为字典，addItems为列表，
    将列表添加到字典中，更新字典
    """
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
    """
    通过利用tuple性质优化了上面的代码，
    与上述代码功能一样：
    参数inventory为字典，addItems为列表，
    将列表添加到字典中，更新字典
    """
    for i in range(len(addItems)):
        print(addItems[i])
        inventory.setdefault(addItems[i], 0)  # 判断list中的值与tuple的keys
        inventory[addItems[i]] += 1           # upadat conunt 
    
    return inventory

inv = addToInventory(inv, dragonLoot)
# print(inv)
displayInventory(inv)


################## 习题6.7表格打印 #################################
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    """
    该函数接受字符串的列表的列表，打印在表格中(右对齐)
    """
    colwidths = [0] * len(tableData)
    col = len(tableData)             # 列数
    raw = [0] * len(tableData)       # 行数
    
    # 寻找每个内层列表中最长字符串
    for i in range(len(tableData)):
        raw[i] = len(tableData[i])
        a = [0] * len(tableData[i])
        for j in range(len(tableData[i])):
            a[j] = len(tableData[i][j])
        a.sort(reverse=True)        # 将每个内层列表的字符串长度从大到小排列
        # print(a)
        colwidths[i] = a[0]         # 将每个内层列表的字符串的最大值赋给列宽
    # print(colwidths)
    raw.sort()
    raw_max = raw[-1]
    # print(raw)
    # print(raw[-1])

    # 打印表格
    for j in range(raw_max):
        for i in range(col):
            print(tableData[i][j].rjust(colwidths[i]) + ' ', end='')
        print('\n', end='')

def main():
    """
    main函数：执行操作
    """
    printTable(tableData)

if __name__ == '__main__':
    main()
