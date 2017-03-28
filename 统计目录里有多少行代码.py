# -*- coding: utf-8 -*-
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import os
import glob
 
# Get all files in designated path
def get_files(path):
    return glob.glob(path + r'/*')
 
# Count lines and blank lines and note lines in designated files
def count_lines(files):
    line, blank, note = 0, 0, 0
    for filename in files:
        f = open(filename, 'rb')
        for l in f:
            l = l.strip()
            line += 1
            if l == '':
                blank += 1
            elif l[0] == '#' or l[0] == '/':
                note += 1
        f.close()
    return (line, blank, note)
 
if __name__ == '__main__':
    files = get_files('./filetext/child_dir')
    # print files
    lines = count_lines(files)
    print 'Line(s): %d, black line(s): %d, note line(s): %d' % (lines[0], lines[1], lines[2])