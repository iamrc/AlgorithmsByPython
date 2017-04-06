#-*-coding:utf-8-*-
#def print_directory_contents(sPath):
"""
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。
"""
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print sChildPath

print print_directory_contents('/tmp/')

def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPtah,sChild)
        if os.path.isdir(sChild):
            print_directory_contents(sChild)
        else print sChildPath