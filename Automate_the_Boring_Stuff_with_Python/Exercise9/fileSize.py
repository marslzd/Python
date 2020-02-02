import os

# print(os.path.getsize('/home/linux/Desktop/Test/1.pdf'))

FilePath = '/home/linux/Desktop/Test'
# 遍历目录树and Copy file 
for foldername, subfolders, filenames in os.walk(FilePath):
    for filename in filenames:
        # print(foldername + '/' +filename)
        print('The size of file %s : ' % (foldername + '/' +filename), end='')
        print(os.path.getsize(foldername + '/' +filename))