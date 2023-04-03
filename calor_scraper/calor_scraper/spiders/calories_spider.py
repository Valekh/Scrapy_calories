import scrapy
import w3lib.html
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#  https://www.calories.info/food/potato-products


class CaloriesSpider(CrawlSpider):
    name = "calories"
    start_urls = ['https://www.calories.info/']

    rules = (
        Rule(LinkExtractor(allow='food'), callback='parse_item'),
    )

    def parse_item(self, response):
        products = response.css('tbody').css('tr')
        for item in products:
                yield {
                    'product': item.css('td.food a::text').get(),
                    'serving': w3lib.html.remove_tags(item.css('td.serving.portion').get()).replace(
                        '\\xa0', ''),
                    'calories': item.css('td.kcal').css('data::text').get(),
                }