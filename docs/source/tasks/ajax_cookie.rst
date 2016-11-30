==================
Ajax Cookie
==================

------------------
Goal
------------------

It is importtant to analyze cookies of http request in many cases

If you have no idea what cookie is , read `it <http://www.w3schools.com/js/js_cookies.asp>`_

If you are using chrome, try visiting chrome://settings/cookies , then you can inspect all cookies in your browser.

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_cookie

------------------
Taskid
------------------

Taskid::

    ajax_cookie

------------------
Detail of task
------------------

In this task we try to crawl product title, product description, price info.

After some tests, you might find out it is hard to make the spider get the data through ajax, so you need to dive into the detail of the ajax request.

You need to make sure the url, http header, cookie values are all reasonable.

Once you finish the coding just run ``scrapy crawl ajax_cookie --loglevel=INFO`` to check the output

The final data should be::

    [{
        "data": {
            "price": "$ 20.00",
            "description": ["55% cotton, 40% polyester, 5% spandex.", "Imported", "Art.No. 85-8023"],
            "title": "Congratulations"
        },
        "taskid": "ajax_cookie"
    }]

------------------
Advanded
------------------

.. note::

    When dealing with cookies in browser, it seems a fresh start without any cookie is a good start. see :ref:`chrome-incognito`.
