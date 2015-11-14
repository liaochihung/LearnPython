url = 'https://buckysroom.org/trade/search.php?page='

'''
def tradeSpider(maxPages):
    page = 1
    while page < maxPages:
        curUrl = url + str(page)
        sourceCode = requests.get(curUrl)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = link.get('href')
            print(href)
        page += 1

tradeSpider(1)
'''
