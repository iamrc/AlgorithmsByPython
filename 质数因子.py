# -*- coding:utf-8 -*-
'''
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180=2X2X3X3X5,它的质数因子为2　2 3 3 5 ）
'''
a = raw_input()

def yinshi(a):
    while a != 1:
        for i in range(2,a+1):
            if(a%i == 0):
                a /= i
                print i
                break
yinshi(64577)