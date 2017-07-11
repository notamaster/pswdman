# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""

class PswdDB:
    '''
    密码数据库，支持增删改查
    '''
    def __init__(self,dbname):
        import shelve
        self.db = shelve.open(dbname,"c")
        self.dList = shelve.open("dlist","c")
        #self.startSize = len(self.db)
        return
    '''  # 做成迭代器 #
    def showAllData(self):
        for i in self.db.keys():
            print(self.db[i])
        return
    def exportData(self,path):
        # 导出数据到csv #
        import csv
        csv.open(path)
        pass
    '''
    def addPswd(self,index=0):
    #向数据库中添加数据
        inDict = {}    
        for i in BTLIST[1:]:
            inDict[i] = input('请输入'+i) 
        if index != 0:
            tmp = index 
        else:
            if self.dList :
                tmp = self.dList.pop(list(self.dList.keys())[0])
            else:
                tmp = str(len(self.db))
        inDict['索引号：'] = tmp
        self.db[tmp] = Pswd(inDict)
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
    
    def showStatus(self):
        print("当前数据库大小 : " + str(len(self.db)) )
        print("回收站大小 :" + str(len(self.dList)))
        for i in self.dList:
            print(i,end =" ")
        print()
        return
    
    def showDataList(self):
        print("_"*15+"DataList"+"_"*15)
        for i in self.db.keys():
            print(i,self.db[i].name,sep=" -> ")
        print("_"*40)
        return
    
    def deletData(self,index):
        if index in self.db:
            self.dList[index] = index  #将索引添加至删除表中
            print(self.db.pop(index)) 
            return True
        else:
            return False
    
    def modifyData(self,index):
        if index in self.db:
            print(self.db[index])
            #self.deletData(name)
            self.addPswd(index)
            return True
        else:
            return False
    
    def main(self):
        #控制流方法
        print("当前数据库大小 : " + str(len(self.db)) )
        while 1:
            print("_"*40)
            op = input("请输入操作码 : ")
            if op.lower() == "q":
                break
            elif op.lower() == "a":
                self.addPswd()
                print("添加成功！！")
            elif op.lower() == "s":
                self.showStatus()
                self.showDataList()
            elif op.lower() == "m":
                self.showDataList()
                name = input("输入要修改的数据 ：")
                if self.modifyData(name):
                    print("修改成功！！！")
                else:
                    print("未找到数据！！！")
            elif op.lower() == "d":
                self.showDataList()
                name = input("输入要删除的数据（谨慎操作！！） ：")
                if self.deletData(name):
                    print("数据已删除！！！")
                else:
                    print("未找到数据！！！")
            elif op == "":
                tmp = str(self.searchPswd())
                print("查询完成！找到数据共计 "+tmp+" 条！！！")
            else:
                print("操作码错误！！按Q键退出！！")
        self.db.close()
        
        
if __name__ == "__main__":
    DATABASE = "shadow"
    x = PswdDB(DATABASE)
    print('*'*40,'*'*5+' ————NB的程序正在运行！！———— '+'*'*6,'*'*40,sep='\n')
    x.main()        
    print('*'*40,'*'*5+' ————NB的程序即将停止！！———— '+'*'*6,'*'*40,sep='\n')
    input("查询结束，数据库已关闭！！")