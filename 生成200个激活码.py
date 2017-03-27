# -*- coding:utf-8 -*-
# 使用 Python 如何生成 200 个激活码
import random, string
 
def rand_str(num, length = 7):
    st = ''
    for i in range(num):
        chars = string.letters + string.digits
        s = [random.choice(chars)for j in range(length)]
        st = st+''.join(s)+'\n'
    with open('Activation_code.txt','wb') as f: 
        f.write(st)

if __name__ == '__main__':
    rand_str(200)