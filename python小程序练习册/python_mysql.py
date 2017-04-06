#!/usr/bin/python
# coding: utf-8
import MySQLdb

#连接
cxn = MySQLdb.Connect(host = '172.29.205.93', user = 'root', passwd = '')
#游标
cur = cxn.cursor()

try:
    cur.execute("DROP DATABASE PyTest")
except Exception as e:
    print(e)
finally:
    pass

#创建数据库
cur.execute("CREATE DATABASE PyTest")
cur.execute("USE PyTest")

#创建表
cur.execute("CREATE TABLE users (id INT, name VARCHAR(8))")
#插入
cur.execute("INSERT INTO users VALUES(1, 'Tina'),(2, 'Tom'),(3, 'Tony'),(4, 'sala')")
#查询
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print('%s\t%s' %row)

#关闭
cur.close()
cxn.commit()
cxn.close()