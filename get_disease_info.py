# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:42:54 2018

@author: Administrator
"""

from selenium import webdriver
import yaml, codecs
from time import sleep


chromedriver='C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver.exe'
driver=webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get('http://www.chealth.org.cn/mon/departments_disease/article/departments_disease.html')
disease_list=driver.find_element_by_id('sc_3')
disease_list.find_element_by_link_text('肿瘤内科').click()
sleep(2)
content=[]
for i in range(14):
    frame=driver.find_element_by_id('bodyPartsListif')
    driver.switch_to_frame(frame)
    select=driver.find_element_by_tag_name('ul')
    options=select.find_elements_by_tag_name('a')
    links=[]
    for opt in options:
        href=opt.get_attribute('href')
        links.append(href)
    for link in links:
        driver2=webdriver.Chrome(chromedriver)
        driver2.maximize_window()
        driver2.get(link)
        sleep(1)
        name=driver2.find_element_by_tag_name('h1')
        alias=driver2.find_element_by_css_selector('span.alias')
        overview=driver2.find_element_by_class_name('overview')
        ps=overview.find_elements_by_tag_name('p')
        hs=overview.find_elements_by_tag_name('h4')
        line={}
        line['name']=name.text
        line['alias']=alias.text.strip()
        for h,p in zip(hs,ps):
            head=h.text
            line[head[:2]]=p.text
        if line not in content:
            content.append(line)
        driver2.quit()
    driver.switch_to_default_content()
    pagebar=driver.find_element_by_id('pagebar')
    pagebar.find_element_by_link_text('下一页').click()
    sleep(2)
stream=codecs.open('cancer_inner_info.yaml', 'w', 'utf8')
yaml.dump(content, stream)
stream.close()
driver.quit()
