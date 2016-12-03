==================
Regex extract
==================

------------------
Goal
------------------

Regex is a very powerful tool when dealing with text, you have no reason to ignore it. A regulare expression is a string describing a certain amount of texts. If you have no knowledge of regex, you should learn it before you begin this task.

You can read this great tutorials `here <https://regexone.com/>`_  , once you have learned regex, you can try this online regex `tool <https://www.debuggex.com/>`_  to quickly test your regex written in python. 

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_regex

If your webapp is working on 8000, click the link below

http://127.0.0.1:8000/content/detail_regex

------------------
Taskid
------------------

Taskid::

    regex_extract

------------------
Detail of task
------------------

In this task we try to crawl product title and price info. Since the data in js is not very easy to extract, regex is a good tool to handle this situation.

Once you finish the coding just run ``scrapy crawl regex_extract --loglevel=INFO`` to check the output

The final data should be::

    [{
        "data": {
            "title": "Regex is important",
            "price": "$ 13.99"
        },
        "taskid": "regex_extract"
    }]
