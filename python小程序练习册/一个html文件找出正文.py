# -*- coding: utf-8 -*-
import bs4
# 利用本地的html文件创建对象
html_doc = open('./test.html')

def extract_content():
    soup = bs4.BeautifulSoup(html_doc, "lxml")
    return soup.body

if __name__ == '__main__':
    print(extract_content())