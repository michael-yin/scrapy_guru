===================
Installation guide
===================

--------------------
Clone the project
--------------------

``git clone the repo from github``

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

You should assign two port of your localhost to make the doc and webapp to run. By default, we recommend you to run doc at ``9000`` port and run web app at ``8000`` port

When you assign port you can launch two servic now, remember you need to open at least two terminal

::

    cd docs/build/html
    # python2
    python -m "SimpleHTTPServer" 9000
    # python3
    python -m http.server 9000

::

    cd webapp
    ./manage.py runserver 8000

Config spider_project
====================

::

    cd spider_project/spider_project
    # edit settings.py , change the port number to make the spider can visit webapp
    WEB_APP_PREFIX = "http://127.0.0.1:8000/"

