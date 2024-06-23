# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class WebscrapescrapyPipeline:
    def process_item(self, item, spider):
        if 'name' in item:
            if 'Data' in item['name']:
                print('pipeline executed')
                return item
            else:
                print('no data found in item')
                raise DropItem('item does not contain data keyword')
        else:
            print('no name in item')
            raise DropItem('item doesnt contain data')
        
