import scrapy
import json

from ..items import WincWineItem
from ..util import is_image_url_valid

class WincSpider(scrapy.Spider):
    name = "winc"
    start_urls = [
        'https://www.winc.com/api/search?index=winesearch-production-4&top=100'
    ]
    
    def parse(self, response):
        response_json = json.loads(response.body_as_unicode())
        results = response_json['search']

        for search_result_json in results:
            yield scrapy.Request('https://www.winc.com/api/products/%s' % search_result_json['product_Id'], callback=self.parse_product, cb_kwargs={'search_result_json': search_result_json})

    def parse_product(self, response, search_result_json):
        product_json = json.loads(response.body_as_unicode())

        item = WincWineItem()
        item.populate_from_product_json(product_json)
        item.populate_from_search_result_json(search_result_json)

        if not is_image_url_valid(item['bottle_image_url']):
            print("Invalid image url: %s" % item['bottle_image_url'])

            return None

        item.save()

        return item

    def parse_wine(self, response):
        pass