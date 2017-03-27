# -*- coding:utf-8 -*-
# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
 
def count(filepath):
    f = open(filepath, 'rb')
    s = f.read()
    words = re.findall('[a-zA-Z0-9]+', s)
    # chars = re.findall('[a-zA-Z0-9]+?',s) 单个字符总数
    return len(words)
 
if __name__ == '__main__':
    num = count('Activation_code.txt')
    print num