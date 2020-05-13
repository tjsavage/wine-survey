import scrapy
import json

from ..items import WincWineItem, WineWineItem
from ..util import is_image_url_valid

class WineSpider(scrapy.Spider):
    name = "wine"
    start_urls = [
        'https://www.wine.com/list/list-customer-favorites/wine/1028-7155',
        'https://www.wine.com/list/list-customer-favorites/wine/1028-7155/2',
        'https://www.wine.com/list/list-customer-favorites/wine/1028-7155/3',
        'https://www.wine.com/list/list-customer-favorites/wine/1028-7155/4',
        'https://www.wine.com/list/list-customer-favorites/wine/1028-7155/5'
    ]

    SELECTOR_MAPPING = [
        ('wine_product_id', 'meta[name=productID]::attr(content)'),
        ('name', '.pipName::text'),
        ('description', '.viewMoreModule_text p::text'),
        ('story', '.viewMoreModule_text p::text'),
        ('origin', '.pipOrigin_link::text'),
        ('region', 'meta[name=productRegion]::attr(content)'),
        ('country', 'originCountry'),
        ('varietal','meta[name=productVarietal]::attr(content)'),
        ('price','meta[name=productPrice]::attr(content)'),
        ('bottle_image_url','.pipThumb_img-1::attr(src)')
    ]
    
    def parse(self, response):

        product_list = response.css('li.prodItem')
    
        for product in product_list:
            product_page_url = product.css('.prodItemImage_link::attr(href)').get()

            yield scrapy.Request('https://www.wine.com%s' % product_page_url, callback=self.parse_product_page)

    def parse_product_page(self, response):
        item = WineWineItem()
        
        for mapping in self.SELECTOR_MAPPING:
            item[mapping[0]] = response.css(mapping[1]).get()

        item['bottle_image_url'] = 'https://www.wine.com%s' % item['bottle_image_url']
        item['bottle_image_url'] = item['bottle_image_url'].replace('w_75,h_75','w_480,h_600')

        item['price'] = item['price'].replace('$','')

        if not is_image_url_valid(item['bottle_image_url']):
            print("Invalid image url: %s" % item['bottle_image_url'])

            return None
        
        item['item_key'] = 'wine%s' % item['wine_product_id']

        

        item.save()

        return item