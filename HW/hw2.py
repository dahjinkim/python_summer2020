"""
Class: Python 2020
Homework Assignment 2
Author: Jin Kim
"""

# import packages
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata
import sys
import os

## Make empty lists to append later
titles = []
published_date = []
issues = []
signatures = []

## We are going to scrape the first two pages of the website
pages = [1, 2]

## For loop to scrape
for i in pages:
    # open petition homepage
    web_address = "https://petitions.whitehouse.gov/?page="
    # get html code
    web_page = urllib.request.urlopen(web_address + str(i))
    # parse the code
    soup = BeautifulSoup(web_page.read())

    # get titles with tag 'h3'
    # the first three elements do not contain titles
    # so, we index from the fourth element, which is positioned at index 3
    h3 = soup.find_all('h3')
    for i in range(3, len(h3)):
        titles.append(h3[i].text)

    # go to each petition page to get published date, issues, number of signitures
    # go to each petition page
    for i in range(3, len(h3)):
        petition_page = urllib.request.urlopen("https://petitions.whitehouse.gov" + h3[i].find('a')['href'])
        petition_soup = BeautifulSoup(petition_page.read())

        # find published date under 'h4' tag with class = 'petition-attribution'
        # append it to the empty list
        published_date.append(petition_soup.find('h4', class_ = 'petition-attribution').text)

        # get issues (policy tags)
        # under tag 'div', class 'content', under tag 'h6'
        # will need to clean up later
        issues.append(petition_soup.find('div', class_ = 'content').find_all('h6'))

        # get number of signitures
        # with tag 'span' under the class 'signatures-number'
        signatures.append(petition_soup.find('span', class_ = 'signatures-number').text)

## check if we are missing any data
len(titles) == len(issues) == len(published_date) == len(signatures)


## Clean up data
# clean up issue data by extracting only the text within tag 'h6'
for i in range(0, len(issues)):
    for j in range(0, 4):
        try:
            issues[i][j] = issues[i][j].text
        except IndexError:
            continue

# clean up published dates to only include dates
dates = []
for i in published_date:
    # data structure: "Published by AA on Month, DD, YYYY"
    # split using 'on' and a white space
    # and keep only the second half
    dates.append(re.split("on\s", i)[1])
# dates

# clean up fancy double quotations in titles
for i in range(0, len(titles)):
    titles[i] = re.sub(u'\u201c', '"', titles[i])
    titles[i] = re.sub(u'\u201d', '"', titles[i])
# titles


## Export into .csv file
# change directory
os.chdir('/Users/jinki/Documents/GitHub/python_summer2020/HW')

# create .csv file
with open('hw2_Jin.csv', 'w', encoding='UTF-8', newline='') as f:
    my_writer = csv.DictWriter(f, fieldnames = ("Title", "Date", "Issue", "Signature"))
    my_writer.writeheader()
    for i in range(0, len(titles)):
        my_writer.writerow({"Title":titles[i], "Date":dates[i], "Issue": issues[i], "Signature": signatures[i]})



#### NOTES ###
# I tried so much to remove the brackets when issues got exported to csv, but failed.
# The type of issues[i] is not list, but it's a beautifulsoup resultobject,
# which made it not possible to apply .join() method.
# The fancy double quotation marks also gave me a nightmare, but I figured this one out.
