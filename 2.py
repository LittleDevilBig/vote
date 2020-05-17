#coding=utf-8
import  xml.dom.minidom
import numpy as np
import os
import glob
g=0
h=0
y=np.zeros(7)
n=np.zeros(7)
m = np.zeros((5000, 8), dtype=np.object)
m = np.loadtxt("text.txt", delimiter=',',dtype=np.object)
source = ['jc', 'c5', 'sy', 'xg', 'qh', 'nc', 'ok']
path = 'D:/nk/文字/dtxml/2007' #文件夹目录

f = glob.glob(path + '/*.dtxml' )
for file in f :
    dom = xml.dom.minidom.parse(file)
    root = dom.documentElement
    a = root.getElementsByTagName(source[6])
    for i in range(len(a)):
        if a[i].firstChild==None: continue
        for j in range(6):
            x = dom.getElementsByTagName(source[j])
            for k in range(3900):
                if m[k][0]==x[i].firstChild.data:
                    y[j]=float(m[k][j+1])/float(m[k][7])
                    n[j]=k
                    break
                else: y[j]=0
        list_y = y.tolist()
        if max(list_y)==0: continue
        max_index = list_y.index(max(list_y))
        if m[int(n[max_index])][0]==a[i].firstChild.data:
            g=g+1
        h=h+1
        print(g / h)
print(g/h)

