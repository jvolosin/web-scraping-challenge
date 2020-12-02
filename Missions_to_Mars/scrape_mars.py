#!/usr/bin/env python
# coding: utf-8

# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd 
from selenium import webdriver
from flask_pymongo import PyMongo


# In[3]:


# Setup splinter
def init_browser():
    executable_path = {"executable_path": "/Users/jvolo/Bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# In[4]:


#Scrape NASA Mars News Site for latest news Title
#Scrape NASA Mars News Site for latest news Paragraph
#Add scrape function

def scrape():

    browser = init_browser()
    listings = {}
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text



# In[5]:


#Display Results
    print(news_title)
    print(news_p)


# In[6]:


#JPL
#Use splinter to navigate the site and find the image url 
#For the current Featured Mars Image and assign the url string to a variable called `featured_image_url`
#Make sure to find the image url to the full size `.jpg` image.
#Make sure to save a complete url string for this image.
# Add scrape function

def scrape():

    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17474_ip.jpg" 

    browser.visit(featured_image_url)

    html = browser.html
    featured_image_soup = BeautifulSoup(html, "html.parser")
    print(featured_image_url)


# In[7]:


#Mars Facts
#Add scrape function

def scrape():

    mars_facts_url = "https://space-facts.com/mars/"


# In[8]:


#Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    tables = pd.read_html(mars_facts_url)
    tables


# In[9]:


#Scrape table for facts

    mars_facts_df = tables[2]
    mars_facts_df


# In[10]:


#Use Pandas to convert the data to a HTML table string.
    html_table = mars_facts_df.to_html()
    html_table


# In[11]:


#USGS Astrogeology
#Obtain high resolution images for each of Mar's hemispheres
#Click each of the links to the hemispheres in order to find the image url to the full resolution image.
#Add scrape function

def scrape():

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    usgs_html = browser.html
    soup = BeautifulSoup(usgs_html, "html.parser")


# In[33]:


# Loop through data to find full resolution image URLs

    hemisphere_image_urls = []
    results = soup.find_all('div', class_='downloads')


    for result in results:
        hemisphere = result.find('div', class_="description")
        title = hemisphere("h3").text
    
        images_html = browser.html
        oup = BeautifulSoup(images_html, 'html.parser')
        image_link = soup.find('div', class_='downloads')
        images_urls = image_link.find("a")["href"]
    

    #Use a Python dictionary to store the data using the keys `img_url` and `title`.
        images_dict = {}
        images_dict['title'] = title
        images_dict['img_url'] = images_url
    
#Append the dictionary with the image url string and the hemisphere title to a list
#This list will contain one dictionary for each hemisphere.
        hemisphere_image_urls.append(images_dict)

    hemisphere_image_urls   
    

