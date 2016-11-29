===================
Installation guide
===================

--------------------
Clone the project
--------------------

``git clone https://github.com/michael-yin/scrapy_guru.git``

--------------------
Virtual environment
--------------------

If you have no idea what virtual environment is, please take look at https://virtualenv.pypa.io/en/stable/installation/

After you created virtual env and activated it, just ``pip install -r requirements.txt`` to install the packages needed

Now you are done with installation.

--------------------
Config
--------------------

Assign port
=================

You should assign a port of your localhost to make webapp to run. By default, we recommend you run web app at ``8000`` port

::

    cd webapp
    ./manage.py runserver 8000

Config spider_project
======================

::

    cd spider_project/spider_project
    # edit settings.py , remember to change the port number if webapp is not 8000
    WEB_APP_PREFIX = "http://127.0.0.1:8000/"

--------------------
Done
--------------------

Now you are done with installation, please read :ref:`before_start`

