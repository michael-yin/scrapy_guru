# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.http.request import Request
from spider_project.items import SpiderProjectItem

from six.moves.urllib import parse


class Basic_extractSpider(scrapy.Spider):
    """
    This spider is an example spider which show people how to write a spider in
    this project to work

    If you have no idea what variable ``name`` means here, please read
    https://doc.scrapy.org/en/latest/intro/tutorial.html

    If you have no idea what variable ``taskid`` and ``entry`` means here, please read
    http://scrapy-guru.readthedocs.io/en/latest/before_start.html
    taskid and entry only make sense in this project.

    """
    taskid = "basic_extract"
    name = taskid
    entry = "content/detail_basic"

    def start_requests(self):
        """
        In the scrapy doc there are two ways to tell scrapy where to begin to
        crawl from.  One is start_requests, the other is start_urls which is
        shortcut to the start_requestt.

        Based on my experience, it is better to use start_requests instead of
        start_urls bacause in this methods you can know how the request object
        are created and how request is yield. You should keep it simple and
        try not to use some magic or it might confuse you.

        In this project, you have no need to change code in this method, just
        modify code in parse_entry_page

        If you fully understatnd how scrapy work, then you are free to choose
        between start_requests and start_urls.
        """
        prefix = self.settings["WEB_APP_PREFIX"]
        result = parse.urlparse(prefix)
        base_url = parse.urlunparse(
            (result.scheme, result.netloc, "", "", "", "")
        )
        # Generate start url from config and self.entry, when you paste the code
        # to another spider you can just change self.entry and self.taskid
        url = parse.urljoin(base_url, self.entry)
        yield Request(
            url=url,
            callback=self.parse_entry_page
        )

    def parse_entry_page(self, response):
        """
        This method is a callback, when scrapy got response from web server, then
        this method will be called to process the response.

        If you have no idea what yield keyword in python mean, please read
        http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
        """
        # we create a item here, fill the data, and yield it
        item = SpiderProjectItem()
        item["taskid"] = self.taskid
        data = {}
        title = response.xpath("//div[@class='product-title']/text()").extract()
        desc = response.xpath(
            "//section[@class='container product-info']//li/text()").extract()
        data["title"] = title
        data["desc"] = desc

        item["data"] = data
        yield item

