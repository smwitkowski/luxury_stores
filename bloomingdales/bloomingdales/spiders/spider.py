import scrapy
from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor
from bloomingdales.items import BloomingdalesItem

class BloomingdalesSpider(CrawlSpider):
    name = "bloomingdales"
    allowed_domains = ['locations.bloomingdales.com']
    start_urls = ["http://locations.bloomingdales.com/index.html"]

    rules = (Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="locations-all"]//h5/a')), callback = 'parse_store', follow = True),)

    def parse_store(self, response):
        items = []
        item = BloomingdalesItem()
        item['Name'] = response.xpath('//*[@id="location-name"]/text()').extract()
        item['Address'] = response.xpath('//*[@itemprop="streetAddress"]/text()').extract()
        item['City'] = response.xpath('//*[@itemprop="addressLocality"]/text()').extract()
        item['State'] = response.xpath('//*[@itemprop="addressRegion"]/text()').extract()
        item['Zip'] = response.xpath('//*[@itemprop="postalCode"]/text()').extract()
        item['Telephone'] = response.xpath('//*[@itemprop = "telephone"]/text()').extract()
        item['URL'] = response.url
        item['Manager'] = response.xpath('//*[@class="manager-wrapper"]/text()').extract()
        item['Image_URL'] = "None"
        item['Monday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="0"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Monday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="0"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        item['Tuesday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="1"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Tuesday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="1"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        item['Wednesday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="2"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Wednesday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="2"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        item['Thursday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="3"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Thursday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="3"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        item['Friday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="4"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Friday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="4"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        item['Saturday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="5"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Saturday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="5"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        item['Sunday_Open'] = response.xpath('//tr[@data-day-of-week-start-index="6"]//span[@class="c-location-hours-details-row-intervals-instance-open"]/text()').extract()
        item['Sunday_Close'] = response.xpath('//tr[@data-day-of-week-start-index="6"]//span[@class="c-location-hours-details-row-intervals-instance-close"]/text()').extract()
        yield item


