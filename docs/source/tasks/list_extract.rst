.. _task_list_extract:

===================================
List page and products extract
===================================

------------------
Goal
------------------

In most cases, your spider should start from a list index page and crawl all the product links in the page, so in this task you will learn how to write spider to work in this case.

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

There are **10** products in list page 1, you should extract all product links first, and for each product, you should crawl title, price, and sku. Sku can be extracted from product url

Once you finish the coding just run ``scrapy crawl list_extract --loglevel=INFO`` to check the output

The final data is too long, this is part of it::

    [{
        "data": {
            "sku": "0184140017",
            "price": ["$14.99"],
            "title": ["Washed linen table runner-Anthracite grey"]
        },
        "taskid": "list_extract"
    }, {
        "data": {
            "sku": "0184140016",
            "price": ["$14.99"],
            "title": ["Washed linen table runner-Grey"]
        },
        "taskid": "list_extract"
    }, {
        "data": {
            "sku": "0184124001",
            "price": ["$19.99"],
            "title": ["Lace table runner-White"]
        },
        "taskid": "list_extract"
    }]
