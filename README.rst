filedb
======

Create a file that pretends to be a MongoDB collection. If you try to
open the file, it will JSONify the collection and dump it back to you.

Why?
----

Because our enterprise database is file based, but our cloud based
database isn't.

...no really why?
-----------------

Files are simpler and don't break. The database operations we need to
perform aren't complicated and don't require high performance. By using
files there isn't a database that can fail. There's the added benefit
that if customers want to use different types of databases for
distributed systems, we can plug into any of them using a ``filedb`` (we
just have to make something that dumps out JSON .

Quickstart
----------

Install FUSE
^^^^^^^^^^^^

Make sure you have `FUSE <http://fuse.sourceforge.net/>`__ installed.

-  `FUSE for OSX <http://osxfuse.github.io/>`__
-  Ubuntu: ``sudo apt-get install g++ libfuse-dev``

Get mongo running
^^^^^^^^^^^^^^^^^

And you'll need a collection with some data in it.

.. code:: bash

    $ mongod

.. code:: bash

    $ mongo
    > use test
    > db.people.insert({"username": "greg"})
    > db.people.insert({"username": "phil"})
    > db.people.insert({"username": "bob"})
    > db.people.insert({"username": "samantha"})

Install filedb
^^^^^^^^^^^^^^

.. code:: bash

    $ pip install filedb

Running via python
^^^^^^^^^^^^^^^^^^

.. code:: bash

    $ filedb /tmp/tutorial/mnt/ mongodb://localhost:27017/test people

Open the file
^^^^^^^^^^^^^

.. code:: bash

    $ cat /tmp/tutorial/mnt/db
    [{ "_id": "52f104a7a0fb769e0cd0d1d4", "username": "greg" }
    { "_id": "52f104a9a0fb769e0cd0d1d5", "username": "phil" }
    { "_id": "52f104aca0fb769e0cd0d1d6", "username": "bob" }
    { "_id": "52f104aea0fb769e0cd0d1d7", "username": "samantha" }]

Running as a service
--------------------

Upstart job.

.. code:: bash

    # install the job
    $ sudo cp -R overlay/* /
    # or
    $ wget https://raw2.github.com/yhat/filedb/master/overlay/etc/init/filedb.conf
    $ sudo mv filedb.conf /etc/init/filedb.conf
    # start the job
    $ sudo start filedb

