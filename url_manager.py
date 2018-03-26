#coding=utf8
__author__ = 'zyx'

class UrlManager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
        self.false_urls=[]

def add_new_url(self, url):
    if url is None:
        return
    if url not in self.new_urls and url not in self.old_urls:
        self.new_urls.add(url)


def add_new_urls(self, urls):
    if urls is None or len(urls)==0:
        return
    for url in urls:
        self.add_new_url(url)

def has_new_url(self):
    return len(self.new_urls)!=0

    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

#将解析失败的URL重新放入url列表进行解析
    def add_false_url(self,url):
#如果一个URL被反复循环爬取多次失败，就放弃该url
        if url is None or self.false_urls.count(url)>4:
            return
        self.false_urls.append(url)
        self.old_urls.remove(url)
        self.add_new_url(url)

#每爬取完一个城市，清空old_url和false_urls列表
    def release_urllist(self):
        if len(self.new_urls)==0:
            self.old_urls.clear()
            self.false_urls=[]