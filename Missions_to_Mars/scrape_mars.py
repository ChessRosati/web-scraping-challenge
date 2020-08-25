from splinter import Browser
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

os.chdir(os.path.dirname(__file__))


def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #Mars News
    html = browser.html
    soup = BeautifulSoup(html, 'html')
    results = soup.find('div', class_='list_text')

    latestTitle = results.find('a').text
    latestText = results.find(class_='article_teaser_body').text
    print(latestTitle)
    print(latestText)

scrape()
