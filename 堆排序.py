#!/usr/bin/envpython
#-*-coding:utf-8-*-
import MySQLdb
 
def fixDown(a,k,n): #自顶向下堆化，从k开始堆化  
    N=n-1  
    while 2*k<=N:  
        j=2*k  
        if j<N and a[j]<a[j+1]: #选出左右孩子节点中更大的那个  
            j+=1  
        if a[k]<a[j]:  
            a[k],a[j]=a[j],a[k]  
            k=j  
        else:  
            break  
  
def heapSort(ls):  
    n=len(ls)-1  
    for i in range(n/2,0,-1):  
        fixDown(ls,i,len(ls))  
    while n>1:  
        ls[1],ls[n]=ls[n],ls[1]  
        fixDown(ls,1,n)  
        n-=1  
    return ls[1:]  
  
ls=[-1,26,5,77,1,61,11,59,15,48,19] #第一个元素不用，占位  
res=heapSort(ls)  
print(res)
print MySQLdb