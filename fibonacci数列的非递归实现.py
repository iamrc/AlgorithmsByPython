# -*- coding:utf-8 -*-
'''
斐波那切数列的非递归实现
现在要求输入一个整数n，请你输出斐波那契数列的第n项。
'''

class Solution:
    def fibonacciateArr(self,n):
        first,second = 0,1
        fibN = 0
        count = 2
        n = int(n)
        if n < 3:
            print 'input error'
        else:
            while count < n:
                fibN = fibN + second
                first = second
                second = fibN
                count += 1
            print fibN
            
s = Solution()
s.fibonacciateArr(-2)
s.fibonacciateArr(1)
s.fibonacciateArr(2)
s.fibonacciateArr(2.5)
s.fibonacciateArr(6)
