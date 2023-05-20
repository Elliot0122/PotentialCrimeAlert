from bs4 import BeautifulSoup

file_path = 'path/to/your/file.html'

with open(file_path, 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# Perform crawling operations on the parsed HTML content
# For example:
# Find all <a> tags and print their href attributes
links = soup.find_all('a')
for link in links:
    print(link.get('href'))