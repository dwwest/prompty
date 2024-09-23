import requests
from bs4 import BeautifulSoup
from time import sleep
import json

with open('ids.json') as f:
    ids = json.load(f)

# can go to network tab of inspector and right click on request
# and do copy as curl to get headers needed
urls = (f'https://www.imdb.com/title/tt{id}/taglines/' for id in ids)

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Language':'en-US,en;q=0.5',
           'Accept-Encoding':'gzip, deflate, br, zstd'}

taglines = []

def append_taglines(tags):
    with open('taglines.html', 'w+') as f:
        f.writelines([str(tag) for tag in tags])

    chars = '[]()'
    for tag in tags:
        text = tag.text.strip()
        if not any(c in text for c in chars):
            taglines.append(text)
            print(text)

for url in urls:

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    tags = soup.find_all("div", {"class":"ipc-html-content-inner-div","role":"presentation"})
    
    append_taglines(tags)

    sleep(10)

with open('taglines.json', 'w+') as f:
    json.dump(taglines, f)