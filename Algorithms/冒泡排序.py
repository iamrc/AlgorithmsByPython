# -*- coding: utf-8 -*-  
'''
冒泡排序

基本思想：从第一个元素开始，每每相邻的两个元素进行比较，若前者比后者大则交换位置。最后两个相邻元素比较完成后，最大的元素形成，然后再次从头开始进行比较，若元素个数为n+1个，则总共需要进行n轮比较就可完成排序（n轮比较后，n个最大的元素已经形成，最后一个元素当然是最小的，就不用再比了）。每轮比较中，每形成一个最大的元素，下一轮比较的时候 就少比较一次，第一轮需要比较n次，第二轮需要比较n-1次，以此类推，第n轮（最后一轮）只需要比较1次就可。这样，列表就排好序了。

按照上面的分析，我们需要两个循环，外循环控制轮数，内循环控制每轮的次数。
'''
#!/usr/bin/python  
import random  
      
unsortedList=[]  
      
# generate an unsorted list  
def generateUnsortedList(num):  
    for i in range(0,num):  
        unsortedList.append(random.randint(0,100))  
    print unsortedList  
      
# 冒泡排序  
def bubbleSort(unsortedList):  
    list_length=len(unsortedList)  
    for i in range(0,list_length-1):  
        for j in range(0,list_length-i-1):  
            if unsortedList[j]>unsortedList[j+1]:  
                unsortedList[j],unsortedList[j+1]=unsortedList[j+1],unsortedList[j]  
    return unsortedList  
      
generateUnsortedList(5)  
print bubbleSort(unsortedList)  
