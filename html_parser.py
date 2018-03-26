#coding=utf8
__author__ = 'zyx'
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def cityurlparser(self,html_cont):
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf8')
        city_urls=set()
        linklist=soup.find('div',class_="city20141104").find_all('a',href=True)
        [city_urls.add(city_url["href"]+"b81-b91/") for city_url in linklist]
        return city_urls


def parse(self,page_url,html_cont):
    if page_url is None or html_cont is None:
        return

    soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf8')
    new_urls=self._get_new_urls(page_url,soup)
    new_data=self._get_new_data(soup)
    city=self._get_city(soup)
    return new_urls,new_data,city

#获取分页链接
    def _get_new_urls(self,page_url,soup):
        new_urls=set()
        links=soup.find('div',class_="page").find_all('a',href=re.compile(r"/house/s/b81-\w+"))
    for link in links:
        new_url=link['href']
        new_full_url=urlparse.urljoin(page_url,new_url)
        new_urls.add(new_full_url)
    return new_urls

#获取页面内容
    def  _get_new_data(self,soup):
        res_data=[]
        nodes=soup.find_all('div',class_="nlc_details")
        for node in nodes:
            house_data={}
            house_name=node.find('div',class_="nlcd_name").get_text()
            house_data['house_name']=''.join(house_name.split())
            house_tag=node.find('div',class_="nlcd_name").find('a',href=True).get("href")
            house_data['house_tag']=''.join(house_tag.split())

            try:
                house_address=node.find('div',class_="address").get_text()
                house_data['house_address']=''.join(house_address.split())
            except:
                house_data['house_address']=""

            try:
                house_price=node.find('div',class_="nhouse_price").get_text()
                house_data['house_price']=''.join(house_price.split())
            except:
                house_data['house_price']=""
            res_data.append(house_data)
    return res_data

def _get_city(self,soup):
    house_city=soup.find('div',class_="s4Box").get_text()
    return house_city