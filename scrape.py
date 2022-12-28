''''This is just a test file on how to scrape the data form the THE HINDHU newspaper website. Please look into the
TheHindhu.py file for the actual concise code...Thank you'''


import requests as res
from bs4 import BeautifulSoup

data = res.get("https://www.thehindu.com/todays-paper/")
soup = BeautifulSoup(data.text, "html.parser")

#for the first column of articles
def first():
    page = soup.find_all("div", id='lead-stories-1')
    articles = [link for link in str(page).split('<div class="element">')]
    del articles[0]
    link=[]
    for i in articles:
        start = i.find('href=')
        start1 = i.find('\"',start+1)
        end = i.find("\"",start1+1)
        atag = i[start1+1:end]
        link.append(atag)
    for j in link:
        url = "https://www.thehindu.com"+j
        news = res.get(url)
        soup2 = BeautifulSoup(news.text, "html.parser")
        title = soup2.find('h1',class_="title").get_text()
        #print(title)
        content = soup2.find_all('p')
        del content[0:5]
        content2 = []
        for i in content:
            i=str(i)
            i = i[i.find('>')+1:i.find('<', i.find('>')+1)]
            content2.append(i)
        para = " ".join(content2)
        return title +'\n' + para



#for the second column of articles
def second():
    page = soup.find_all("div", id='lead-stories-2')
    articles = [link for link in str(page).split('<div class="element">')]
    del articles[0]
    link=[]
    for i in articles:
        start = i.find('href=')
        start1 = i.find('\"',start+1)
        end = i.find("\"",start1+1)
        atag = i[start1+1:end]
        link.append(atag)
    for j in link:
        url = "https://www.thehindu.com"+j
        news = res.get(url)
        soup3 = BeautifulSoup(news.text, "html.parser")
        title = soup3.find('h1',class_="title").get_text()
        #print(title)
        content = soup3.find_all('p')
        del content[0:5]
        content2 = []
        for i in content:
            i=str(i)
            i = i[i.find('>')+1:i.find('<', i.find('>')+1)]
            content2.append(i)
        para = " ".join(content2)
        return title +'\n' + para

first()
second()