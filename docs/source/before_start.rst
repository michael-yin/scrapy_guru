.. _before_start:

========================================
Read before you start
========================================

------------------
Entry
------------------

Every task have an entry point where spider start to crawl, this entry point may be overview page which contains many product page, or it might be product detail page. or something else.

------------------
Taskid
------------------

The taskid is unique, each task have unique taskid, and we need to remember to set it in item yield from spider.

------------------
Item
------------------

The data scraped by spider should be filed in ``SpiderProjectItem`` located in ``spider_project/spider_project/items.py``::

    class SpiderProjectItem(scrapy.Item):
        # define the fields for your item here like:
        taskid = scrapy.Field()
        data = scrapy.Field()

The ``taskid`` field is the taskid you can get in each task, and the ``data`` is the data scraped, in most cases, the data filed is a ``dict`` python type.

--------------------------------------------------
How to know if the spider work fine in each task?
--------------------------------------------------

Since it is not easy to analyze code to check if the spider work fine, so I think it is better to focus on the scraped data to check if the spider is right.

After spider yield the item, the pipeline will check if the scraped data is right and the result can be found in log file. This work is done by ``spider_project`` automatically.

--------------------------------------------------
Done
--------------------------------------------------

Now you are ready to start developing spider, please start here :ref:`task_basic_extract`




