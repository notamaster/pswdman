# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""
import pswddb
import config

def main():
    x = pswddb.PswdDB(config.DATABASENAME)
    print('*'*40,'*'*5+' ————NB的程序正在运行！！———— '+'*'*6,'*'*40,sep='\n')
    x.main()
    print('*'*40,'*'*5+' ————NB的程序即将停止！！———— '+'*'*6,'*'*40,sep='\n')
	

if __name__ == "__main__":
    main()
    input("查询结束，数据库已关闭！！")
    
'''
def addPswd(self,index=0):
    #向数据库中添加数据
        inDict = {}    
        for i in config.BTLIST[1:]:
            inDict[i] = input('请输入'+i) 
        if index != 0:
            tmp = index 
        else:
            if self.dList :
                tmp = self.dList.pop(list(self.dList.keys())[0])
            else:
                tmp = str(len(self.db))
        inDict['索引号：'] = tmp
        self.db[tmp] = pswd.Pswd(inDict)
        return
    
    def searchPswd(self):
        #在数据控中查找数据
        cnt = 0
        keyword = input("input keywords :").split()
        try:
            if len(keyword) <= 1 :
                for i in self.db:
                    if keyword[0] in self.db[i].indexStr :
                        print(self.db[i])
                        cnt += 1
            elif keyword[1] == "-a":
                for i in self.db:
                    if keyword[0] in self.db[i].allStr :
                        print(self.db[i])
                        cnt += 1
        except:
            print("关键词错误！！！")
        return cnt
'''