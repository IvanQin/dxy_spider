# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json
import csv
from dxy.items import DxyItem
from ..conf import TO_PAGE
from ..conf import FROM_PAGE


class SpSpider(scrapy.Spider):
    name = 'sp'
    allowed_domains = ['www.dxy.cn']
    start_urls = ['http://www.dxy.cn/bbs/board/185?order=2&tpg=' + str(i) for i in range(FROM_PAGE, TO_PAGE)]

    def parse(self, response):
        # hxs = Selector(response.body)

        page = response.url[-1]
        questions = Selector(response=response).xpath('//td[@class="news"]/a').extract()

        for i in range(0, len(questions)):
            questions_text = Selector(text=questions[i]).xpath('//a/text()').extract()
            questions_link = Selector(text=questions[i]).xpath('//a/@href').extract()

            if len(questions_text) >= 1 and len(questions_link) >= 1:
                item = DxyItem()
                item['title'] = questions_text[0]
                item['link'] = questions_link[0]
                item['page'] = page
                yield item
