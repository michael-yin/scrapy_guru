======================
Enhance your browser
======================

.. _chrome-incognito:

--------------------
Incognito mode
--------------------

incognito mode is also called private mode in some browser. In this mode the browser will not send the cookies saved in normal mode , and when you open a new one, it have no cookies saved. This property make it very easy for spider development.

Because at sometime, we need to find out specific value in cookie to make spider to work, in incognito mode we can better check the value and got to know how the website might work when spider crawling from a *fresh start*.

.. _chrome-xpath-css:

-----------------------------------------------
How to quickly test my xpath or css expression
-----------------------------------------------

There are several plugin in browser to support xpath extraction. You can try ``XPath Helper`` in google chrome, which will make it easy to evaluate xpath expression on webpage.

.. image:: ../_images/xpath_helper.png

Here is how you use it. Press ``ctrl+shift+x`` to open XPath Helper, and you can see the tool bar. You can type your xpath query string in the toolbar, and the result of the xpath will show on the right side and in the web page the selected content will have a yellow backgroud, which is very easy to check if the xpath expression is right.

.. note::

    What you should concern here is that in some cases the xpath espression which indeed work in browser can not work on raw html becuase some DOM element might been modified by js, so please test it in scrapy shell before write it in spider code.

If you do not want to install extention to make this done, google chrome have built-in support to query xpath and css expression. Take a look at ``$()`` and ``$x()`` in console.

.. _chrome-web-tools:

-----------------------------------------------
How to use web dev tools
-----------------------------------------------

Here is overview screnshot about the web dev tools of google chrome, you can learn more here:  https://developers.google.com/web/tools/chrome-devtools/

.. image:: ../_images/chrome.jpg

