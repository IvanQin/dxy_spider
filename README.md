# dxy_spider

## 介绍
一个丁香园的爬虫，适用网页http://www.dxy.cn/bbs/board/185 。
爬取制定页面帖子中的问题和对应的链接，并存放到 /dxy/result/ 中，以csv格式存放数据。


## 依赖package 
scrapy

安装方式：pip install scrapy


## 设置爬取页面
更改 /dxy/conf.py 中的 FROM_PAGE 和 TO_PAGE，并保存.


## 运行方式
进入根目录/ ，打开terminal或者cmd，运行 
scrapy crawl sp


