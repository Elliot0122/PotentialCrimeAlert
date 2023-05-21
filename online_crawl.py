import json
import datetime
import requests
from bs4 import BeautifulSoup
def create_data_to_json():
    month = {
        'Jan' : '1',
        'Feb' : '2',
        'Mar' : '3',
        'Apr' : '4',
        'May' : '5',
        'Jun' : '6',
        'Jul' : '7',
        'Aug' : '8',
        'Sep' : '9',
        'Oct' : '10',
        'Nov' : '11',
        'Dec' : '12'
    }

    url = 'https://discoverevvnt.com/framed/eyJwX2lkIjo2OTM1LCJ3aWRnZXQiOmZhbHNlLCJsYW5kc2NhcGUiOmZhbHNlLCJ2aXJ0dWFsIjpmYWxzZSwiY19pZCI6bnVsbCwiZF9iYWNrZmlsbF9pbWFnZXMiOmZhbHNlfQ==?evPage=1'

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all div elements with class "w-full h-28"
    div_elements = soup.find_all('div', class_='c-card block row-span-2 relative md:rounded-t overflow-hidden bg-white rounded subtle-shadow border relative border-white undefined')


    events = dict()

    year = datetime.date.today().year
    if year not in events:
        events[year] = dict()

    # Print the found div elements
    for div in div_elements:
        date = div.find('div', class_ = '-mt-1 shadow-md')
        info = div.find('div', class_='w-full h-28')
        url = div.find('a')
        category = div.find('div', class_='flex-none inline-flex py-1 px-2 rounded-2xl text-xs font-semibold border border-theme subtle-shadow items-center bg-white text-theme-alt')

        if date:
            date = date.find_all('span')
            new_month = month[date[0].text]
            new_date = date[1].text
            if new_month not in events[year]:
                events[year][new_month] = dict()
            if new_date not in events[year][new_month]:
                events[year][new_month][new_date] = dict()
            
        if info:
            title = info.find('h3', class_ = 'font-bold line-clamp-2 leading-5').text
            destination = info.find('li', class_ = 'line-clamp-1').text
            time = info.find('li').text
            price = info.find_all('li')[-1].text

            if title not in events[year][new_month][new_date]:
                events[year][new_month][new_date][title] = dict()
                events[year][new_month][new_date][title]["destination"] = destination
                events[year][new_month][new_date][title]["time"] = time.strip()
                if price != destination:
                    events[year][new_month][new_date][title]["price"] = price
                else:
                    events[year][new_month][new_date][title]["price"] = "unavailable or free"
                if url:
                    events[year][new_month][new_date][title]["url"] = url.get('href')
                    print(url.get('href'))
                if category:
                    events[year][new_month][new_date][title]["url"] = category.text
    with open('./data/event.json', 'w') as fp:
        json.dump(events, fp)



if __name__ == '__main__':
    create_data_to_json()
    # retrun_event()