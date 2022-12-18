# -*- coding: utf-8 -*-
import scrapy


class SamsungSpiderSpider(scrapy.Spider):
    name = 'samsung_Spider'
    allowed_domains = ['www.economictimes.indiatimes.com']
    start_urls = ['https://www.economictimes.indiatimes.com/']

    def parse(self, response):
        pass
