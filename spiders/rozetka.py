# -*- coding: utf-8 -*-
import scrapy


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua/mobile-phones/c80003/']
    start_urls = ['http://rozetka.com.ua/mobile-phones/c80003//']
    custom_settings = {
            'FEED_URI' : 'tmp/rozetka.csv'
    }


    def parse(self, response):
        titles = response.css('img::attr(title)').extract()
        images = response.css('img::attr(src)').extract()
        for item in zip(titles,images):
            scraped_info = {
                    'title' : item[0],
                    'image' : [item[1]]
            }

            yield scraped_info
