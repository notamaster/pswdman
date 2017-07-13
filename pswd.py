# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""

class Pswd:
    '''
    存储密码的数据结构
    '''
    def __init__(self,index,xin):
        '''
        init Pswd class , xin must be a specail dict ,index must be a string
        '''
        self.dataDict = xin
        self.name = self.dataDict["名称："]
        self.index = index
        self.indexStr = index + " : " + self.dataDict['名称：']
        self.allStr = index        
        for i in self.dataDict:
            self.allStr += self.dataDict[i]
        return
    def __str__(self):
        '''
        print the password
        '''
        print("索引号： -> "+self.index)
        for i in self.dataDict:
            print(i,self.dataDict[i],sep=" -> ")
        return  "_"*40

if __name__ == "__main__":
    '''
    This code is noly for test !!
    '''
    help(Pswd)