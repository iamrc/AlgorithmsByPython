# -*- coding:utf-8 -*-
'''
斐波那切数列的非递归实现
现在要求输入一个整数n，请你输出斐波那契数列的第n项。
'''
class Solution:
    def fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
        
    def fibonacci_recursion(self,n):
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

s = Solution()
print s.fibonacci_recursion(3)