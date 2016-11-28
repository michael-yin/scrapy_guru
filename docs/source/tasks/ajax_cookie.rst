==================
Ajax Cookie
==================

------------------
Goal
------------------

It is importtant to analyze cookies of http request in many cases

You should create a spider which have name ``ajax_cookie``

Once you finish the coding just run ``scrapy crawl ajax_cookie --loglevel=INFO`` to check the output

------------------
Entry
------------------

Remember to change the port number if it is not 8000

http://127.0.0.1:8000/content/detail_cookie

------------------
taskid
------------------

taskid::

    ajax_cookie

------------------
Detail of task
------------------

In this task we try to crawl product title, product description, price info.

You should be concern that the description is in the html, but the title and price info should be given by ajax. 

After some tests, you might find out it is hard to make the spider get the data through ajax, so you need to dive into the detail of the ajax request.

You need to make sue the url, http header, cookie values are all reasonable.

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
