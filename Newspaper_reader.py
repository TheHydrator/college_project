#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from urllib.request import urlopen

import nltk

import feedparser as fp

import newspaper

from newspaper import Article

ans = input("APNA_KHABRI \n\n"
            "1. TELL ME THE LATEST NEWS \n"
            "2. I'LL CHOOSE THE NEWS CATEGORY \n")

if ans == '1':
    site = 'https://news.google.com/news/rss'


elif ans == '2':
    cat = input("Select NEWS category \n"
                "1.COMPANIES \n"
                "2.OPINION \n"
                "3.MONEY \n"
                "4.POLITICS \n"
                "5.SCIENCE \n"
                "6.INDUSTRY \n"
                "7.SPORTS  \n"
                "8.TECHNOLOGY \n"
                "9.MARKETS \n"
                "10.AI \n"
                )
    rsslink = {"1": "https://www.livemint.com/rss/companies",
               "2": "https://www.livemint.com/rss/opinion",
               "3": "https://www.livemint.com/rss/money",
               "4": "https://www.livemint.com/rss/politics",
               "5": "https://www.livemint.com/rss/science",
               "6": "https://www.livemint.com/rss/industry",
               "7": "https://www.livemint.com/rss/sports",
               "8": "https://www.livemint.com/rss/technology",
               "9": "https://www.livemint.com/rss/markets",
              "10": "https://www.livemint.com/rss/AI"}

    site = rsslink.get(cat)

else:
    print("wrong input")

# webscrapping the rss feed

from bs4 import BeautifulSoup as soup

import os

op = urlopen(site)  # Open that site

rd = op.read()  # read data from site

op.close()  # close the object

sp_page = soup(rd, 'xml')  # scrapping data from site

news_list = sp_page.find_all('item')  # finding news

from gtts import gTTS

for news in news_list:

    print(news.title.text)
    url = news.link.text

    article = Article(url)
    article.download()
    article.parse()

    #article.nlp()
    print(article.summary)

    mytext = news.title.text

    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save('latestnews.mp3')
    os.system('start latestnews.mp3')

    com = input("do you want hear the next news(y/n)")
    if com == 'y':
        continue
    elif com == 'n':
        break
    else:
        print("wrong input")
        break


# In[ ]:





# In[ ]:




