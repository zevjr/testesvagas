from scrapy.crawler import CrawlerProcess
from pagescrap.pages_spider import PagesSpider


def init_app(list_urls):
    process = CrawlerProcess({
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json',

    })

    process.crawl(PagesSpider, urls=list_urls)
    process.start()
