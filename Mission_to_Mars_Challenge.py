#!/usr/bin/env python
# coding: utf-8

# In[51]:


# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[52]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[53]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[54]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[55]:


slide_elem.find('div', class_='content_title')


# In[56]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[57]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[58]:


# ### Featured Image


# In[59]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[60]:


# Find and click the full image button
full_image_elem = browser.find_by_tag("button")[1]
full_image_elem.click()


# In[61]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[62]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[64]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[65]:


# ### Mars Facts


# In[66]:


#create dataframe from html table
df = pd.read_html('https://galaxyfacts-mars.com')[0]

#assign columns
df.columns=['description', 'Mars', 'Earth']

#set Description Column as index
df.set_index('description', inplace=True)
df


# In[67]:


#convert table to a html object 
df.to_html()


# In[68]:


#end the auto browser session
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




