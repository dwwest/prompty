import requests
from bs4 import BeautifulSoup

# can go to network tab of inspector and right click on request
# and do copy as curl to get headers needed
url = 'https://www.imdb.com/title/tt0457430'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Languague':'en-US,en;q=0.5',
           'Accept-Encoding':'gzip, deflate, br, zstd'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
