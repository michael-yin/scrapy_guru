==================
Ajax Header
==================

------------------
Goal
------------------

Some backend systems would check http header to block some abnormal request. In this case we need to make sure the request from our spider will hsave the same http header as we see in the browser.

You should check the http header in the browser first and then implement it in your spider.

If you have no idea what http header is , check `here <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>`_

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_header

------------------
Taskid
------------------

Taskid::

    ajax_header

------------------
Detail of task
------------------

In this task we try to crawl product title and price info. You should find out that the value in html is not the one you see in your brower.

Once you finish the coding just run ``scrapy crawl ajax_header --loglevel=INFO`` to check the output

The final data should be::

    [{
        "data": {
            "price": "$ 12.99",
            "title": "MAMA Jersey Top"
        },
        "taskid": "ajax_header"
    }]


------------------
Advanded
------------------

.. note::

    Actually you can use some proxy tools to help you analyze http request easier, visit :ref:`mitmproxy`.
