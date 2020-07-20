import scrapy
import re
from pagescrap.utils import get_regex, get_link_logo


class PagesSpider(scrapy.Spider):
    name = 'pages'

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        urls = kwargs.pop('urls', [])
        if urls:
            self.start_urls = urls
        self.logger.info(self.start_urls)

    def parse(self, response):
        html = response.text
        list_regex = get_regex()

        phone_list = []
        for i in list_regex:
            phone_list.append(re.findall(i, html))

        phone_union = []
        for union in phone_list:
            phone_union = list(set().union(phone_union, union))

        phones = []
        for phone in phone_union:
            phones.append(''.join(phone))

        img_logos = response.xpath('//img').getall()

        cmp = get_link_logo(img_logos)

        result = {'logo': ''.join(set(cmp)), 'phones': phones, 'website': response.url}
        yield result
