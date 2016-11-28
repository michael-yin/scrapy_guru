==================
Scrapy Commands
==================

--------------
Scrapy parse
--------------

Is it a good idea to run spider directly after you finish you spider? No! You must at least to test each method to make sure it work as expected.

``scrapy parse`` can help you test your method to make sure it work fine. Here is a example

::

    scrapy parse --spider=hm --loglevel=DEBUG -c parse_product_page "http://www.hm.com/us/product/92806?article=92806-J"

Make sure to use this to test your methods and it will save your a lot of time later, trust me!

--------------
Scrapy shell
--------------

When the spider raise some error in processing specific page, you need to figure out why spider did not work as expected. You can use parse mathod talked above, or you can use ``scrapy shell`` under this circumstance. Actually, scrapy shell is so powerful that it can save us a lot of time if you can master it.

You can type ``scrapy shell`` to open scrapy shell

* use ``fetch`` to get web page and get the new response
* you can use ``response.xpath`` and ``response.css`` to test your expression in this web page, this can quickly find out the error
* you can call this ``view(response)`` to open the page in your browser

ipython
----------------

It is stronglly recommended to install ipython as well as scrapy. ipython offers introspection, rich media, shell syntax, tab completion, and history.

.. note::

    You can enter ``edit`` to input multiple lines of code to ipython shell and quickly tested it.


