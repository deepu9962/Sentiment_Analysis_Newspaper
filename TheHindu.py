import requests as res
from bs4 import BeautifulSoup

data = res.get("https://www.thehindu.com/todays-paper/")
soup = BeautifulSoup(data.text, "html.parser")

def hindu():
    ids = ['lead-stories-1','lead-stories-2']  #id attribute of each column articles 
    dictionary = {}
    for m in range(len(ids)):                   #to webscrape from the official website of TheHindu Newspaper website
        page = soup.find_all("div", id=ids[m])
        articles = [link for link in str(page).split('<div class="element">')]
        del articles[0]
        link=[]
        for i in articles:                  #just to get the links of the articles, later which will be used to get the content of the article
            start = i.find('href=')
            start1 = i.find('\"',start+1)
            end = i.find("\"",start1+1)
            atag = i[start1+1:end]
            link.append(atag)
        for j in link:                     #Now to get the content for sentiment analysis
            url = "https://www.thehindu.com"+j
            news = res.get(url)
            soup2 = BeautifulSoup(news.text, "html.parser")
            title = soup2.find('h1',class_="title").get_text()
            content = soup2.find_all('p')
            del content[0:5]
            content2 = []
            for i in content:               #cleaning the data
                i=str(i)
                i = i[i.find('>')+1:i.find('<', i.find('>')+1)]
                content2.append(i)
            para = " ".join(content2)

            #to just have a snapshot
            #print(title)
            #print(para)

            #for sentiment analysis, we'll just stack up the articles and their respective content to a list and send them accordingly
            dictionary[title]=para
    return dictionary

hindu()