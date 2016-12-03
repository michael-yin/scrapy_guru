.. _task_list_extract_pagination:

==================================
List page and pagination extract
==================================

------------------
Goal
------------------

The only difference between this task and :ref:`task_list_extract` is that thie task also needs deal with pagination

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

    list_extract_pagination

------------------
Detail of task
------------------

There are about 100+ products in all list pages, you should crawl them all, for each product, you should crawl title, price, and sku. Sku can be extracted from product url

The final data is too long, this is part of it::

    [{
        "data": {
            "sku": "0447183001",
            "price": ["$14.99"],
            "title": ["Textured trinket box-White"]
        },
        "taskid": "list_extract_pagination"
    }, {
        "data": {
            "sku": "0463014001",
            "price": ["$39.99"],
            "title": ["Cotton terry dressing gown-Light grey"]
        },
        "taskid": "list_extract_pagination"
    }]
