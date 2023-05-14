import os
'''
读取文件夹下所有文件的名字并把他们用列表存起来
'''
path = "E:\\0\dataset"
datanames = os.listdir(path)
list = []
for i in datanames:
    list.append(i)
print(list)
