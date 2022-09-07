import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/product-reviews/B0834KJBM3/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
reviewlist = []

def get_soup(url):
    # send the url to splash service to render the page
    r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook':'review'})
    try:
        for item in reviews:
            review = {
            'product': soup.title.text.replace('Amazon.in:Customer reviews: ','').strip(),
            'title' : item.find('a',{'data-hook':'review-title'}).text.strip(),
            'rating' : float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
            'body' : item.find('span',{'data-hook':'review-body'}).text.strip()
            }
            reviewlist.append(review)            
    except:
        pass

for x in range(1,100):
    soup = get_soup(f'https://www.amazon.in/product-reviews/B0834KJBM3/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break


df = pd.DataFrame(reviewlist)
df.to_excel('Maono AU-MH601 Professional.xlsx', index=False)
print('Fin')