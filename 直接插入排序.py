# -*- coding:utf-8 -*-
# 直接插入排序

class SQlite:
    def __init__(self,lst=None):
        self.lst = lst
    def sort(self):
        lst = self.lst
        length = len(lst)
        for i in range(1,length):
            if lst[i] < lst[i-1]:
                temp = lst[i]
                j = i-1
                while lst[j] > temp and j>=0: 
                    lst[j+1] = lst[j]
                    j -= 1
                lst[j+1] = temp
        return lst
sqlite = SQlite([1,4,2,5,8,7])
print sqlite.sort()