## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
##  -Specialization
##    Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##    Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence.
##  -Name
##  -Title
##  -E-mail
##  -Web page

from bs4 import BeautifulSoup
import urllib.request
import csv
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys


web_address = 'https://polisci.wustl.edu/people/88/all'
web_page = urllib.request.urlopen(web_address)
web_page

soup = BeautifulSoup(web_page.read())
all_a_tags = soup.find_all('a')
len(all_a_tags)

l = {"class" : [], "href" : []} # create a dictionary
for p in range(0,60):
    try:
        # extract all attrs 'class' from the all_a_tags
        l["class"].append(all_a_tags[p].attrs["class"])
        # extract all attrs 'href' from the all_a_tags
        l["href"].append(all_a_tags[p].attrs["href"])
    except KeyError:
        continue

prof_website = l["href"]
prof_website = prof_website[11:35]
print(prof_website)


prof_website_links = []

for i in range(0, len(prof_website)):
  try:
    prof_website_links.append('https://polisci.wustl.edu' + str(prof_website[i]))
  except KeyError:
    continue

del prof_website_links[8]

print(prof_website_links)

# web_address = 'https://polisci.wustl.edu/people/88/list/88/all'

name = []
title = []
personal_webpage = []
email = []
interest = []

# run the function for the first 2 cases
for i in range(0, 2):
  driver = start_chrome(prof_website_links[i], silent = True)
  html = driver.page_source
  driver.close()
  soup = BeautifulSoup(html)
  name.append(soup.find(class_ = 'inner').find('h1').text)

  #soup = soup.find(class_ = 'inner').find('div', class_ = 'person')
  #party.append(soup.find(class_ = 'office').find_all('li')[1].text)
  email.append(soup.find(class_ = 'contactinfo first notexternal').find('a', href = True)['href'].split(":")[1])
