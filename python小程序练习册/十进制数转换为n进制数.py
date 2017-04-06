#-*-coding:utf-8-*-
# 把一个十进制数转成n进制，辗转相除，取余，逆序
def mun2n(num,n):
    if n != 0:
        result = []
        while num != 0:
            result.append(num % n)
            num = num / n
        print result[::-1]    

mun2n (10,2)  
