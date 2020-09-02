from bs4 import BeautifulSoup
import urllib.request

web_address = "https://petitions.whitehouse.gov/petitions"
web_page = urllib.request.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
print(soup.prettify())
