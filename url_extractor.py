from bs4 import BeautifulSoup
import requests

url = "https://www.webscraper.io/test-sites/e-commerce/allinone"

response = requests.get(url)
print(response)         # <Response [200]> if it was a successfull request.

source_code = response.text
# print(source_code)

data = BeautifulSoup(source_code, 'html.parser')
# print(data)

# finding html tags
# a tags
tags = data.find_all('a')
# print(tags)         # returns all the anchor tags

# find links in page.

for tag in tags:
    print(tag.get('href'))              # prints all the links in the page.
