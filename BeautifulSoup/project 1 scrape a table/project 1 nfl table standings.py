# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 
@author: oscah

First project: Scrape a table from a web site by using beautifulsoup
    - The table was the current (mar 26) standigs of the NFL league. 
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2022/REG'

page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

table = soup.find('table',class_="d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")
table

headers = table.find_all('th')
headers

headers_list=[]
for header in headers:
    i=header.text
    headers_list.append(i)
    
df=pd.DataFrame(columns=headers_list)

for j in table.find_all('tr')[1:]:
    
    first = j.find_all('td')[0].find('div',class_='d3-o-club-fullname').text
    row_data = j.find_all('td')[1:]
    row=[td.text for td in row_data]
    row.insert(0,first)
    length=len(df)
    df.loc[length]=row
 

df.to_csv('E:/WORK IN PROGRESS/web scraping/orject1_nfl_table_scraped.csv')

    
    