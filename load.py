# -*- coding: utf-8 -*-
"""
NB的程序 密码加载神器

@author: notagod
"""
#import csv
#import a01
PATH = r'G:\my_code\shadow'
#x = a01.PswdDB("shadow")
BTLIST =['名称：', '分类：', '账号:','用户名：', '密码：', '绑定信息：','备注：']

class tes():
    sut = 0
    def __init__(self):
        self.num = tes.sut
        tes.sut += 1
        
for i in range(5):
    x = tes()
    print(x.num)

'''
with open(PATH,'r') as f:
        x = csv.reader(f)
        for i in x:
            for j in i:
                print(j,end = ' ')
            print("*")
'''