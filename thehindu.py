import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta  # Make sure we import datetime correctly

def _get_the_hindu():
    
    # Send a request to the website
    url = "https://www.thehindu.com/latest-news/"
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')


    # Extract the date
    date = soup.find(class_="latest-date").text.strip()

    # Find all news items
    news_items = soup.find_all(class_="element")

    now = datetime.now()  # Get the current time
    news_data = []

    for item in news_items:
        title_tag = item.find(class_="title")
        if title_tag:
            title = title_tag.text.strip()
            link = title_tag.find('a')['href']
            time_tag = item.find(class_="news-time")
            
            if time_tag:
                published_time_str = time_tag['data-published']
                published_time = datetime.strptime(published_time_str, "%Y-%m-%dT%H:%M:%S%z")
                delay = now - published_time.replace(tzinfo=None)
                delay_minutes = int(delay.total_seconds() // 60)
                time_ago = f"{delay_minutes} minutes ago" if delay_minutes > 0 else "Just now"
            else:
                time_ago = "No time available"
            
            news_item = {
                "title": title,
                "link": link,
                "published_time": time_ago
            }
            news_data.append(news_item)

    json_data = {
        "date": date,
        "news": news_data
    }

    json_data_str = json.dumps(json_data, indent=4)

    # with open('headlines.json', 'w') as json_file:
    #     json_file.write(json_data_str)

    return json.loads(json_data_str)
