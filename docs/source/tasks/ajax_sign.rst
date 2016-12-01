=================
Ajax Sign
=================

------------------
Goal
------------------

Many websites now minified js file when deployment, so we should learn how to analyze the minmized code in browser and try to debug it in some cases to figure out the workflow. This process is like disassemble in reverse engineering.

------------------
Entry
------------------

If you have no idea what entry and taskid is, check :ref:`before_start`

Remember to config ``WEB_APP_PREFIX`` which located in spider_project/spider_project/settings.py

Entry::

    content/detail_sign

------------------
Taskid
------------------

Taskid::

    ajax_sign

------------------
Detail of task
------------------

In this task we try to crawl product title, product description, price info.

You found out that the ajax url used ``sign`` in the url but you have no idea where it is from, and it seems the js file ``detail_sign.js`` is minified.

Once you finish the coding just run ``scrapy crawl ajax_sign --loglevel=INFO`` to check the output

The final data should be::

    [{
        "data": {
            "price": "$ 20.00",
            "description": ["55% cotton, 40% polyester, 5% spandex.", "Imported", "Art.No. 85-8023"],
            "title": "Congratulations"
        },
        "taskid": "ajax_sign"
    }]

------------------
Advanded
------------------

.. note::

    Learn how to pretty print minified js and debug the minified js, :ref:`chrome-debug-minified-js`
