#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 sensitive，否则打印出 normal。
import re

def filtered_words(filepath,word):
    wordslist = []
    f = open(filepath,'rb')
    s = f.read()
    wordslist = re.findall('[a-zA-Z0-9]+',s)
    print wordslist
    return word in wordslist


word = raw_input('please input your sensitive word:')
print filtered_words('filtered_words.txt',word)