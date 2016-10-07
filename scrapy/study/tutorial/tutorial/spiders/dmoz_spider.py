from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, reponse):
        sel = Selector(reponse)
        sites = sel.xpath('//div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)
        return items
