.. doc documentation master file, created by
   sphinx-quickstart on Tue Nov  1 20:44:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Getting help
============

.. _issue tracker: https://github.com

Basic concepts
===============================

.. toctree::
    :maxdepth: 2
    :caption: Basic concepts
    :hidden:

    intro
    install
    before_start

:doc:`intro`
    Introduction of this project

:doc:`install`
    How to install and config this project

:doc:`before_start`
    Something you should know before you start

    
Advanced topic
===============================

.. toctree::
    :maxdepth: 1
    :caption: Advanced topic
    :hidden:

    topic/chrome
    topic/zaw
    topic/how_to_debug
    topic/mitmproxy

:doc:`topic/chrome`
    How to enhance your browser to make it help you develope spider

:doc:`topic/zaw`
    How to enhance your terminal shell.

:doc:`topic/how_to_debug`
    How to troubleshoot your scrapy spider.

:doc:`topic/mitmproxy`
    How to inspect your http request.

Task List
===============================

.. toctree::
    :maxdepth: 1
    :caption: Task List
    :hidden:

    tasks/basic_extract
    tasks/json_extract
    tasks/ajax_extract
    tasks/ajax_header
    tasks/meta_storeinfo
    tasks/ajax_cookie
    tasks/ajax_sign

:doc:`tasks/basic_extract`
    Understand the spider workflow and basic xpath syntax.

:doc:`tasks/json_extract`
    Learn to use json module to extract json data.

:doc:`tasks/ajax_extract`
    Learn to inspect ajax request.

:doc:`tasks/ajax_header`
    Learn to inspect http header of ajax request.

:doc:`tasks/meta_storeinfo`
    Learn to pass additional data to callback functions

:doc:`tasks/ajax_cookie`
    Learn to analyze cookie of http request.

:doc:`tasks/ajax_sign`
    Learn to analyze minified js and debug code in browser.

