==================
Meta StoreInfo
==================

------------------
Goal
------------------

Sometime if you want to pass value between more than one http pages, then you will need response.meta as a tmp datatable.

------------------
Entry
------------------

Remember to change the port number if it is not 8000

http://127.0.0.1:8000/content/detail_header

------------------
taskid
------------------

taskid::

    meta_storeinfo

------------------
Detail of task
------------------

In this task we try to crawl product title, product description, price info. 

You should be concern that the description is in the html, but the title and price info should be given by ajax. To deal with this situation, you should save the description in response.meta and pass it in request.

For more info, please take a look at 

https://doc.scrapy.org/en/latest/topics/request-response.html#passing-additional-data-to-callback-functions

The final data should be::

    [{
        "data": {
            "price": "$ 12.99",
            "description": ["55% cotton, 40% polyester, 5% spandex.", "Imported", "Art.No. 85-8023"],
            "title": "MAMA Jersey Top"
        },
        "taskid": "meta_storeinfo"
    }]

