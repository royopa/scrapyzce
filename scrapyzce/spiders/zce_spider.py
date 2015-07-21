import scrapy


class ZceSpider(scrapy.Spider):
    name = "zce_spider"
    allowed_domains = ["zend.com"]
    start_urls = [
        "http://www.zend.com/en/yellow-pages/ZEND024088"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        #candidate_id = xpath('//table/tr[1]/td[2]/text()').extract()
        #city = xpath('//table/tr[1]/td[4]/text()').extract()
        #region = xpath('//table/tr[1]/td[5]/text()').extract()
        #country = xpath('//table/tr[1]/td[6]/text()').extract()
        #
        # photo_url = xpath('//table/tr[1]/td[6]/text()').extract()
        #
        # formatar ainda date = xpath('//table/tr[2]/td[2]/text()').extract()
        # formatar ainda site = xpath('//table/tr[3]/td[2]/text()').extract()
        # formatar ainda sites = xpath('//table/tr[7]/td[2]/text()').extract()
        # formatar ainda photo = xpath('//div[2]/img[1]/').extract()
        #
