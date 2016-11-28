==================
Basic extraction
==================

------------------
Goal
------------------

There are mainly two ways in scrapy to extract info from html, one is **css** and the other is **xpath**, in the code of this project I will choose xpath and I have to say there is not much difference between them, you can pick the one you prefer.

Once you finish the coding just run ``scrapy crawl basic_extract --loglevel=INFO`` to check the output

------------------
Entry
------------------

Remember to change the port number if it is not 8000

http://127.0.0.1:8000/content/detail_basic

------------------
taskid
------------------

taskid::

    basic_extract

------------------
Detail of task
------------------

In this task we extract the title, description from the entry page (above), the final data should be::

