from urllib import urlopen
from bs4 import BeautifulSoup
import os

articlepages = os.listdir('/Users/kathryn/Desktop/montagarticles')
for htmlFile in articlepages:

    textUrl = '/Users/kathryn/Desktop/montagarticles/' + htmlFile
    textPage = urlopen(textUrl)
    text = textPage.read()
    soup = BeautifulSoup(text)
    articletext = soup.find_all(class_="content-text")
    for element in articletext:
        words = element.get_text().encode('utf-8')
        f = open("montagtext.txt", "a")
        f.write(words)
    f.close()
