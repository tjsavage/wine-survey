# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy, urllib, mimetypes
from scrapy_djangoitem import DjangoItem

from survey.models import WineItem

class WineWineItem(DjangoItem):
    django_model = WineItem
    

class WincWineItem(DjangoItem):
    django_model = WineItem
    product_id = scrapy.Field()
    wine_id = scrapy.Field()

    PRODUCT_FIELD_MAPPINGS = {
        ('product_id', 'productId'),
        ('wine_id', 'wineId'),
        ('name', 'name'),
        ('description', 'blurb'),
        ('story', 'description'),
        ('origin', 'origin'),
        ('winc_product_id', 'productId'),
        ('winc_product_code', 'productCode')
    }

    SEARCH_RESULT_FIELD_MAPPINGS = {
        ('region', 'originRegion'),
        ('country', 'originCountry'),
        ('vintage', 'vintage')
    }


    # Returns a populated item based on the JSON
    # response coming from https://www.winc.com/api/products/{product_Id}
    def populate_from_product_json(self, product_json):
        for mapping in self.PRODUCT_FIELD_MAPPINGS:
            if mapping[1] in product_json:
                self[mapping[0]] = product_json[mapping[1]]
        
        self['price'] = product_json['pricing']['retail']
        if product_json['pricing']['retail'] != product_json['pricing']['member']:
            self['sale_price'] = product_json['pricing']['member']


        if not product_json['varietal'] or product_json['varietal'] == 'NA':
            self['varietal'] = None
        else:
            self['varietal'] = product_json['varietal']

        self['bottle_image_url'] = 'https://d207gb2bfvg73.cloudfront.net/%s/hero@2x.jpg' % product_json['productCode']

        if product_json['ratings']:
            self['user_rating'] = product_json['ratings']['average']

    def populate_from_search_result_json(self, search_result_json):
        for mapping in self.SEARCH_RESULT_FIELD_MAPPINGS:
            if mapping[1] in search_result_json:
                self[mapping[0]] = search_result_json[mapping[1]]
    
        if 'screwcap' in search_result_json['closure']:
            self['closure_type'] = 'SC'
        else:
            self['closure_type'] = 'CO'

        if search_result_json['rose'] != '':
            self['wine_type'] = 'Ro'
        elif search_result_json['sparkling'] != '':
            self['wine_type'] = 'S'
        elif search_result_json['wineType'] == 'white':
            self['wine_type'] = 'W'
        elif search_result_json['wineType'] == 'red':
            self['wine_type'] = 'R'
        
        self['item_key'] = 'winc%s' % self['product_id']