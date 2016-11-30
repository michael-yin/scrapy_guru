=============
Intro
=============

------------------------------------------------
Supplement instead of alternative of scrapy doc
------------------------------------------------

Scrapy doc is a good start for people who want to learn to write spider by using scrapy. Since scrapy doc mainly focus on the components and concepts in scrapy, some points which make sense in spider development with scrapy are missed in the doc. I think it is essential to add the contents here.

Scrapy doc is great enouth and it does not make much sense to create another doc which have identical content, so I did not talk much in componetns of scrapy in this doc. **It is strongly recommend user to read scrapy `official doc <https://doc.scrapy.org/en/latest/index.html>`_  first to have a basic understanding such as how to create spider and how to run spider in scrapy. You might can not get some points here if you have no idea how the spider work in scrapy** If you have question for scrapy, please check it in official doc first.

------------------------
How to use this project
------------------------

First, you should take a view of the workflow figure of this project to know how this project work and read `basic concepts <http://scrapy-guru.readthedocs.io/en/latest/#basic-concepts>`_ in doc.

Secondly user will check some simple tasks in online doc of project, actually these tasks are like `code kata <https://en.wikipedia.org/wiki/Kata_(programming)>`_ and you will get skills by doing it. User should create spider as doc asked and run the spider to get the data as expected. There is a sample spider callled ``basic_extract`` in the project, just follow it to create new one and debug. If user can not make the spider to work, you can also see the working spider code in the solution repo which I will push later.

Thirdly user can get some advaned advise or tips in `advanced topic <http://scrapy-guru.readthedocs.io/en/latest/#advanced-topic>`_ , you can learn how to enhance your browser to make it more helpful in spider development or other stuff.

--------------------
Doc
--------------------

http://scrapy-guru.readthedocs.io/en/latest/index.html

--------------------
Support Platform
--------------------

OSX, Linux, python 2.7+, python 3.4+

--------------------
Workflow
--------------------

Please click the image for better resolution.

.. image:: http://scrapy-guru.readthedocs.io/en/latest/_images/scrapy_tuto.png
    :height: 600px
    :width: 800px

--------------------
Project structure
--------------------

Here is the directory structure::

    .
    ├── docs
    │   ├── Makefile
    │   ├── build
    │   └── source
    ├── requirements.txt
    ├── spider_project
    │   ├── release
    │   ├── scrapy.cfg
    │   └── spider_project
    └── webapp
        ├── content
        ├── db.sqlite3
        ├── manage.py
        ├── staticfiles
        ├── templates
        └── webapp

* ``docs`` contains the html documentation of this project
* ``webapp`` is a web application developed by ``Django``, we can see this app as a website which show us product info and product links, and we need to write spider to extract the data from it. 
* ``spider_project`` is a project based on ``Scrapy`` which we should write spider in it to extract data from ``webapp``.

--------------------
First glance
--------------------

So here is an example product detail page, it is rendered by ``webapp`` mentioned above.

.. image:: http://scrapy-guru.readthedocs.io/en/latest/_images/first_glance.png

Now according to `task <http://scrapy-guru.readthedocs.io/en/latest/tasks/basic_extract.html>`_ in the doc, we need to extract product title and desc from the product detail page

Here is part of spider code::

    class Basic_extractSpider(scrapy.Spider):
        taskid = "basic_extract"
        name = taskid
        entry = "content/detail_basic"

        def parse_entry_page(self, response):
            item = SpiderProjectItem()
            item["taskid"] = self.taskid
            data = {}
            title = response.xpath("//div[@class='product-title']/text()").extract()
            desc = response.xpath("//section[@class='container product-info']//li/text()").extract()
            data["title"] = title
            data["desc"] = desc

            item["data"] = data
            yield item

We can run the spider now, the spider will start to crawl from the ``self.entry`` and it will check the data scraped automatically. if the data scraped have some mistake, it will give the detail of the error and help you get the spider work as expect.

-----------------------
Keep going
-----------------------

Read doc of this project for more detail and instruction

http://scrapy-guru.readthedocs.io/en/latest/index.html
