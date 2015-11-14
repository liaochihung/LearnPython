import requests

from bs4 import BeautifulSoup


def start(url):
    wordList = []
    source = requests.get(url).text
    soup = BeautifulSoup(source)
    for postText in soup.findAll('a', {'class': 'index_singleListTitles'}):
        content = postText.string
        words = content.lower().split()
        for eachWord in words:
            print(eachWord)
            wordList.append(eachWord)


start("https://buckysroom.org/tops.php?type=text&period=this-month")
