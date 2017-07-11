# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""
import config

class Pswd:
    '''
    存储密码的数据结构
    '''
    def __init__(self,inDict):
        self.dataDict = inDict
        self.name = self.dataDict["名称："]
        self.index = self.dataDict['索引号：']  # auto allocate !!
        self.indexStr = self.dataDict['索引号：'] + " : " + self.dataDict['名称：']
        self.allStr = ""        
        for i in config.BTLIST:
            self.allStr += self.dataDict[i]
        return
    def __str__(self):
        for i in config.BTLIST:
            print(i+self.dataDict[i])
        return  "_"*40


