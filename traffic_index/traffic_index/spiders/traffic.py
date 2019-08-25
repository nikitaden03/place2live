# TODO Add documentation to this module (traffic)
from scrapy import Spider
from scrapy.loader import ItemLoader
from traffic_index.items import TrafficIndexItem


class TrafficSpider(Spider):
    # TODO Add documentation for this class(TrafficSpider) and parse function
    name = "traffic"
    allowed_domains = ["tomtom.com"]
    start_urls = ["https://www.tomtom.com/en_gb/traffic-index/ranking/"]

    def parse(self, response):
        # Base XPath for extract need values
        xpath_selector = "//div[@id='RankingPage-table']//td[{}]"
        world_ranks = response.xpath(xpath_selector.format(1)).getall()
        cities = response.xpath(xpath_selector.format(3)).getall()
        countries = response.xpath(xpath_selector.format(4)).getall()
        congestion_levels = response.xpath(xpath_selector.format(5)).getall()
        for rank, city, country, level in zip(
            world_ranks, cities, countries, congestion_levels
        ):
            i = ItemLoader(item=TrafficIndexItem())
            i.add_value("world_rank", rank)
            i.add_value("city", city)
            i.add_value("country", country)
            i.add_value("congestion_level", level)
            yield i.load_item()
