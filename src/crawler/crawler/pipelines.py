# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def __init__(self):
        self.file = open('store.json','w')
    def process_item(self, item, spider):
        wenjian = json.dumps(item,ensure_ascii=False) + ',\n'
        self.file.write(wenjian)
        #print('itcase: ', item)
        return item
    def __del__(self):
        self.file.close()