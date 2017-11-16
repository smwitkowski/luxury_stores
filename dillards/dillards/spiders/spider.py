import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from dillards.items import DillardsItem

class BloomingdalesSpider(CrawlSpider):
    name = "dillards"
    allowed_domains = ['dillards.com']
    start_urls = ["https://www.dillards.com/stores"]

    rules = (Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@class="mallname"]/a')), callback = 'parse_store', follow = True),)

    def parse_store(self, response):
        items = []
        item = DillardsItem()
        item['Name'] = response.xpath('//*[@class = "store-name"]/text()').extract()
        item['Address'] = response.xpath('//*[@data-twist = "address"]/text()[1]').extract()
        full_address = response.xpath('//*[@data-twist = "address"]/text()[2]').extract()
        item['City'] = re.search('^.*(?=,)', str(full_address)).group()
        item['State'] = re.search('(?<=\\\\xa0).*?(?=\\\\xa0)', str(full_address)).group().strip()
        item['Zip'] = re.search('[\d]{5,5}', str(full_address)).group()
        item['Telephone'] = response.xpath('//*[@data-twist = "phone"]/a/text()').extract()
        item['URL'] = response.url
        manager = response.xpath('//p[contains(text(), "Store Manager")]/text()').extract()
        if re.search('Store Manager', str(manager)):
            item['Manager'] = re.search('^.*(?=,)', str(manager)).group()
        else:
            item['Manager'] = "NA"
        image_url = response.xpath('//*[@data-twist = "store-image"]/@src').extract()
        item['Image_URL'] = ''.join(['https://www.dillards.com', str(image_url)])

        Monday = response.xpath('//*[td[contains(text(), "Monday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Monday), re.IGNORECASE):
            item['Monday_Open'] = re.search('^.*(?=-)', str(Monday)).group().strip()
        else:
            item['Monday_Open'] = "Closed"

        if re.search("PM", str(Monday), re.IGNORECASE):
            item['Monday_Close'] = re.search('(?<=-).*', str(Monday)).group().strip()
        else:
            item['Monday_Close'] = "Closed"

        Tuesday = response.xpath('//*[td[contains(text(), "Tuesday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Tuesday), re.IGNORECASE):
            item['Tuesday_Open'] = re.search('^.*(?=-)', str(Tuesday)).group().strip()
        else:
            item['Tuesday_Open'] = "Closed"

        if re.search("PM", str(Tuesday), re.IGNORECASE):
            item['Tuesday_Close'] = re.search('(?<=-).*', str(Tuesday)).group().strip()
        else:
            item['Tuesday_Close'] = "Closed"

        Wednesday = response.xpath('//*[td[contains(text(), "Wednesday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Wednesday), re.IGNORECASE):
            item['Wednesday_Open'] = re.search('^.*(?=-)', str(Wednesday)).group().strip()
        else:
            item['Wednesday_Open'] = "Closed"

        if re.search("PM", str(Wednesday), re.IGNORECASE):
            item['Wednesday_Close'] = re.search('(?<=-).*', str(Wednesday)).group().strip()
        else:
            item['Wednesday_Close'] = "Closed"

        Thursday = response.xpath('//*[td[contains(text(), "Thursday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Thursday), re.IGNORECASE):
            item['Thursday_Open'] = re.search('^.*(?=-)', str(Thursday)).group().strip()
        else:
            item['Thursday_Open'] = "Closed"

        if re.search("PM", str(Thursday), re.IGNORECASE):
            item['Thursday_Close'] = re.search('(?<=-).*', str(Thursday)).group().strip()
        else:
            item['Thursday_Close'] = "Closed"

        Friday = response.xpath('//*[td[contains(text(), "Friday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Friday), re.IGNORECASE):
            item['Friday_Open'] = re.search('^.*(?=-)', str(Friday)).group().strip()
        else:
            item['Friday_Open'] = "Closed"

        if re.search("PM", str(Friday), re.IGNORECASE):
            item['Friday_Close'] = re.search('(?<=-).*', str(Friday)).group().strip()
        else:
            item['Friday_Close'] = "Closed"

        Saturday = response.xpath('//*[td[contains(text(), "Saturday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Saturday), re.IGNORECASE):
            item['Saturday_Open'] = re.search('^.*(?=-)', str(Saturday)).group().strip()
        else:
            item['Saturday_Open'] = "Closed"

        if re.search("PM", str(Saturday), re.IGNORECASE):
            item['Saturday_Close'] = re.search('(?<=-).*', str(Saturday)).group().strip()
        else:
            item['Saturday_Close'] = "Closed"

        Sunday = response.xpath('//*[td[contains(text(), "Sunday")]]/td[contains(text(),"PM")]/text()').extract()
        if re.search("PM", str(Sunday), re.IGNORECASE):
            item['Sunday_Open'] = re.search('^.*(?=-)', str(Sunday)).group().strip()
        else:
            item['Sunday_Open'] = "Closed"

        if re.search("PM", str(Sunday), re.IGNORECASE):
            item['Sunday_Close'] = re.search('(?<=-).*', str(Sunday)).group().strip()
        else:
            item['Sunday_Close'] = "Closed"
        yield item


