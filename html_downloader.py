# coding=utf-8
__author__ = 'zyx'
import requests

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        count = 0;
        while count <10:
            try:
                html=requests.get(url,timeout = count+1)
                html=html.content.decode("gbk").encode("utf8")
                break
            except:
                print('获取 {} 失败 , 开始第 {} 次重试'.format(url,count+1))
                count += 1
        return html