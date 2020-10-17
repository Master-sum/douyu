import scrapy
from douyu.items import DouyuItem
import json
class DouyuImgSpider(scrapy.Spider):
    name = 'douyu_img'
    allowed_domains = ['douyu.com']
    base_url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/'
    num = 1
    start_urls = [base_url + str(num)]

    def parse(self, response):
        data_list1 = json.loads(response.body)['data']
        data_list = data_list1['rl']
        print(data_list)
        if len(data_list) == 0:
            return
        for data in data_list:
            item = DouyuItem()
            item['name_img'] = data['nn']
            item['url_img'] = data['rs1']
            yield item
        self.num += 1
        url = self.base_url + str(self.num)
        yield scrapy.Request(url,callback=self.parse,dont_filter=True)