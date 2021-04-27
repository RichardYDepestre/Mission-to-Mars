# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# %%
def get_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def close_browser():
    browser.quit()

# %% [markdown]
# ### Featured Images


# %%
browser = get_browser()
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# %%
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
#
slide_elem.find('div', class_='content_title')
#
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %% [markdown]
# #### 10.3.4 Scrape Mars Data: **Featured Images**

# %%
# Visit URL
browser = get_browser()
url = 'https://spaceimages-mars.com'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com{img_url_rel}'
img_url

# %% [markdown]
# #### 10.3.5 Scrape Mars Data: Mars Facts

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df
df.to_html()

# %% [markdown]
# #### close browser

# %%
close_browser()


# %%
# Import splinter, BeautifulSoup, and Pandas


# %%
# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# %%
# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# %%
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# %%
slide_elem.find('div', class_='content_title')


# %%
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %% [markdown]
# ### JPL Space Images Featured Image

# %%
# Visit URL
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
hemisphere_image_urls = []  # list to hold dictionary
hemispheres = {}  # dict to hold url and title

browser.visit(url)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)  # populate list
    browser.back()  # navigate back


# %%
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# %%
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# %%
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# %%
# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url

# %% [markdown]
# ### Mars Facts

# %%
df = pd.read_html(
    'https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.head()


# %%
df.columns = ['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

# %% [markdown]
# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# %% [markdown]
# ### Hemispheres

# %%
# 1. Use browser to visit the URL
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)


# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# %%
# 5. Quit the browser
browser.quit()


# %%
