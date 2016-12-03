==================
List page extract
==================

------------------
Goal
------------------

In most cases, your spider should start from a list index page and crawl all the product links in the page, so in this task you will learn how to write spider to work in this case.

You should notice that you need also deal with pagination.

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/list_basic/1

If your webapp is working on 8000, click the link below

http://127.0.0.1:8000/content/list_basic/1

------------------
Taskid
------------------

Taskid::

    list_extract

------------------
Detail of task
------------------

There are about 100+ products in all list pages, you should crawl them all, for each product, you should crawl title, price, and sku. Sku can be extracted from product url

Once you finish the coding just run ``scrapy crawl list_extract --loglevel=INFO`` to check the output

The final data is too long, this is part of it::

    [{
        "data": {
            "price": ["$29.99"],
            "title": ["Large wooden box-Dusky green"],
            "sku": "0442019003"
        },
        "taskid": "list_extract"
    }, {
        "data": {
            "price": ["$14.99"],
            "title": ["Textured trinket box-White"],
            "sku": "0447183001"
        },
        "taskid": "list_extract"
    }, {
        "data": {
            "price": ["$39.99"],
            "title": ["Cotton terry dressing gown-Light grey"],
            "sku": "0463014001"
        },
        "taskid": "list_extract"
    }]
