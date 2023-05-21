import json
import os

file_path = "origin_crime.json"

tags = ["DateReported", "Time", "Type", "Location", "lat", "lng"]
geo_tag = ["lat", "lng"]

crime  = dict()

with open(file_path) as f:
    data = json.load(f)

    for i in data:
        month, date, year = i[tags[0]].split("/")
        time = i[tags[1]]
        title = i[tags[2]]
        destination = i[tags[3]]
        lat = i[tags[4]]
        lng = i[tags[5]]
        if year not in crime:
            crime[year] = dict()
        if month not in crime[year]:
            crime[year][month] = dict()
        if date not in crime[year][month]:
            crime[year][month][date] = dict()
        if title not in crime[year][month][date]:
            crime[year][month][date][title] = dict()
        crime[year][month][date][title]["destination"] = destination
        crime[year][month][date][title]["time"] = time
        crime[year][month][date][title]["Geocode"] = dict()
        crime[year][month][date][title]["Geocode"]["lat"] = lat
        crime[year][month][date][title]["Geocode"]["lng"] = lng

file_path = "new_crime.json"
with open(file_path, 'w') as f:
    json.dump(crime, f)