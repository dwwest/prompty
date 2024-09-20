import requests
from bs4 import BeautifulSoup
from time import time, sleep
from warnings import warn
from random import randint
import math
import re

# adapted from: https://stackoverflow.com/questions/47483067/pull-imdbids-for-titles-on-search-list

# this is very hard coded!

url = 'http://www.imdb.com/search/title?num_votes=25000,&title_type=feature&view=simple&sort=num_votes,desc&page=1&ref_=adv_nxt'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Languague':'en-US,en;q=0.5',
           'Accept-Encoding':'gzip, deflate, br, zstd'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
num_films_text = soup.find_all('div', {'class':'sc-e3ac1175-3 jfNgiQ'})
num_films=re.search(r'of ([\d,]+)',str(num_films_text[0])).group(1)
num_films=int(num_films.replace(',', ''))
print(num_films)

num_pages = math.ceil(num_films/50)
print(num_pages)

ids = []
start_time = time()
rs = 0

# For every page in the interval`
for page in range(1,num_pages+1):    
    # Make a get request    
    url = "http://www.imdb.com/search/title?num_votes=25000,&title_type=feature&view=simple&sort=num_votes,desc&page="+str(page)+"&ref_=adv_nxt"
    response = requests.get(url, headers=headers)

    # Pause the loop
    sleep(randint(8,15))  

    # Monitor the requests
    rs += 1
    sleep(randint(1,3))
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'.format(rs, rs/elapsed_time))

    # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(rs, response.status_code))   

    # Break the loop if the number of requests is greater than expected
    if rs > num_pages:
        warn('Number of requests was greater than expected.')  
        break

    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')

    # Select all the 50 movie containers from a single page
    movie_containers = page_html.find_all('div', class_ = 'lister-item mode-simple')

    # Scrape the ID 
    for i in range(len(movie_containers)):
        id = re.search(r'tt(\d+)/',str(movie_containers[i].a)).group(1)
        ids.append(id)
print(ids)
