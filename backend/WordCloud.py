import pandas as pd
import os
import json
column_names = [
    "Category",
    "Frequency"
]
def count_categories():
    json_file = './event.json'
    with open(json_file) as file:
        data = json.load(file)

    category_counts = {}

    for year, year_data in data.items():
        for month, month_data in year_data.items():
            for day, day_data in month_data.items():
                for event_name, event_details in day_data.items():
                    categories = event_details["category"]
                    for category in categories:
                        if category in category_counts:
                            category_counts[category] += 1
                        else:
                            category_counts[category] = 1

    print(category_counts)
    category_result = []

    for i, count in category_counts.items():
        categories = i.split("/")
        for category in categories:
            sub_categories = category.split("&")
            for sub_category in sub_categories:
                sub_category = sub_category.strip()
                temp = {"category": sub_category, "frequency": count}
                category_result.append(temp)


    with open('wordcloud.json', 'w') as file:
        json.dump(category_result, file)

if __name__ == "__main__":
    count_categories()
