# -*- coding: utf-8 -*-

import os
def countword(file):
        filelist=[]   #储存文件名
        wordcounts={}   #储存单词及词频
        print "\n*****往年试卷高频词汇******\n"
        for f in os.listdir("file"):  #遍历文件夹中的文件
            #print f
            list.append(f)
            filelist1=filelist[1:]    #获取试卷文件名
        #print filelist1
            for paper in filelist1:   #遍历文件
                content=open("%s/%s"%(paperfile,paper)).read().strip().split()   #打开并读取试卷
                for word in content:
                    word=word.rstrip('.').rstrip(',').rstrip(':').strip("()")  #去除单词前后的标点符号
                    if word not in wordcounts:
                        wordcounts[word]=1     
                    else:
                        wordcounts[word]+=1
        new_wordcounts=sorted(wordcounts.iteritems(),key=lambda v:v[1],reverse=True)   #v[1]为键值排序，v[0]为键排序，
        #生成的是以元组为元素的列表
        for i in  new_wordcounts:
             print i
        return i
paperfile="C:\Users\Administrator\Desktop\paperfile.txt"
countword(paperfile)    #调用函数
