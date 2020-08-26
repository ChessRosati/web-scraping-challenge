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

    #JPL Mars Space Images - Featured Image
    JPLurl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(JPLurl)
    html = browser.html
    soup = BeautifulSoup(html, 'html')

    picURL = soup.find('a', class_= "button fancybox")["data-fancybox-href"]
    picURL = "https://www.jpl.nasa.gov" + picURL

    # Mars Facts
    factsURL = 'https://space-facts.com/mars/'
    tables = pd.read_html(factsURL)
    df = tables[0]
    df

    facts = df.to_html()

    # Mars Hemispheres
    hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemiURL)
    html = browser.html
    soup = BeautifulSoup(html, 'html')

    scrape = soup.find_all('div', class_='item')
    hemiPics = []

    for x in scrape:
        hemiDict = {}
        result = x.find('div', class_='description').find('a').text
        hemiDict['title'] = result

        link = x.find('div', class_='description').find('a')["href"]
        link = "https://astrogeology.usgs.gov/" + link
    
        browser.visit(link)
        hemitml = browser.html
        hemiSoup = BeautifulSoup(hemitml, 'html')
    
        pic = hemiSoup.find('div', class_='content').find('a')['href']
        hemiDict['img_url'] = pic
        hemiPics.append(hemiDict)
        browser.visit(hemiURL)

    browser.quit()

    data = {"latestTitle" : latestTitle,
        "latestText" : latestText,
        "marsImages" : picURL,
        "marsTable" : facts,
        'hemisphereImages' : hemiPics}
    return data
scrape()
