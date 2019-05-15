from urllib import urlopen
from bs4 import BeautifulSoup
import os
count = 1
montagpages = os.listdir('/Users/kathryn/Desktop/montagpages')
for htmlFile in montagpages:
    textUrl = '/Users/kathryn/Desktop/montagpages/' + htmlFile
    textPage = urlopen(textUrl)
    text = textPage.read()
    soup = BeautifulSoup(text)
    articles = soup.find_all(class_="homepage-post-info")
    for x in articles:
        links = x.find_all("a")
        for a in links:
            link = a['href']
            f = open("getmontagarticles.sh", "a")
            f.write("curl https://www.montag.wtf" + link + " -o ~/Desktop/montagarticles/" + str(count) + ".html\n")
            count += 1
            f.close()
