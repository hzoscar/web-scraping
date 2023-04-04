# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:43:20 2023

@author: oscah

python file to scrape an e-comerce website to get the information about computers with certain features.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://listado.mercadolibre.com.co/computacion/portatiles-accesorios/portatiles/nuevo/10-a-20-GB/mas-de-512-GB-capacidad-del-ssd/laptop_PriceRange_2500000-5000000_NoIndex_True#applied_filter_id%3DSSD_DATA_STORAGE_CAPACITY%26applied_filter_name%3DCapacidad+del+SSD%26applied_filter_order%3D12%26applied_value_id%3D%5B512GB-*%29%26applied_value_name%3D512+GB+o+m%C3%A1s%26applied_value_order%3D2%26applied_value_results%3D73%26is_custom%3Dfalse'
url1='https://listado.mercadolibre.com.co/computacion/portatiles-accesorios/portatiles/nuevo/10-a-20-GB/mas-de-512-GB-capacidad-del-ssd/laptop_Desde_51_PriceRange_2500000-5000000_NoIndex_True'
url2='https://listado.mercadolibre.com.co/computacion/portatiles-accesorios/portatiles/nuevo/10-a-20-GB/mas-de-512-GB-capacidad-del-ssd/laptop_Desde_101_PriceRange_2500000-5000000_NoIndex_True'

urls=[url,url1,url2]

page=requests.get(url)
page
soup = BeautifulSoup(page.text,'lxml')
soup
df=pd.DataFrame({})

for i in urls:
    
    page=requests.get(i)
    soup = BeautifulSoup(page.text,'lxml')    
    computers = soup.find_all('li',class_='ui-search-layout__item shops__layout-item')
    
    for computer in computers:
        
        link = computer.find('a',class_= 'ui-search-item__group__element shops__items-group-details ui-search-link').get('href') 
        name= computer.find('h2',class_='ui-search-item__title shops__item-title').text
        price=computer.find('span',class_='price-tag-text-sr-only').text 
        price_True=computer.find('div',class_='ui-search-price__second-line shops__price-second-line').text
    
        
        df=df.append({'Links':link,'Name':name,'Price':price,'Price_true':price_True},ignore_index=True)
        
df.to_csv('E:/WORK IN PROGRESS/web scraping/project 2 mercado libre computers/raw file computers.csv')
