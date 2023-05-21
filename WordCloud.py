import pandas as pd
import os
import json
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
    return category_counts
if __name__ == "__main__":
    count_categories()