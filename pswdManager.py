# -*- coding: utf-8 -*-
"""
NB的程序 密码管理神器

@author: notagod
"""
import pswd

if __name__ == "__main__":
	DATABASE = "shadow"
	x = pswd.PswdDB(DATABASE)
	print('*'*40,'*'*5+' ————NB的程序正在运行！！———— '+'*'*6,'*'*40,sep='\n')
	x.main()        
	print('*'*40,'*'*5+' ————NB的程序即将停止！！———— '+'*'*6,'*'*40,sep='\n')
	input("查询结束，数据库已关闭！！")