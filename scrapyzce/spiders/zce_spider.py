import scrapy
from scrapyzce.items import ScrapyZceItem


class ZceSpider(scrapy.Spider):

    def get_urls():
        with open('urls_to_check.txt') as f:
            return f.read().splitlines()

    def parse(self, response):
        item = ScrapyZceItem()

        item['candidate_name'] = response.xpath('//div/h1/text()').extract()

        item['cert_name'] = response.xpath('//div/h2/text()').extract()

        item['candidate_id'] = response.xpath(
            '//table/tr[1]/td[2]/text()').extract()

        cert_date = response.xpath(
            '//table/tr[2]/td[2]/div/div/div/text()').extract()

        cert_date = cert_date[0].replace("\t", "")
        cert_date = cert_date.replace("\n", "")

        item['cert_date'] = cert_date

        item['company_name'] = response.xpath(
            '//table/tr[3]/td[2]/a/text()').extract()

        item['company_link'] = response.xpath(
            '//table/tr[3]/td[2]/a/@href').extract()

        item['city'] = response.xpath(
            '//table/tr[4]/td[2]/text()').extract()

        item['state_region'] = response.xpath(
            '//table/tr[5]/td[2]/text()').extract()

        item['country'] = response.xpath('//table/tr[6]/td[2]/text()').extract()

        item['photo_url'] = response.xpath(
            '//div[2]/img[@id="zce-photo"]/@src').extract()

        print item['candidate_name']
        print item['candidate_id']
        print item['cert_name']
        print item['cert_date']
        print item['company_name']
        print item['company_link']
        print item['city']
        print item['state_region']
        print item['country']
        print item['photo_url']

        yield item

    name = "zce_spider"
    allowed_domains = ["zend.com"]
    start_urls = get_urls()
