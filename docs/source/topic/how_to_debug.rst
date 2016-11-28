====================
How to debug spider
====================

--------------------
Print log
--------------------

Log is the only way to figure out what happend when scrawl working. So I will give you some suggestion about the log.

The spider may raise exception when working due to the different html structure or something else, you might need to log the entire html souce code to analyze later. Here is an example.

:: 

    logging.info('error occur at ' + response.url)
    logging.info(response.body)

--------------------
PDB
--------------------

I do not understand why scrapy not recommend pdb over scrapy shell, in my opinion pdb is the best debuging tool when developing spider.

You can set breakpoint, conditional breakpoint in spider, inspect variable in pdb shell, and print traceback, which make debug work easier. Somebody might not know ``ipdb``. I must say ipdb add some more usefull feature to ``pdb`` and it is worthile to give it a try.
