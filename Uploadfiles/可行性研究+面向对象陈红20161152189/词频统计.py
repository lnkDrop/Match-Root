import re
f=open("英语文本.txt") 
#读取文件中的字符串
txt = f.read()
 #去除字符串中的标点、数字等
txt = re.sub('[,\.()":;!@#$%^&*\d+-/?"<>]|\'s|\'', '', txt)
#替换换行符，大小写转换，拆分成单词列表
word_list = txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
d = {}#创建一个空字典
for word in word_list:
#统计字典中的词频
    if word in d.keys():
        d[word] += 1
    else:
        d[word] =1
#按照单词出现次数排序
d= sorted(d.items(), key=lambda x:x[1], reverse=True)
#输出到文件
f1=open("词频统计.txt", 'w')
for i in d:
    f1.write("%s\t%s\n" %(i[0],str(i[1])))
f1.close()


