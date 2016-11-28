=================
Ajax Sign
=================

------------------
Goal
------------------

Many websites now minified js file before deployment, so we should learn how to analyze the minmized code in browser and try to debug it in some cases.

You should create a spider which have name ``ajax_sign``

Once you finish the coding just run ``scrapy crawl ajax_sign --loglevel=INFO`` to check the output

------------------
Entry
------------------

Remember to change the port number if it is not 8000

http://127.0.0.1:8000/content/detail_sign

------------------
taskid
------------------

taskid::

    ajax_sign

------------------
Detail of task
------------------

In this task we try to crawl product title, product description, price info.

You should be concern that the description is in the html, but the title and price info should be given by ajax.

You found out that the ajax url used ``sign`` in the url but you have no idea how it is calculated, and it seems the js file ``detail_sign.js`` is minified.

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

    Learn how to pretty print minified js and debug the minified js, :ref:`chrome-web-tools`
