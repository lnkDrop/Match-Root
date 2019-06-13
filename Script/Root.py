#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
def azlist():
    List = []
    for ch in range(97, 123):
        List += chr(ch)
    return List
num = azlist()
for i in range(len(num)):
    f = open(r"D:/Project/Root_Diction/"+str(num[i])+".txt", 'r', encoding='utf-8')
    lines = f.readlines()
    RD = []
    for line3 in lines:
        if line3[0:4] == "【词根】":
            result_list = re.findall('[a-zA-Z]+', line3)  # 正则表达式取出词根
            if len(result_list) and result_list[0].startswith(num[i]):
                # print(result_list)
                RD += list(set(result_list))
    f = open(".txt")
    f.write(str(RD))  # 将字符串写入文件中
    f.write("\n")  # 换行  
    print(RD)

    f.close()
