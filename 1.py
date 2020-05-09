#coding=utf-8
import  xml.dom.minidom
import numpy as np
import os
import glob
g=0
m = np.zeros((5000, 8), dtype=np.object)
d = {"a": -1}
source = ['jc', 'c5', 'sy', 'xg', 'qh', 'nc', 'ok']
path = 'D:/nk/文字/dtxml/2003' #文件夹目录

f = glob.glob(path + '/*.dtxml' )
for file in f :
    dom = xml.dom.minidom.parse(file)
    root = dom.documentElement
    a = root.getElementsByTagName(source[6])
    for i in range(len(a)):
        if a[i].firstChild==None: continue
        if a[i].firstChild.data not in d:
            m[g][0] = a[i].firstChild.data
            d[m[g][0]] = g
            g = g + 1
        for j in range(7):
            x = dom.getElementsByTagName(source[j])
            if x[i].firstChild.data == a[i].firstChild.data:
                m[d[a[i].firstChild.data]][j + 1] = m[d[a[i].firstChild.data]][j + 1] + 1
    np.savetxt("text.txt", m,fmt="%s",delimiter=",")
    #b = np.loadtxt("filename.txt", delimiter=',')

np.savetxt("ans.txt", m,fmt="%s",delimiter=",")







