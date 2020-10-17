"""
作者   ：bjx
创建时间   ：2020/10/17  11:43 上午 
文件名称   ：运行文件.PY
开发工具   ：PyCharm
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl douyu_img".split())