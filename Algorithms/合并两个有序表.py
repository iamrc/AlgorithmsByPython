# 线性表la,lb中的值非递减有序排列，现将两表合并为一个新的线性表lc，且lc中的值非递减有序
def merge(a_list,b_list):
    c_list = []
    a_len = len(a_list)
    b_len = len(b_list)
    pa = pb = 0
    while pa < a_len and pb < b_len:
        if a_list[pa] < b_list[pb]:
            c_list.append(a_list[pa])
            pa = pa + 1                
        else:
            c_list.append(b_list[pb])
            pb = pb + 1                
    c_list.extend(b_list[pb:])
    c_list.extend(a_list[pa:])
    print c_list[::]
la = [1,3,5]
lb = [2,4,6,7,8,10]
merge(la,lb)
