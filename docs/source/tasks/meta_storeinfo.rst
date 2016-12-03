==================
Meta StoreInfo
==================

------------------
Goal
------------------

Sometime if you want to pass value between more than one http pages, then you will need response.meta as a tmp datatable.

You can learn more `here <https://doc.scrapy.org/en/latest/topics/request-response.html#passing-additional-data-to-callback-functions>`_

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_header

If your webapp is working on 8000, click the link below

http://127.0.0.1:8000/content/detail_header

------------------
Taskid
------------------

Taskid::

    meta_storeinfo

------------------
Detail of task
------------------

In this task we try to crawl product title, product description, price info.

You should be concern that the description is in the raw html, but the title and price info should be given by ajax. To deal with this situation, you should save the description in response.meta and pass it in request.

The final data should be::

    [{
        "data": {
            "price": "$ 12.99",
            "description": ["55% cotton, 40% polyester, 5% spandex.", "Imported", "Art.No. 85-8023"],
            "title": "MAMA Jersey Top"
        },
        "taskid": "meta_storeinfo"
    }]

