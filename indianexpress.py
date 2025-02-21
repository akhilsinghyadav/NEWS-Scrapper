import json


from bs4 import BeautifulSoup
import requests

def _get_the_express():  
    MAX_LIM = 4       ###############     CONTROLLLER
    num = 2
    news_data_ie = []
    first_url = "https://indianexpress.com/section/explained/"
    _get_the_ex_url(first_url, news_data_ie)
    while num < MAX_LIM:
        # print(f'traverse{num}')
        base_url =  f"https://indianexpress.com/section/explained/page/{num}"
        _get_the_ex_url(base_url, news_data_ie)
        num = num +1 
        
                
    json_data_str_ie = json.dumps(news_data_ie, indent=4)
    return json.loads(json_data_str_ie)

def _get_the_ex_url(url, news_data_ie):
    response = requests.get(url) 
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    h3_elements = soup.find_all('h3')
    # print(len(h3_elements))
    for h3 in h3_elements:
        # counter = 0
        a = h3.find('a')
        url = a['href']
        title = a['title'] # a.text
        news_item_ie = {
                "title": title,
                "link": url,
            }
        # counter=counter+1
        # print(counter)
        news_data_ie.append(news_item_ie)
