# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from scrapy.pipelines.images import ImagesPipeline
import scrapy,os
class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['url_img']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        path = '/Users/baijinxing/Documents/files'
        if results[0][0] == True:
            os.rename(path + results[0][1]['path'],path + str(item['name_img']) + ".jpg")
        return item

