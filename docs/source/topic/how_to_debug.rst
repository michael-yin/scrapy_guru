====================
Troubleshoot spider
====================

--------------
Scrapy shell
--------------

scrapy shell is a scrapy command which provides us a interactive shell where we can test our code and check the output.

It is stronglly recommended to install `ipython <http://ipython.org/>`_ with scrapy. ipython offers introspection, rich media, shell syntax, tab completion, and history.

For example, when you try to solve :ref:`task_basic_extract` , you can use scrapy shell quickly test your code.

* enter ``scrapy shell`` to open scrapy shell
* use ``fetch http://127.0.0.1:8000/content/detail_basic`` to get web page we want to analyze
* you can use ``response.xpath`` and ``response.css`` to test your expression in this web page, this can quickly find out the error, in this task, we can test ``response.xpath("//div[@class='product-title']/text()").extract()``
* if the output is right, just copy the code in spider.

--------------
Scrapy parse
--------------

``scrapy parse`` can help you test your method to make sure it work fine. Here is a example

::

    scrapy parse --spider=basic_extract --loglevel=DEBUG -c parse_entry_page "http://127.0.0.1:8000/content/detail_basic"

Make sure to use this to test your methods and it will save your a lot of time later, trust me!

--------------------
Print log
--------------------

Log is the only way to figure out what really happend when scrawl working. So I will give you some suggestion about the log.

The spider may raise exception when working due to the different html structure or something else, you might need to log the entire html souce code to analyze later. Here is an example, we print the response.body in log to troubleshoot.

:: 

    self.logger.debug('error occur at ' + response.url)
    self.logger.debug(response.body)

--------------------
PDB
--------------------

I do not understand why scrapy not recommend pdb over scrapy shell, in my opinion pdb is the best debuging tool when developing spider.

You can set breakpoint, conditional breakpoint in spider, inspect variable in pdb shell, and print traceback, which make debug work easier. Somebody might not know ``ipdb``. I must say ipdb add some more usefull feature to ``pdb`` and it is worthile to give it a try.

Take a look at this great `post <https://pymotw.com/2/pdb/>`_ 
