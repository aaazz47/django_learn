# 加载项目
    # BeautifulSoup 用于解析页面
    # requests 用于请求页面
    # collections.deque 队列，利用先进先出暂存待抓取页面
    # time.sleep 增加抓取时间间隔

import requests
import time
import re

from bs4 import BeautifulSoup
from collections import deque

# 初始化
queue = deque()    # 队列，记录待抓取页面
visited = set()    # 集合，用于记录已抓取页面
file_name = 'urls.txt'
baseurl = 'http://www.597club.com'    #抓取入口
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux i686; rv:55.0) Gecko/20100101 Firefox/55.0'}

queue.append(baseurl)
cnt = 1

while queue:
    url = queue.popleft() # 取出对首元素

    print('抓取序号：' + str(cnt) + '  正在抓取：--' + url)
    time.sleep(5)
    rq = requests.get(url, headers = headers)
    print('    序号:' + str(cnt) + ' 抓取成功 正在解析...')
    cnt += 1

    data = BeautifulSoup(rq.text, 'lxml')
    for link in data.find_all('a'):
        link = link.get('href')
        if link != None:
            if 'http' not in link:
                try:
                    link = baseurl + re.match('^/.*',link).group()
                except:
                    continue
            
            if link not in visited:
                visited |= {link}    # 并集加入已抓取集合
                queue.append(link)
                print("  加入队列：--" + link)
                
                with open(file_name,'a+') as f:
                    f.write(link + '\n')



# # 使用requests请求网页

# rq = requests.get(url, headers=headers)

# soup = BeautifulSoup(rq.text,'lxml')

# for link in soup.find_all('a'):
#     link = link.get('href')
#     if link != None:
        
#         # 储存到文档
#         file_name = ('urls.txt')
#         with open(file_name,'a+') as f:
#             f.write(link + '\n')
        



