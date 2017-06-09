# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
import time
import os
from .spiders import sp


class DxyPipeline(object):
    store_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result')

    def __init__(self):
        _filename = time.strftime('%Y-%m-%d %H-%M-%S',
                                  time.localtime(time.time())) + ' Page_' + str(sp.FROM_PAGE) + '-' + str(
            sp.TO_PAGE) + '.csv'
        self.store_path = os.path.join(self.store_path, _filename)
        self.file = open(self.store_path, 'w+', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['标题', '链接', '页号'])

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        page = item['page']
        if item['link'] != 'javascript:;':
            self.writer.writerow([title, link, page])
        return item
