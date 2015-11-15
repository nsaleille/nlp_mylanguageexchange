import scrapy
from mylanguageexchange_crawler.items import mylanguageexchangeItem
import json
from scrapy.utils.serialize import ScrapyJSONEncoder

class MylanguageexchangeSpider(scrapy.Spider):
    name = "mylanguageexchange"
    allowed_domains = ["mylanguageexchange.com"]
    start_urls = [
        "http://www.mylanguageexchange.com/Search-Pen-pals.asp?selX3=22"
    ]

    def parse(self, response):

        items = []
        for row in response.xpath('//table[@class="TblDataRecs"]/tr'):
            item = mylanguageexchangeItem()
            name = row.xpath('td[@class="userdata"]//a//b/text()').extract()
            item["name"] = [x.strip() for x in name]
            country = row.xpath('td[@class="userdata"][@data-th="Country(City)"]//tr[1]/td/text()').extract()
            item["country"] = [x.strip() for x in country]
            city = row.xpath('td[@class="userdata"][@data-th="Country(City)"]//tr[2]/td/text()').extract()
            item["city"] = [x.strip().strip('()') for x in city]
            native = row.xpath('td[@class="userdata"][@data-th="Native Language"]//td/text()').extract()
            item["native"] = [x.strip() for x in native]
            practicing = row.xpath('td[@class="userdata"][@data-th="Practicing Language"]//td/text()').extract()
            item["practicing"] = [x.strip() for x in practicing]
            desc = row.xpath('td[@class="userdata"][@data-th="Description"]//td/text()').extract()
            item["desc"] = [x.strip() for x in desc]
            items.append(item)

        _encoder = ScrapyJSONEncoder()
        with open('mylanguageexchange_crawled.json', 'w') as outfile:
            outfile.write(_encoder.encode(items))

