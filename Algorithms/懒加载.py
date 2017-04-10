# -*- coding:utf-8 -*-
# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def lazy_port():
        def multip(a,b):
            return a*b
        return reduce(multip,lst,1)
    return lazy_port

f = calc_prod([1,2,3])
print f()