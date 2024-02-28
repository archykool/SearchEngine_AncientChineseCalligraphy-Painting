# -*- coding: utf-8 -*-
import scrapy
from tpm.items import TpmItem


class TpmspiderSpider(scrapy.Spider):
    name = 'tpmspider'
    allowed_domains = ['www.dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/searchs/handwritings/category_id/92/p/1.html']

    def parse(self, response):
        # 遍历当前页的12件藏品
        for i in range (2, 14):
            item = TpmItem ()
            item['title'] = response.xpath (
                '//*[@id="building2"]/div/div[2]/table/tbody/tr[' + str (i) + ']/td[1]/a/text()').extract()
            item['dynasty'] = response.xpath (
                '//*[@id="building2"]/div/div[2]/table/tbody/tr[' + str (i) + ']/td[2]/text()').extract()
            item['classify'] = response.xpath (
                '//*[@id="building2"]/div/div[2]/table/tbody/tr[' + str (i) + ']/td[3]/text()').extract()
            item['author'] = response.xpath (
                '//*[@id="building2"]/div/div[2]/table/tbody/tr[' + str (i) + ']/td[4]/text()').extract()

            # 进入二级连接
            detail_page = response.xpath ('//*[@id="building2"]/div/div[2]/table/tbody/tr[' + str(i) + ']/td[1]/a/@href').extract_first()
            detail_url = response.urljoin (detail_page)
            item['collection_detail_url'] = response.urljoin (detail_page)
            yield scrapy.Request (detail_url, meta={'item':item}, callback=self.parse_detail, dont_filter=True)

            # 进入下一页
            i = 2
            while i <= 41:
                next_url = 'https://www.dpm.org.cn/searchs/handwritings/category_id/92/p/' + str(i) + '.html'
                i = i + 1
                yield scrapy.Request(next_url)

    def parse_detail(self,response):
        item = response.meta['item']
        item['image'] = response.xpath ('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract ()
        item['title2'] = response.xpath ('//*[@id="hl_content"]/div/div[2]/h3/text()').extract ()
        item['content'] = response.xpath ('//*[@id="hl_content"]/div/div[2]/div[1]/p').extract ()
        yield item