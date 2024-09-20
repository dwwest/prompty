import requests
from bs4 import BeautifulSoup
from time import sleep
import json




# can go to network tab of inspector and right click on request
# and do copy as curl to get headers needed
urls = ['https://www.imdb.com/title/tt0457430/taglines/']
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Languague':'en-US,en;q=0.5',
           'Accept-Encoding':'gzip, deflate, br, zstd'}

taglines = []
for url in urls:

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    tags = soup.find_all("div", {"class":"ipc-html-content-inner-div","role":"presentation"})
    for tag in tags:
        taglines.append(tag.text.strip())
    
    sleep(10)

with open('taglines.json', 'w+') as f:
    json.dump(taglines, f)