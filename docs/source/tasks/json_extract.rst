==================
Json extract
==================

------------------
Goal
------------------

Recently many websites start to use json format to save data. So we need to learn how to handle this situation.

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_json

------------------
Taskid
------------------

Taskid::

    json_extract

------------------
Detail of task
------------------

In this task we try to crawl product title and price info. You should find out that the value returned by xpath is not the one you see in your brower. Because javascript have change that.

Once you finish the coding just run ``scrapy crawl json_extract --loglevel=INFO`` to check the output

The final data should be::

    [{
        "data": {
            "price": "$ 13.99",
            "title": "MAMA Jersey Top"
        },
        "taskid": "json_extract"
    }]

------------------
Advanded
------------------

.. note::

    Sometime there are some unicode char in the raw json string which might cause program raise UnicodeDecodeError. You should remember before runing json.loads, make the the json_data is decoded as unicode string type. If there are some syntax error in json string, you can use `json lint <http://jsonlint.com/>`_ to help you figure out where the error is.
