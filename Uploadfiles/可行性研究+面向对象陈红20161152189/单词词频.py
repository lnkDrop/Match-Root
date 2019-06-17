import re
punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')

word_count_list={}
with open("in.txt",'r') as f:
    for line in f:
        #print('去除标点前：',line)
        line2 = ''.join(filter(lambda x: x not in punct, line))
        #print('去除标点后：', line2)
        wordlist=line2.strip().split()
        for word in wordlist:
            #print('({})'.format(word),end='')
            if word not in word_count_list.keys():
                word_count_list[word]=1
            else:
                word_count_list[word]+=1

print(word_count_list)
