# -*- encoding:utf-8 -*-

import scrapy
from lianjia.items import LianjiaItem

class Lianjiaspider(scrapy.spiders.Spider):
    name = "lianjiaspider"
    local = {'dongcheng':'35','xicheng':'55','chaoyang':'100','haidian':'100','fengtai':'65','shijingshan':'20','tongzhou':'31','changping':'40','daxing':'24','yizhuangkaifaqu':'8','shunyi':'22','fangshan':'9','mentougou':'5','pinggu':'1','huairou':'1','miyun':'1','yanqing':'1'}
    start_urls = []
    for k in local.keys():
        for i in range(1,int(local[k])+1):
            url = 'https://bj.lianjia.com/zufang/'+k+'/pg' + str(i) + '/'
            start_urls.append(url)
    allowed_domains = ["linajia.com"]

    def parse(self, response):
        item = LianjiaItem()
        for i in range(1, 31):
            title = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/h2/a/text()').extract()[0]
            url = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/h2/a/@href').extract()[0]
            name = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/div[1]/div[1]/a/span/text()').extract()[0]
            pattern1 = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/div[1]/div[1]/span[1]/span/text()').extract()[0]
            pattern2 = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/div[1]/div[1]/span[2]/text()').extract()[0]
            pattern = pattern1 + pattern2
            direction = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/div[1]/div[1]/span[3]/text()').extract()[0]
            location = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/div[1]/div[2]/div/a/text()').extract()[0]
            try:
                year = response.xpath('//*[@id="house-lst"]/li['+str(i)+']/div[2]/div[1]/div[2]/div/text()[2]').extract()[0]
            except:
                year = ""
            finally:
                item['name'] = name
                item['title'] = title
                item['pattern'] = pattern
                item['direction'] = direction
                item['url'] = url
                item['location'] = location
                item['year'] = year
                yield item
