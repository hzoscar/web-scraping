# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:17:24 2023

@author: oscah
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('E:/WORK IN PROGRESS/web scraping/Selenium/chromedriver_win32/chromedriver.exe')
driver.get('https://www.goat.com/sneakers')

last_height=driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(12)
    new_height=driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height=new_height

product= 'GridStyles__GridCellWrapper-sc-1cm482p-0 biZBPm'

soup=BeautifulSoup(driver.page_source,'lxml')

product_card=soup.find_all('div',class_= product)

df=pd.DataFrame({'Link':[''],'Name':[''],'Released_data':[''],'price':['']})

for snaker in product_card:
    try:        
        link=snaker.find('a',class_='GridCellLink__Link-sc-2zm517-0 dcMqZE').get('href')
        #link
        name=snaker.find('div',class_='GridCellProductInfo__Name-sc-17lfnu8-3 hfCoWX').text
        #name
        released_data=snaker.find('div',class_='GridCellProductInfo__Year-sc-17lfnu8-2 jJQboW').text
        #released_data
        price=snaker.find('div',class_='GridCellProductInfo__Price-sc-17lfnu8-6 gsZMPb').text
        #price
        df=df.append({'Link':link,'Name':name,'Released_data':released_data,'price':price},ignore_index=True)
    except:
        pass
df.to_csv('E:\WORK IN PROGRESS\web scraping\Selenium\dfcoat.csv')
