# -*- coding:utf-8 -*-
'''
连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
'''
a=raw_input()
def chstr(line):
    left = len(line)%8
    if left != 0:
        line += '0' * (8 - left)
    for i in range(len(line) / 8):
        print line[i*8:(i+1)*8] 

chstr(a)