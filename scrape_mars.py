#!/usr/bin/env python
# coding: utf-8

# !pip install selenium
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import tweepy
# Twitter API Keys
from config import (api_key, api_secret, access_token, access_token_secret)
import bs4 as bs
import urllib.request
import numpy as np
import pandas as pd
import selenium 



executable_path = {'executable_path': 'C:/Users/atcga/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# make a parent function called scrape and then children function for each elemtn to be caLLED

def scrape():
    # scrapedict={}
    # scrapedict["news"]=get_news()
    
    
    #make a dictiionary of all the functions and through it n the app.py
    newsdict = get_news()
    imagedict = get_images()
    tweetdict = get_tweet()
    factsdict = get_facts()
    hemidict = get_hemispheres()

        
    scrapedict = {
        "news": newsdict,
        "images": imagedict,
        "weather": tweetdict,
        "facts": factsdict,
        "hemisphere": hemidict

    # # }   
    # scrapedict= {
    #     'newsdict':get_news(),
    #     'imagedict' : get_images(),
    #     'tweetdict' : get_tweet(),
    #     'factsdict' : get_facts(),
    #     'hemidict': get_hemispheres()

    }
    return scrapedict
# to establish browser for each use


#function for news
def get_news():

    # URL of page to be scraped
    news_url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(news_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Examine the results, then determine element that contains sought info
    print(soup.prettify())

    # results are returned as an iterable list
    results = soup.find_all('div', class_="slide")

    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return title of paragragh
            news_title = result.find('div', class_="content_title").text
            # Identify paragraph
            news_p = result.find('div', class_="rollover_description_inner").text
            news={"news_title": news_title, "news_p": news_p}
            return news
        except:
            print("e")



#Function for Mars images
def get_images():

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    image_html = browser.html
    image_soup = BeautifulSoup(image_html, 'html.parser')
    image_path =image_soup.find("img", class_="thumb")["src"]
    featured_image_url="https://jpl.nasa.gov"+image_path
    return {"featured_image_url": featured_image_url}



# Mars Weather from twitter
def get_tweet():

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    target_user = "marswxreport"
    full_tweet = api.user_timeline(target_user , count = 1)
    mars_weather=full_tweet[0]['text']
    return {"mars_weather":mars_weather}

# Mars Facts
def get_facts():

    source = urllib.request.urlopen('https://space-facts.com/mars/').read()
    facts_soup = bs.BeautifulSoup(source,'lxml')
    table = facts_soup.find('table', attrs={'class':'tablepress tablepress-id-mars'})
    table_rows = table.find_all('tr')
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
    Mars_table=pd.DataFrame(l, columns=["Mar's Characteristics", "Value"])
    mars_table=Mars_table.set_index("Mar's Characteristics")

    mars_html_table = mars_table.to_html(classes='mars_html_table')
    mars_html_table=mars_html_table.replace('\n', ' ')
    

    mars_table.to_html('mars_html_table.html')
    return {"html table":"mars_html_table.html"}

# Mar's hemispheres images and links.
def get_hemispheres():

    USGS_url = 'https://astrogeology.usgs.gov/'
    browser.visit(USGS_url)
    # browser.find_link_by_partial_href('cache')
    # page_html=browser.html
    # #hemi_soup = BeautifulSoup(page_html, 'html.parser')
    return [
        {"title":"Cerberus Hemisphere Enhanced", "image_url":"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title":"Schiaparelli Hemisphere Enhanced", "image_url":"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title":"Syrtis Major Hemisphere Enhanced", "image_url":"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title":"Valles Marineris Hemisphere Enhanced", "image_url":"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
            ]

# print (scrapedict)