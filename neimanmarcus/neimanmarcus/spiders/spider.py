import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from neimanmarcus.items import NeimanmarcusItem

class NeimanmarcsSpider(CrawlSpider):
    name = "neimanmarcus"
    allowed_domains = ['neimanmarcus.com']
    start_urls = ["http://www.neimanmarcus.com/stores/locations?geoLocation=Upper%20Marlboro%20,%20MD"]

    rules = (Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@class = "store_name"]')), callback = 'parse_store', follow = True),)


    def parse_store(self, response):
        items = []
        item = NeimanmarcusItem()
        item['Name'] = response.xpath('translate(normalize-space(//div[@class = "store-header store-name"]/div[1]/text()), " ", " ")').extract()
        address_1 = response.xpath('//span[@itemprop = "streetAddress"][1]/text()').extract()
        address_2 = response.xpath('//span[@itemprop = "streetAddress"][2]/text()').extract()
        item['Address'] = ''.join([str(address_1), " ", str(address_2)]).strip()
        item['City'] = response.xpath('translate(normalize-space(//span[@itemprop = "addressLocality"][1]/text()), ",", "")').extract()
        item['State'] = response.xpath('//span[@itemprop = "addressRegion"]/text()').extract()
        item['Zip'] = response.xpath('//span[@itemprop = "postalCode"]/text()').extract()
        item['Telephone_1'] = response.xpath('//div[span[@itemprop = "telephone"]][1]/span[1]/a/text()').extract()
        item['Telephone_2'] = response.xpath('//div[span[@itemprop = "telephone"]][1]/span[2]/a/text()').extract()
        item['URL'] = response.url
        manager = "NA"
        if re.search('Store Manager', str(manager)):
            item['Manager'] = re.search('^.*(?=,)', str(manager)).group()
        else:
            item['Manager'] = "None"
        image_url = response.xpath('//div[div[@class = "storeDesc"]]/span/img/@src').extract()
        item['Image_URL'] = ''.join(['http://www.neimanmarcus.com', str(image_url)])

        Monday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Mon")]]/td[contains(text(), "PM")]/text()').extract()
        if re.search("PM", str(Monday), re.IGNORECASE):
            item['Monday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Monday))[0]
        else:
            item['Monday_Open'] = "Closed"

        if re.search("PM", str(Monday), re.IGNORECASE):
            item['Monday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Monday))[1]
        else:
            item['Monday_Close'] = "Closed"

        Tuesday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Tue")]]/td[contains(text(), "PM")]').extract()
        if re.search("PM", str(Tuesday), re.IGNORECASE):
            item['Tuesday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Tuesday))[0]
        else:
            item['Tuesday_Open'] = "Closed"

        if re.search("PM", str(Tuesday), re.IGNORECASE):
            item['Tuesday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Tuesday))[1]
        else:
            item['Tuesday_Close'] = "Closed"

        Wednesday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Wed")]]/td[contains(text(), "PM")]').extract()
        if re.search("PM", str(Wednesday), re.IGNORECASE):
            item['Wednesday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Wednesday))[0]
        else:
            item['Wednesday_Open'] = "Closed"

        if re.search("PM", str(Wednesday), re.IGNORECASE):
            item['Wednesday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Wednesday))[1]
        else:
            item['Wednesday_Close'] = "Closed"

        Thursday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Thu")]]/td[contains(text(), "PM")]').extract()
        if re.search("PM", str(Thursday), re.IGNORECASE):
            item['Thursday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Thursday))[0]
        else:
            item['Thursday_Open'] = "Closed"

        if re.search("PM", str(Thursday), re.IGNORECASE):
            item['Thursday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Thursday))[1]
        else:
            item['Thursday_Close'] = "Closed"

        Friday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Fri")]]/td[contains(text(), "PM")]').extract()
        if re.search("PM", str(Friday), re.IGNORECASE):
            item['Friday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Friday))[0]
        else:
            item['Friday_Open'] = "Closed"

        if re.search("PM", str(Friday), re.IGNORECASE):
            item['Friday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Friday))[1]
        else:
            item['Friday_Close'] = "Closed"

        Saturday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Sat")]]/td[contains(text(), "PM")]').extract()
        if re.search("PM", str(Saturday), re.IGNORECASE):
            item['Saturday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Saturday))[0]
        else:
            item['Saturday_Open'] = "Closed"

        if re.search("PM", str(Saturday), re.IGNORECASE):
            item['Saturday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Saturday))[1]
        else:
            item['Saturday_Close'] = "Closed"

        Sunday = response.xpath('//div[contains(@class,"hide-on-tablet")]//tr[td[contains(text(), "Sun")]]/td[contains(text(), "PM")]').extract()
        if re.search("PM", str(Sunday), re.IGNORECASE):
            item['Sunday_Open'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Sunday))[0]
        else:
            item['Sunday_Open'] = "Closed"

        if re.search("PM", str(Sunday), re.IGNORECASE):
            item['Sunday_Close'] = re.findall('\d{1,2}:\d{,2}\w{,2}', str(Sunday))[1]
        else:
            item['Sunday_Close'] = "Closed"

        yield item