import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.ucdavis.edu/news/latest"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all the title elements with the specified class
    titles = soup.find_all("span", class_="field field--name-title field--type-string field--label-hidden")
    categories = soup.find_all("li", class_="vm-teaser__cat-marker")
    websites = soup.find_all("a", href_="vm-teaser__cat-marker")
    # Extract the text from the title elements and display them
    for title in titles:
        if title:
            print(title.text)