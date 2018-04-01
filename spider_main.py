# coding=utf-8
__author__ = 'zyx'

import url_manager,html_downloader,html_parser,html_outputer
from print_manage import *

import time
import traceback

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()#管理URL
        self.downloader=html_downloader.HtmlDownloader()#下载URL内容
        self.parser=html_parser.HtmlParser()#解析URL内容
        self.outputer=html_outputer.HtmlOutputer()#输出获取到的内容

    #获取待爬取城市链接
    def District_Crwa(self,root_url):
        html_cont=self.downloader.download(root_url)
        district_urls=self.parser.district(html_cont)
        return district_urls

    def Business_District_Crwa(self,root_url):
        print_info('开始下载 {}'.format(root_url))
        html_cont=self.downloader.download(root_url)
        print_info('开始解析 {} '.format(root_url))
        business_district_urls = self.parser.business_district_parser(html_cont)
        return business_district_urls

#爬虫主体程序
    def crwa(self,district,business,city_url):
        count=0
        self.urls.add_new_url(city_url)#将根链接首先放入page页urllist
        while self.urls.has_new_url():
            count=count+1
            try:
                new_url=self.urls.get_new_url()#获取新的链接
                print_info ('{}{}第{}个网页【{}】开始处理--------------'.format(district,business,count,new_url))
                html_cont=self.downloader.download(new_url)#下载页面内容
                new_urls, new_data ,house_city= self.parser.parse(new_url, html_cont)#解析页面内容
                self.urls.add_new_urls(new_urls)
                self.outputer.output_excel(new_data,house_city,district,business)#写入excel
                #self.outputer.output_mysql(new_data,house_city)#写入mysql
                print_info ('{}{}第{}个网页【{}】输出成功--------------'.format(district,business,count,new_url))
            except Exception as e:
                print_dbg(e)
                print_dbg(traceback.print_exc())
                self.urls.add_false_url(new_url)#如果解析失败，则将url放入失败列表
                print_info ('{}{}第{}个网页【{}】爬取失败，舍弃'.format(district,business,count,new_url))
                time.sleep(2)
                count=count-1

        self.urls.release_urllist()#解析并输出完一个城市后，释放page页urllist

if __name__=="__main__":
    obj_spider=SpiderMain()
    root_url="http://esf.xian.fang.com/"
    district_urls=obj_spider.District_Crwa(root_url)

    for district, url in district_urls.items() :
        district_urls[district] = obj_spider.Business_District_Crwa(url)
        print(district_urls[district])

    for district,business_dict in district_urls.items():
        for business,url in business_dict.items():
            obj_spider.crwa(district,business,url)
