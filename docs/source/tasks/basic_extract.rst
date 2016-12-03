.. _task_basic_extract:

==================
Basic extract
==================

------------------
Goal
------------------

There are mainly two ways in web crawling package such as scrapy, beautifulsoup to extract info from html, one is ``css`` and the other is ``xpath``, you can learn css `here <https://api.jquery.com/category/selectors/>`_ and xpath `here <https://msdn.microsoft.com/en-us/library/ms256471%28v=vs.110%29.aspx>`_ 

I must say there is not much difference between them, you can pick the one you prefer in spider developing.

You might need quickly test your xpath or css expression in your browser, check it here :ref:`chrome-xpath-css`

I have created basic_extract spider to show you how to use it in this project. You are free to delete it and create your own or modify it.

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_basic

If your webapp is working on 8000, click the link below

http://127.0.0.1:8000/content/detail_basic

------------------
Taskid
------------------

Taskid::

    basic_extract

------------------
Detail of task
------------------

Once you finish the coding just run ``scrapy crawl basic_extract --loglevel=INFO`` to check the output, this command is a scrapy command which run spider which have name basic_extract and set the logging level to INFO. This command will run the spider, crawl the data and check the data. Results will show up in terminal

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

    What you should concern in this task is that in some cases the xpath espression which indeed work in your browser can not work on raw html becuase some DOM element might been modified by js, so please test it in scrapy shell before write it in spider code.

