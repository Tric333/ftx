#coding=utf8
__author__ = 'zyx'
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def cityurlparser(self,html_cont):
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='gb2312')
        city_urls=set()
        linklist=soup.find('div',class_="wid1000").find('div',class_='qxName').find_all('a',href=re.compile(r"/house-a\w\w\w\w/"))
        [city_urls.add(urlparse.urljoin('http://esf.xian.fang.com',city_url["href"])) for city_url in linklist]
        return city_urls


    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='gb2312')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(soup)
        city=self._get_city(soup)
        return new_urls,new_data,city

#获取分页链接
    def _get_new_urls(self,page_url,soup):
        new_urls=set()
        links=soup.find('div',class_="wid1000").find('div',class_='shangQuan').find('p',class_='contain').find_all('a',href=re.compile(r"/house-a\w+"))

        for link in links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

#获取页面内容
    def  _get_new_data(self,soup):
        res_data=[]
        nodes=soup.find('div',class_="houseList").find_all('dl',id = re.compile('list_\w+'))

        for node in nodes:
            house_data={}
            try:#小区名字
                house_name=node.find('p',class_="mt10").find('a').get('title')
                house_data['house_name']=''.join(house_name.split())
            except:
                house_data['house_name']=""

            try:#房子网址
                house_tag=node.find('p',class_="mt10").find('a').get("href")
                house_data['house_tag']=''.join(urlparse.urljoin('http://esf.xian.fang.com',house_tag))
            except:
                house_data['house_tag']=''

            try:#小区地址
                house_address=node.find('p',class_="mt10").find(class_='iconAdress ml10 gray9').get('title')
                house_data['house_address']=''.join(house_address.split())
            except:
                house_data['house_address']=""

            try:#单价
                house_unit_price=node.find('div',class_="moreInfo").find('p',class_='danjia alignR mt5').get_text()
                house_data['house_unit_price']=''.join(house_unit_price.split())
            except:
                house_data['house_unit_price']=""

            try:#面积
                house_size=node.find('div',class_="area alignR").get_text()
                house_data['house_size']=''.join(house_size.split())
            except:
                house_data['house_size']=""

            try:#总价
                house_total_price=node.find('div',class_="moreInfo").find('p',class_='mt5 alignR').get_text()
                house_data['house_total_price']=''.join(house_total_price.split())
            except:
                house_data['house_total_price']=""

            res_data.append(house_data)
        return res_data

    def _get_city(self,soup):
        house_city=soup.find('div',class_="s4Box").get_text()
        return house_city