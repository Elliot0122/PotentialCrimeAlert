import json
import datetime
import requests
from GoogleMap import GetGeoCode
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
        category = div.find_all('span', class_='inline-block mr-1')

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
                events[year][new_month][new_date][title]["Geocode"] = GetGeoCode(destination)
                if price != destination:
                    events[year][new_month][new_date][title]["price"] = price
                else:
                    events[year][new_month][new_date][title]["price"] = "unavailable or free"
                if url:
                    events[year][new_month][new_date][title]["url"] = url.get('href')
                if category:
                    events[year][new_month][new_date][title]["category"] = []
                    for i in category:
                        events[year][new_month][new_date][title]["category"].append(i.text)
    with open('./data/event.json', 'w') as fp:
        json.dump(events, fp)

def return_event(date):
    create_data_to_json()
    year, month, day = date.split('/')
    with open('./data/event.json', 'r') as fp:
        data = json.load(fp)
        if data[year][month][day]:
            event_name = []
            for key in data[year][month][day]:
                event_name.append(key)
            return event_name, data[year][month][day]
        else:
            return {}
        
def return_dates():
    with open('./data/event.json', 'r') as fp:
        all_date = []
        data = json.load(fp)
        for i in data:
            for j in data[i]:
                for k in data[i][j]:
                    temp = {
                        "year": i,
                        "month": j,
                        "date": k
                    }
                    all_date.append(temp)
    file_path = "data/date.json"
    with open(file_path, 'w') as f:
        json.dump(all_date, f)

def return_event_days(date1, date2):
    create_data_to_json()
    year1, month1, date1 = date1.split('/')
    year2, month2, date2 = date2.split('/')
    year1, month1, date1, year2, month2, date2 = int(year1), int(month1), int(date1), int(year2), int(month2), int(date2)
    event_info = []
    with open('./data/event.json', 'r') as fp:
        data = json.load(fp)
        for i in range(year1, year2+1):
            for j in range(month1, month2+1):
                for k in range(date1, 32):
                    if j == month2+1 and k > date2:
                        break
                    if str(i) in data and str(j) in data[str(i)] and str(k) in data[str(i)][str(j)]:
                        temp = dict()
                        for l in data[str(i)][str(j)][str(k)].keys():
                            temp["title"] = l
                            temp["lat"] = data[str(i)][str(j)][str(k)][l]["Geocode"]["lat"]
                            temp["lng"] = data[str(i)][str(j)][str(k)][l]["Geocode"]["lng"]
                        event_info.append(temp)
    file_path = "./data/EventDate.json"
    with open(file_path, 'w') as f:
        json.dump(event_info, f)

if __name__ == '__main__':

    # create_data_to_json()
    # try:
    #     print(return_event("2023/6/2"))
    # except:
    #     print("No event")

    print(return_dates())