import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from nordstrom.items import NordstromItem

class NordstromSpider(CrawlSpider):
    name = "nordstrom"
    allowed_domains = ['mystore411.com']
    start_urls = ["https://www.mystore411.com/store/listing/49/Nordstrom-store-locations"]

    rules = (Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="main"]//a[contains(@href, "store/list") and contains(@href, "Nordstrom")]')), follow = True),
             Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="main"]//a[contains(@href, "store/view") and contains(@href, "Nordstrom")]')), callback='parse_store', follow = True),)

    def parse_store(self, response):
        items = []
        item = NordstromItem()
        item['Name'] = response.xpath('//a[@itemprop="item" and contains(text(),"in")]/text()').extract()
        item['Address'] = response.xpath('//span[@itemprop = "streetAddress"]/text()').extract()
        item['City'] = response.xpath('translate(normalize-space(//span[@itemprop = "addressLocality"][1]/text()), ",", "")').extract()
        item['State'] = response.xpath('//span[@itemprop = "addressRegion"]/text()').extract()
        item['Zip'] = response.xpath('//span[@itemprop = "postalCode"]/text()').extract()
        item['Telephone'] = response.xpath('//span[@itemprop = "telephone"]/text()').extract()
        item['URL'] = response.url
        item['Manager'] = "NA"
        item['Image_URL'] = "NA"
        hours = response.xpath('//div[h3[contains(text(),"Store Hours")]]/h3/following-sibling::p[1]/text()').extract()
        for i in range(len(hours)-1):
            Monday_Time = re.search("((?<=(Mon))|(?<=(Mon-(Tue|Wed|Thu|Fri|Sat|Sun)))|(?<=Tue-Mon)|(<?=(Wed-(Mon|Tue)))|(?<=(Thu-(Mon|Tue|Wed)))|(?<=(Fri-(Mon|Tue|Wed|Thu)))|(?<=(Sat-(Mon|Tue|Wed|Thu|Fri)))|(?<=(Sun-(Mon|Tue|Wed|Thu|Fri|Sat)))).*", str(hours[i]), re.IGNORECASE)
            if Monday_Time is not None:
                monday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Monday_Time.group())
                item['Monday_Open'] = monday_hours[0][0]
                item['Monday_Close'] = monday_hours[1][0]
            Tuesday_Time = re.search("((?<=(Tue))|(?<=Tue-(Wed|Thu|Fri|Sat|Sun|Mon))|(?<=(Wed-(Tue)))|(?<=(Thu-(Tue|Wed)))|(?<=(Fri-(Tue|Wed|Thu)))|(?<=(Sat-(Tue|Wed|Thu|Fri)))|(?<=(Sun-(Tue|Wed|Thu|Fri|Sat)))|(?<=(Mon-(Tue|Wed|Thu|Fri|Sat|Sun)))).*", str(hours[i]), re.IGNORECASE)
            if Tuesday_Time is not None:
                tuesday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Tuesday_Time.group())
                item['Tuesday_Open'] = tuesday_hours[0][0]
                item['Tuesday_Close'] = tuesday_hours[1][0]
            Wednesday_Time = re.search("((?<=(Wed))|(?<=(Wed-(Thu|Fri|Sat|Sun|Mon|Tue)))|(?<=(Thu-Wed))|(?<=(Fri-(Wed|Thu)))|(?<=(Sat-(Wed|Thu|Fri)))|(?<=(Sun-(Wed|Thu|Fri|Sat)))|(?<=(Mon-(Wed|Thu|Fri|Sat|Sun)))|(?<=(Tue-(Wed|Thu|Fri|Sat|Sun)))).*", str(hours[i]), re.IGNORECASE)
            if Wednesday_Time is not None:
                wednesday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Wednesday_Time.group())
                item['Wednesday_Open'] = wednesday_hours[0][0]
                item['Wednesday_Close'] = wednesday_hours[1][0]
            Thursday_Time = re.search("((?<=(Thu))|(?<=Thu-(Fri|Sat|Sun|Mon|Tue|Wed))|(?<=(Fri-Thu))|(?<=(Sat-(Thu|Fri)))|(?<=(Sun-(Thu|Fri|Sat)))|(?<=(Mon-(Thu|Fri|Sat|Sun)))|(?<=(Tue-(Thu|Fri|Sat|Sun|Mon)))|(?<=(Wed-(Thu|Fri|Sat|Sun|Mon|Tue)))).*", str(hours[i]), re.IGNORECASE)
            if Thursday_Time is not None:
                thursday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Thursday_Time.group())
                item['Thursday_Open'] = thursday_hours[0][0]
                item['Thursday_Close'] = thursday_hours[1][0]
            Friday_Time = re.search("((?<=(Fri))|(?<=(Fri-(Sat|Sun|Mon|Tue|Wed|Thu)))|(?<=(Sat-Fri))|(?<=(Sun-(Fri|Sat)))|(?<=(Mon-(Fri|Sat|Sun)))|(?<=(Tue-(Fri|Sat|Sun|Mon)))|(?<=(Wed-(Fri|Sat|Sun|Mon|Tue)))|(?<=(Thu-(Fri|Sat|Sun|Mon|Tue|Wed)))).*", str(hours[i]), re.IGNORECASE)
            if Friday_Time is not None:
                friday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Friday_Time.group())
                item['Friday_Open'] = friday_hours[0][0]
                item['Friday_Close'] = friday_hours[1][0]
            Saturday_Time = re.search("((?<=(Sat))|(?<=(Sat-(Sun|Mon|Tue|Wed|Thu|Fri)))|(?<=(Sun-Sat))|(?<=(Mon-(Sat|Sun)))|(?<=(Tue-(Sat|Sun|Mon)))|(?<=(Wed-(Sat|Sun|Mon|Tue)))|(?<=(Thu-(Sat|Sun|Mon|Tue|Wed)))|(?<=(Fri-(Sat|Sun|Mon|Tue|Wed|Thu)))).*", str(hours[i]), re.IGNORECASE)
            if Saturday_Time is not None:
                saturday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Saturday_Time.group())
                item['Saturday_Open'] = saturday_hours[0][0]
                item['Saturday_Close'] = saturday_hours[1][0]
            Sunday_Time = re.search("((?<=(Sun))|(?<=(Sun-(Mon|Tue|Wed|Thu|Fri|Sat)))|(?<=(Mon-Sun))|(?<=(Tue-(Sun|Mon)))|(?<=(Wed-(Sun|Mon|Tue)))|(?<=(Thu-(Sun|Mon|Tue|Wed)))|(?<=(Fri-(Sun|Mon|Tue|Wed|Thu)))|(?<=(Sat-(Sun|Mon|Tue|Wed|Thu|Fri)))).*", str(hours[i]), re.IGNORECASE)
            if Sunday_Time is not None:
                sunday_hours = re.findall('((\d{1,2}\:\d{2}\w{2})|(\d{1,2}\w{2}))', Sunday_Time.group())
                item['Sunday_Open'] = sunday_hours[0][0]
                item['Sunday_Close'] = sunday_hours[1][0]
        yield item