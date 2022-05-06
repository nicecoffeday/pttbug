import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0')

def PttStock(url):
    resp = requests.get(url)        #確認url 狀況 是否能連上
    if resp.status_code != 200:
        print('URL發生網址:' + url)
        return
    
    soup = BeautifulSoup(resp.text , 'html5lib')
    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']  #取得上一頁 功能標籤

    articles = []
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()
        count = rent.find('div', 'nrec').text.strip()
        date = rent.find('div', 'meta').find('div', 'date').text.strip()
        article = '%s %s:%s' % (date, count, title) #將上述抓的資訊 串再一起

        try:
            if today == date and int(count) > 70:
                articles.append(article)
        
        except:
            if today == date and count == '爆':
                articles.append(article)
    
    if len(articles) != 0:
        for article in articles:
            print(article)
        PttStock('https://www.ppt.cc' + paging)
    else:
        return
PttStock('https://www.ptt.cc/bbs/Stock/index.html')
