# 习题6.7表格打印
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colwidths = [0] * len(tableData)
    for i in range(len(tableData)):
        a = [0] * len(tableData[i])
        for j in range(len(tableData[i])):
            a[j] = len(tableData[i][j])
        a.sort(reverse=True)
        print(a)
        colwidths[i] = a[0]
    print(colwidths)
    
    for j in range(4):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colwidths[i]) + ' ', end='')
        print('\n', end='')

printTable(tableData)


# import numpy as np 
# print(np.max([1, 2]))