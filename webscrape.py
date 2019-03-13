from bs4 import BeautifulSoup
import time
import requests
link = []
news = []
k = 0
response = requests.get("https://timesofindia.indiatimes.com/rss.cms")
soup = BeautifulSoup(response.text,'html.parser')
linkboxes = soup.find_all('span','rssp')
for linkbox in linkboxes :
    link.append(linkbox.contents[0].get('href'))
for l in link :
    k += 1
    resp = requests.get(l)
    fullnews = BeautifulSoup(resp.text,'html.parser')
    if(k != 67 and k != 81) :
        news.append(fullnews.find_all('title')[2].text)
        print(k,"\t",fullnews.find_all('title')[2].text)
    elif(k == 67) :
        print(k,"\t",fullnews.find('h2').contents[0].text)
        news.append(fullnews.find('h2').contents[0].text)
k = 0
while(True) :
    link1 = []
    news1 = []
    k1 = 0
    response1 = requests.get("https://timesofindia.indiatimes.com/rss.cms")
    soup1 = BeautifulSoup(response1.text,'html.parser')
    linkboxes1 = soup1.find_all('span','rssp')
    for linkbox1 in linkboxes1 :
        link1.append(linkbox1.contents[0].get('href'))
    for l1 in link1 :
        k1+=1
        resp1 = requests.get(l1)
        fullnews1 = BeautifulSoup(resp1.text,'html.parser')
        if(k1 != 67 and k1 != 81) :
            news1.append(fullnews1.find_all('title')[2].text)
        elif(k1 == 67) :
            news1.append(fullnews1.find('h2').contents[0].text)
    k1 = 0
    for i in range(1,80) :
        if(news[i] != news1[i]) :
            print("----------UPDATE----------")
            print(i,'/t',news1[i])
            news[i] = news1[i]
    time.sleep(300)