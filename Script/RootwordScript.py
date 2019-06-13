'''
建立26个线程，分别爬取不同字母（开启的一段时间内，只出现了12个进程，阻塞了很久）
'''
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import threading

class Root_Diction:

    def __init__(self):
        UA = UserAgent().random
        self.page_url = []
        self.headers = {'User-Agen':UA}
        self.url_sort={}

    def _thread(self):
        home_page_token = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
        need_join=[]
        for i in range(len(home_page_token)):
            th=threading.Thread(target=self.get_all_Url,args=(home_page_token[i]))
            th.start()
            print('线程%s启动'%home_page_token[i])
            need_join.append(th)
        for j in need_join:
            j.join(timeout=300)

    #获得所有的A，B，C...页面的所有页码url
    def get_all_Url(self,letter):
        j = 1  # j作为输出，查看爬取进度
        try:
            for i in range(65):
                url = 'https://www.youdict.com/root/page/' + str(letter)+'/'+str(i)
                html = requests.get(url, headers=self.headers,allow_redirects=False)   #超出页码之后，由于重定向，状态码依旧是200，需要重定向
                if html.status_code != 200:  # 不等于200时，说明页码60太大了，已经结束了
                    break  #不能用continue，继续的话，只会让i+1然后继续重定向继续continue直到遍历结束
                html.encoding = 'utf-8'
                soup = BeautifulSoup(html.text, 'lxml')
                datas = soup.select('.content')

                # 数据处理
                data = datas[0].get_text()
                # data = data.replace('【', '').replace('】', '')
                # data = data.replace('词根含义', '\n【含义】')
                # data = data.replace('词根来源', '\n【来源】')
                # data = data.replace('同源单词', '\n【同源】')
                # data = data.replace('拉丁语词根', '\n拉丁语')
                # data = data.replace('相关描述', '\n【相关】')
                # data = data.replace('与词根', '与')
                # data = data.replace('相关词缀', '\n【相关】')
                # data = data.replace('相关词根词缀', '\n【相关】')
                # data = data.replace('来源及含义', '\n来源及含义：')
                # data = data.replace('同源词', '\n【同源词】')
                # data = data.replace('词根', '\n【词根】')
                # data = data.replace('后缀', '\n【后缀】')
                # data = data.replace('前缀', '\n【前缀】')
                with open('D:/Root_Diction/' + str(letter) + '.txt', 'a', encoding='utf-8') as f:  # a表示追加，不存在则创建
                    f.write(data + '\n\n\n')
                    f.close()

                print('*******成功写入%s的第%d页数据，请等待*******' %(letter,j))
                j += 1
        except Exception as e:
            print('爬取过程出现错误，错误信息：',e)
        print('%s线程结束'%letter)

    #运行程序
    def run(self):
        self._thread()

dic = Root_Diction()
dic.run()