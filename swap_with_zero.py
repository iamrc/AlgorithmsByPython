# -*- coding:utf-8 -*-
'''
交换数组里n和0的位置
array: 存储[0-n)的数组
len: 数组长度
n: 数组里要和0交换的数
'''

class Swap_with_zero:
    def __init__(self,lst=None):
        self.lst = lst
    def sort(self):
        lst = self.lst
        length = len(lst)
        if length == 0:
            return 
        p0 = pi = pf = 0
        for i in range(0,length):
            #找０元素
            if lst[i] == i:
                pi += 1
                continue
            else:
                for j in range (0,length):
                    #找０
                    if lst[j] == 0:
                        p0 = j
                    #找i位置的目标元素(即值等于i的元素)
                    if lst[j] == i:
                        pf = j
                if p0 == pf:
                    lst[pi],lst[p0] = lst[p0],lst[pi]
                else:
                    lst[pi],lst[p0] = lst[p0],lst[pi]
                    lst[pi],lst[pf] = lst[pf],lst[pi]
                pi += 1
        lst[0] = 0
        return lst
        
s1 = Swap_with_zero([0,2,3,1,5,4])
s2 = Swap_with_zero([3,2,1,0])
print s1.sort()
print s2.sort()

                

