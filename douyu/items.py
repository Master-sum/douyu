# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:

    #图片名字
    name_img = scrapy.Field()
    #图片连接
    url_img= scrapy.Field()

