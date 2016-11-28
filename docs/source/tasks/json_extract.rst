==================
Json extract
==================

------------------
Goal
------------------

Recently many websites extract from json data saved in html source. So we need to learn how to handle this situation.

You should create a spider which have name ``json_extract``

Once you finish the coding just run ``scrapy crawl json_extract --loglevel=INFO`` to check the output

------------------
Entry
------------------

Remember to change the port number if it is not 8000

http://127.0.0.1:8000/content/detail_json

------------------
taskid
------------------

taskid::

    json_extract

------------------
Detail of task
------------------

In this task we try to crawl product title and price info. You should find out that the value returned by xpath is not the one you see in your brower. Because javascript have change that.

The real data is saved in json_data.

The final data should be::

