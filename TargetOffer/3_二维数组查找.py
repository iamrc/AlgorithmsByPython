# -*- coding:utf-8 -*-
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
'''
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # 标识变量
        found = False
        # 检查输入 None，空数组
        if len(array) == 0 or len(array[0]) == 0:
            return found
        nRow = len(array)
        nCol = len(array[0])
        # 右上角位置
        row = 0
        col =  nCol-1
        # 从右上角遍历
        while (row<nRow) and (col>=0):
            if array[row][col] ==  target:
                found = True
                break
            elif array[row][col] >  target:
                col = col-1
            else:
                row = row+1
        return found

myarr = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
p= Solution()
print p.Find(7,myarr)