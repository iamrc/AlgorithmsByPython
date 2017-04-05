# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class Solution:
    def rotateArr(self,arr):
        arrlen = len(arr)
        if arrlen == 0:
            return 
        front,end = 0,arrlen-1
        while (end-front)>1:
            middle = (front+end)//2
            if arr[middle] > arr[front] :
                front = middle 
            elif arr[middle] < arr[end] :
                end = middle 
        minVal = end
        print arr[minVal]

s = Solution()
arr1 = [4,5,6,1,2,3]
arr2 = []
arr3 = [1]
s.rotateArr(arr1)
s.rotateArr(arr2)
s.rotateArr(arr3)