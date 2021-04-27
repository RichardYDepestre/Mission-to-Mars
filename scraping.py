# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', headless=True, **executable_path)
    return browser


def scrape_all():
    browser = init_browser()
    news_title, news_paragraph = mars_news(browser)
    # mars_facts = mars_facts()
    # print(mars_data)
    # Run all scraping functions and store results in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "mars_hemispheres": get_mars_hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return mars_data


def mars_news(browser):
    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find(
            'div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    #  full_image_elem = browser.find_by_tag('a', class_="btn-primary")
    full_image_elem
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}"
    # img_url = f"https://spaceimages-mars.com/image/featured/mars3.jpg"
    return img_url


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html(
            'https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns = ['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    df
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()
    # return df.to_html(classes="table table-striped")


def get_mars_hemispheres(browser):
    hemisphere_image_urls = list()  # dict. entries container
    # Cerberus
    url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
    browser.visit(url)

    start_obj = browser.find_by_xpath(
        '//*[@id="product-section"]/div[2]/div[1]/a/img').click()
    next_obj = browser.find_by_xpath('//*[@id="wide-image-toggle"]').click()
    # scrape new screen html
    img_html = browser.html
    img_soup = soup(img_html, 'html.parser')
    img = browser.find_by_xpath('//*[@id="wide-image"]/div/ul/li[1]/a').text
    img_title = browser.find_by_xpath(
        '//*[@id="results"]/div[1]/div/div[3]/h2').first.text
    img_url = browser.find_by_xpath('//*[@id="wide-image"]/img')
    # print(img_title)
    # print(img_url['src'])
    dict_entry = {"image title": img_title, "image url": img_url['src']}
    hemisphere_image_urls.append(dict_entry)
    # print(hemisphere_image_urls)
    browser.back()

    # Schiaparelli
    url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
    browser.visit(url)

    start_obj = browser.find_by_xpath(
        '//*[@id="product-section"]/div[2]/div[2]/a/img').click()
    next_obj = browser.find_by_xpath('//*[@id="wide-image-toggle"]').click()
    # scrape new screen html
    img_html = browser.html
    img_soup = soup(img_html, 'html.parser')
    img = browser.find_by_xpath('//*[@id="wide-image"]/div/ul/li[1]/a').text
    img_title = browser.find_by_xpath(
        '//*[@id="results"]/div[1]/div/div[3]/h2').first.text
    img_url = browser.find_by_xpath('//*[@id="wide-image"]/img')
    # print(img_title)
    # print(img_url['src'])
    dict_entry = {"image title": img_title, "image url": img_url['src']}
    hemisphere_image_urls.append(dict_entry)
    # print(hemisphere_image_urls)
    browser.back()

    # Syrtis
    url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
    browser.visit(url)

    start_obj = browser.find_by_xpath(
        '//*[@id="product-section"]/div[2]/div[3]/a/img').click()
    next_obj = browser.find_by_xpath('//*[@id="wide-image-toggle"]').click()
    # scrape new screen html
    img_html = browser.html
    img_soup = soup(img_html, 'html.parser')
    img = browser.find_by_xpath('//*[@id="wide-image"]/div/ul/li[1]/a').text
    img_title = browser.find_by_xpath(
        '//*[@id="results"]/div[1]/div/div[3]/h2').first.text
    img_url = browser.find_by_xpath('//*[@id="wide-image"]/img')
    # print(img_title)
    # print(img_url['src'])
    dict_entry = {"image title": img_title, "image url": img_url['src']}
    hemisphere_image_urls.append(dict_entry)
    # print(hemisphere_image_urls)
    browser.back()

    # Valles
    url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
    browser.visit(url)

    start_obj = browser.find_by_xpath(
        '//*[@id="product-section"]/div[2]/div[4]/a/img').click()
    next_obj = browser.find_by_xpath('//*[@id="wide-image-toggle"]').click()
    # scrape new screen html
    img_html = browser.html
    img_soup = soup(img_html, 'html.parser')
    img = browser.find_by_xpath('//*[@id="wide-image"]/div/ul/li[1]/a').text
    img_title = browser.find_by_xpath(
        '//*[@id="results"]/div[1]/div/div[3]/h2').first.text
    img_url = browser.find_by_xpath('//*[@id="wide-image"]/img')
    # print(img_title)
    # print(img_url['src'])
    dict_entry = {"image title": img_title, "image url": img_url['src']}
    hemisphere_image_urls.append(dict_entry)
    # print(hemisphere_image_urls)
    browser.back()
    return hemisphere_image_urls

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
