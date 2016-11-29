.. _task_basic_extract:

==================
Basic extract
==================

------------------
Goal
------------------

There are mainly two ways in scrapy to extract info from html, one is ``css`` and the other is ``xpath``, in the code of this project I will choose xpath and I have to say there is not much difference between them, you can pick the one you prefer.

Once you finish the coding just run ``scrapy crawl basic_extract --loglevel=INFO`` to check the output

------------------
Entry
------------------

Remember to change the port number if it is not 8000

http://127.0.0.1:8000/content/detail_basic

------------------
Taskid
------------------

Taskid::

    basic_extract

------------------
Detail of task
------------------

In this task we extract the title, description from the entry page (above), the final data should be::

    [{
        "data": {
            "desc": ["55% cotton, 40% polyester, 5% spandex.", "Imported", "Art.No. 85-8023"],
            "title": ["MAMA Jersey Top"]
        },
        "taskid": "basic_extract"
    }]

------------------
Advanded
------------------

.. note::

    What you should concern here is that in some cases the xpath espression which indeed work in browser can not work on raw html becuase some DOM element might been modified by js, so please test it in scrapy shell before write it in spider code. You can visit :ref:`chrome-xpath-css` to learn more.

