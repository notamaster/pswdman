# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""
import shelve
import pswd

class PswdDB:
    '''
    密码数据库，支持增删改查导入导出
    '''
    def __init__(self,dbname):
        '''
        init pswddb class . In fact , it open two shelve databases
        '''
        self.db = shelve.open(dbname,"c")
        self.db_d = shelve.open(dbname+"_dl","c")
        if 'dlist' not in self.db_d :
            self.db_d['dlist'] = []
        self.d_list = self.db_d['dlist']
        return
        
    def append(self,xin):
        '''
        向数据库中添加数据，并自动生成索引号，xin为输入字典
        '''
        if not self.d_list:
            index = str(len(self.db))
        else:
            index = self.d_list.pop()
        self.db[index] = pswd.Pswd(index,xin)
        return True
        
    def select(self,keyword,allsearch = 0):
        '''
        查找数据,返回找到的数据条数
        '''
        cnt = 0
        if allsearch == 0:
            for i in self.db:
                if keyword in self.db[i].indexStr :
                    print(self.db[i])
                    cnt += 1
        else:
            for i in self.db:
                if keyword[0] in self.db[i].allStr :
                    print(self.db[i])
                    cnt += 1
        return cnt
        
    def deletData(self,index):
        '''
        删除数据，输入索引
        '''
        if index in self.db:
            self.d_list.append(index)  #将索引添加至删除表中
            print(self.db.pop(index)) 
            return True
        else:
            return False
    
    def modifyData(self,index,xin):
        '''
        修改数据，输入索引和输入字典。本质是删除索引并用改索引建立新的Pswd对象
        '''
        if index in self.db:
            self.deletData(index)
            self.append(index,xin)
            return True
        else:
            return False
    
    def showStatus(self):
        '''
        show status of the database
        '''
        print("当前数据库大小 : " + str(len(self.db)) )
        print("回收站大小 : " + str(len(self.d_list)))
        #显示回收站中的索引号:
        #for i in self.dList:
        #    print(i,end =" ")
        print()
        return
    
    def showDataList(self):
        '''
        show data list
        '''
        print("_"*15+"DataList"+"_"*15)
        for i in self.db:
            print(i,self.db[i].name,sep=" -> ")
        print("_"*40)
        return
    
    def close(self):
        '''
        close database
        '''
        self.db.close()
        self.db_d.close()
        print("数据库已关闭 ！！！")
        
    def from_csv(path):
        '''
        
        '''
        import csv
        with open(path,'r') as f:
            x = csv.reader(f)
            for i in x:
                for j in i:
                    print(j,end = ' ')
                print("*")
                
    def to_csv(path):
        '''
        
        '''
        import csv
        with open(path,'r') as f:
            x = csv.reader(f)
            for i in x:
                for j in i:
                    print(j,end = ' ')
                print("*")
 
        
if __name__ == "__main__":
    '''
    test code
    '''
    help(PswdDB)