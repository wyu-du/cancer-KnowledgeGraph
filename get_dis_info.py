# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:48:03 2018

@author: Administrator
"""

from selenium import webdriver
from time import sleep
import pandas as pd

df=pd.read_csv('data/edge_cancer.csv', encoding='utf8')
dis=list(df['Source'])
dis=list(set(dis))

chromedriver='C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver.exe'
driver=webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get('http://www.chealth.org.cn/mon/departments_disease/article/departments_disease.html')
clean_links={}
content=[]
for d in dis:
    d_links={}
    driver.find_element_by_id('searchText').clear()
    driver.find_element_by_id('searchText').send_keys(d)
    sleep(1)
    driver.find_element_by_class_name('btn').click()
    sleep(2)
    try:
        searchleftbox=driver.find_element_by_id('searchFacetFieldShow')
        sleep(2)
        searchleftbox.find_element_by_partial_link_text('疾病').click()
    except:
        continue
    else:
        sleep(4)
        searchlist=driver.find_element_by_id('searchlistContent')
        links=searchlist.find_elements_by_xpath('//div[@class="Searchlist"]/h3')
        for link in links:
            href=link.find_element_by_tag_name('a').get_attribute('href')
            href=href.split("'")[1]
            text=link.find_element_by_tag_name('a').text
            d_links[text]=href
    clean_links[d]=d_links
driver.quit()

for d, d_dict in clean_links.items():
    for d_out, d_link in d_dict.items():
        driver2=webdriver.Chrome(chromedriver)
        driver2.maximize_window()
        driver2.get(d_link)
        sleep(1)
        name=driver2.find_element_by_tag_name('h1')
        alias=driver2.find_element_by_css_selector('span.alias')
        overview=driver2.find_element_by_class_name('overview')
        ps=overview.find_elements_by_tag_name('p')
        hs=overview.find_elements_by_tag_name('h4')
        line={}
        line['disease_in']=d
        line['disease_out']=d_out
        line['disease_in_related']=list(df[df['Source']==d]['Target'])
        line['disease_out_alias']=alias.text.strip()
        for h,p in zip(hs,ps):
            head=h.text
            line[head[:2]]=p.text
        if line not in content:
            content.append(line)
        driver2.quit()

df=pd.DataFrame(content)
df.to_csv('data/cancer_info_disease.csv', index=False, encoding='utf8')
