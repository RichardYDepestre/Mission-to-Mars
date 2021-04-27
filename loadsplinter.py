from splinter import Browser
from bs4 import BeautifulSoup as soup
import requests
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import datetime as dt

# Setup splinter


def init_splinter(url):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    return browser


def init_splinter_x():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    return browser


def get_web_content(browser):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    return soup
