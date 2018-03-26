# coding=utf-8
__author__ = 'zyx'
import requests

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        html=requests.get(url)
        html=html.content.decode("gbk").encode("utf8")
        return html