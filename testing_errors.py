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

#def scrape()::

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

        # Identify and return title of paragragh
        news_title = result.find('div', class_="content_title").text
        # Identify paragraph
        news_p = result.find('div', class_="rollover_description_inner").text
        news= {"news_title": news_title, "news_p": news_p}
    print (news)

