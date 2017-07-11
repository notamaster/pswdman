# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""

BTLIST =['索引号：','名称：', '分类：', '账号：','密码：', '用户名：', '绑定信息：','备注：']

class Pswd:
    '''
    存储密码的数据结构
    '''
    def __init__(self,inDict):
        self.dataDict = inDict
        self.name = self.dataDict["名称："]
        self.index = self.dataDict['索引号：']
        self.indexStr = self.dataDict['索引号：'] + " : " + self.dataDict['名称：']
        self.allStr = ""        
        for i in BTLIST:
            self.allStr += self.dataDict[i]
        return
    def __str__(self):
        for i in BTLIST:
            print(i+self.dataDict[i])
        return  "_"*40


