# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 02:40:36 2023

@author: oscah
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('E:/WORK IN PROGRESS/web scraping/Selenium/chromedriver_win32/chromedriver.exe')
driver.get('https://store.unionlosangeles.com/collections/sale')
time.sleep(20)

soup=BeautifulSoup(driver.page_source,'lxml')

product='isp_grid_product'

product_card=soup.find_all('li',class_= product)

df=pd.DataFrame({'Link':[''],'Name':[''],'letters_on':[''],'Old_price':[''],'Price':['']})
time.sleep(5)
i=1
while i<=12:
    for cloth in product_card:
        try:
            link=cloth.find('a',class_='isp_product_image_href').get('href')
            full_link='https://store.unionlosangeles.com'+link
            full_link
            #break
            name=cloth.find('div',class_='isp_product_title').text
            #name
            letters_on=cloth.find('div',class_='isp_product_vendor').text
            #letters_on   
            old_price=cloth.find('span',class_='isp_compare_at_price money').text
            #old_price
            price=cloth.find('span',class_='isp_product_price isp_compare_at_price_exist money').text
            #price
            df=df.append({'Link':full_link,'Name':name,'letters_on':letters_on,'Old_price':old_price,'Price':price},ignore_index=True)
        except:
            pass
    time.sleep(10)
    #next_page='//*[@id="isp_pagination_anchor"]/ul/li[12]'
    next_page='//*[@id="isp_pagination_anchor"]/ul/li[12]'
    #driver.find_element('xpath',next_page).click()
    button=driver.find_element('xpath',next_page)
    driver.execute_script('arguments[0].click();',button)
    time.sleep(10)
    soup=BeautifulSoup(driver.page_source,'lxml')
    product='isp_grid_product'
    product_card=soup.find_all('li',class_= product)
    i=i+1
    
    
df.to_csv('E:\WORK IN PROGRESS\web scraping\Selenium\dfunionlosangeles.csv')