import requests
from bs4 import BeautifulSoup

url = 'https://discoverevvnt.com/framed/eyJwX2lkIjo2OTM1LCJ3aWRnZXQiOmZhbHNlLCJsYW5kc2NhcGUiOmZhbHNlLCJ2aXJ0dWFsIjpmYWxzZSwiY19pZCI6bnVsbCwiZF9iYWNrZmlsbF9pbWFnZXMiOmZhbHNlfQ==?evPage=1'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all div elements with class "w-full h-28"
div_elements = soup.find_all('div', class_='c-card block row-span-2 relative md:rounded-t overflow-hidden bg-white rounded subtle-shadow border relative border-white undefined')

# Print the found div elements
for div in div_elements:
    info = div.find('div', class_='w-full h-28')
    url = div.find('a')
    # print("///////")
    if info:
        title = info.find('h3', class_ = 'font-bold line-clamp-2 leading-5')
        destination = info.find('li', class_ = 'line-clamp-1')
        time = info.find('li')
        price = info.find_all('li')[-1]

        print(title.text)
        print(destination.text)
        print(time.text.strip())
        if price.text != destination.text:
            print(price.text)
    if url:
        print(url.get('href'))