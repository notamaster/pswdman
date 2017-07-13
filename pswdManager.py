# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""
import pswddb
import config

def pswdManager(db_name=config.DATABASENAME):
    '''
    密码管理器主控制方法
    '''
    x = pswddb.PswdDB(db_name)
    print("当前数据库大小 : " + str(len(x.db)) )
    while 1:
        print("_"*40)
        op = input("请输入操作码 : ")
        op = op.lower()
        if op == "q":
            break
        elif op == "a":
            xin = sp_input()
            x.append(xin)
            print("添加成功！！")
        elif op == "s":
            x.showStatus()
        elif op == "ls":
            x.showDataList()
        elif op.lower() == "m":
            x.showDataList()
            index = input("输入要修改数据的索引号 ：")
            if index not in x.db:
                print("未找到数据！！！")
            xin = sp_input()
            if x.modifyData(index,xin):
                print("修改成功！！！")
            else:
                print("error 233 ")
        elif op.lower() == "d":
            x.showDataList()
            index = input("输入要删除的数据（谨慎操作！！） ：")
            if x.deletData(index):
                print("数据已删除！！！")
            else:
                print("未找到数据！！！")
        elif op == "":
            keyword = input("keyword: ")
            tmp = str(x.select(keyword))
            print("查询完成！找到数据共计 "+tmp+" 条！！！")
        elif op == "as":
            keyword = input("keyword: ")
            tmp = str(x.select(keyword,1))
            print("查询完成！找到数据共计 "+tmp+" 条！！！")
        elif op == "root":
            root = input("启用root权限？？？")
            if root.lower() =="y":
                root(x)
        else:
            print("操作码错误！！按Q键退出！！")
    x.close()

def sp_input():
    '''
    输入字典生成器
    '''
    xin = {}
    for i in config.BTLIST:
        xin[i] = input(i)
    return xin
    
def root(x):
    '''
    root 管理器
    '''
    root_op = input("请输入root秘语： ")
    if root_op == "import":
        pass
    elif root_op == "export":
        pass
    else:
        print("你对root一无所知！！！")
    return


if __name__ == "__main__":
    print('*'*40,'*'*5+' ————NB的程序正在运行！！———— '+'*'*6,'*'*40,sep='\n')
    pswdManager()
    print('*'*40,'*'*5+' ————NB的程序即将停止！！———— '+'*'*6,'*'*40,sep='\n')
    input("查询结束，数据库已关闭！！")
