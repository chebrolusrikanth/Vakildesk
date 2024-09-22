import requests
from bs4 import BeautifulSoup
url = 'https://edition.cnn.com/'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h3', class_='cd__headline')

    for article in articles:
        title = article.get_text(strip=True)
        link = article.find('a')['href']
        
        if not link.startswith('http'):
            link = 'https://edition.cnn.com' + link
        
        print(f'Title: {title}')
        print(f'URL: {link}\n')
else:
    print("Failed to retrieve the page. Status code:",response.status_code)
