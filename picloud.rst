.. _picloud:

=======
PiCloud
=======

Overview
========

The cloud API
=============

Configuration
-------------

:attr:`cloud.start_simulator(force_restart=False)`
    Run the cloud locally using multiprocessing.

:attr:`cloud.setkey(api_key, api_secretkey)`
    Configure your cloud account.

Task submission and control
---------------------------

:attr:`cloud.call(func, *args, **kwargs)`
    Call ``func(*args)`` on the cloud and return a job id.

:attr:`cloud.map(func, *sequences)`
    A parallel version of Python's built-in :func:`map` function.

:attr:`cloud.result(jids, timeout=None)`
    Return the result of job or jobs. Calls :func:`cloud.join` internally.

:attr:`cloud.iresult(jids, timeout=None)`
    Like :func:`cloud.result` but returns an iterable.

:attr:`cloud.status(jids)`
    Get the status of the job or jobs.

:attr:`cloud.kill(jids)`
    Kill the job or jobs.

:attr:`cloud.join(jids, timeout=None)`
    Wait for the job or jobs to complete.

Files
-----

:attr:`cloud.files.put(file_path)`
    Send a local file to the cloud filesystem. Works from the cloud as well.

:attr:`cloud.files.get(file_name)`
    Retrieve a file from the cloud filesystem. Works from the cloud as well.

:attr:`cloud.files.delete(file_name)`
    Delete a file by name from the cloud filesystem.

When to use PiCloud
===================

* You don't own a cluster or supercomputer and don't want to purchase and
  maintain one.
* You do have money to spend.
* You don't mind using a partially proprietary solution.
* You want something that "just works" with EPD.
* You can live with high latency (your tasks take well over 1 second).
* You can get your modules and packages uploaded and running on their servers.

Examples
========

Prime numbers
-------------

Random matrices
---------------