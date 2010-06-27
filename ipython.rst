.. _ipython:

=======
IPython
=======

Overview
========

IPython is an interactive computing environment for Python. You may already be
familiar with its enhanced interactive Python shell that has been used
throughout this tutorial:

.. sourcecode:: ipython

    $ ipython
    Enthought Python Distribution -- http://code.enthought.com

    Python 2.6.5 |EPD 6.2-1 (32-bit)| (r265:79063, May 28 2010, 15:13:03) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.10 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object'. ?object also works, ?? prints more.

    In [1]: import math

    In [2]: math.sqrt?
    Type:		builtin_function_or_method
    Base Class:	<type 'builtin_function_or_method'>
    String Form:	<built-in function sqrt>
    Namespace:	Interactive
    Docstring:
        sqrt(x)
    
        Return the square root of x.

The IPython interactive shell has a number of popular features including:

* Tab completion.
* Access to previous results (``_10``).
* Magic command system (``%magic``).
* Easy access to the system shell (``!ls``).
* Easy access to documentation (``foo?``) and source code (``foo??``).

IPython also has an architecture for interactive parallel computing. This
section of the tutorial describes that aspect of IPython.

Architecture description
========================

Like multiprocessing, IPython uses processes for parallelism. IPython's 
parallel computing framework consists of three main components:

Engine
    IPython processes that execute Python code received over a network.
Controller
    A central process that manages a set of engines, presenting those engines
    to clients through a variety of interfaces.
Client
    A high-level class you will use in your code to interact with the engines
    through different interfaces.

Here are some other highlights of IPython's parallel computing framework:

* Full support for message passing using MPI or 0MQ. But MPI is not a
  dependency.
* Extensible integration with popular batch systems (ssh, PBS, mpiexec,
  Windows HPC Server 2008 (upcoming release), SGE (coming soon)).
* Rock solid, capabilities based security model that has been audited by the
  DoD.
* Designed for and tested on traditional clusters and supercomputer with 
  locked down security and firewalls.
* Lots of dependencies, but they come with EPD.

To perform a parallel computation using IPython, you will need to:

1. Start an IPython cluster (1 controller + multiple engines) using the
   :command:`ipcluster` command.
2. In the code you want to parallelize, create a
   :class:`MultiEngineClient` or
   :class:`TaskClient` class to connect to and interact with
   the cluster.

I now describe these steps in more detail.

Startup an IPython cluster
==========================

For the purposes of this tutorial, we will focus on running an IPython cluster
on a single host with a multicore CPU. In this context, you can start a
cluster with a controller and two engines using the :command:`ipcluster`
command as follows:

.. code-block:: bash

    $ ipcluster local -n 2

Once this is done, you can open a second terminal, startup IPython and begin
to interact with the cluster:

.. sourcecode:: ipython

    In [1]: from IPython.kernel import client

    In [2]: mec = client.MultiEngineClient()

    In [3]: mec.get_ids()

    Out[3]: [0, 1]


    In [4]: mec.execute('print "Hello world!"')

    Out[4]: 
    <Results List>
    [0] In [1]: print "Hello world!"
    [0] Out[1]: Hello world!

    [1] In [1]: print "Hello world!"
    [1] Out[1]: Hello world!


.. note:: 
    The only thing that changes when running parallel IPython on a cluster or
    supercomputer is how the controller and engines are started. The
    :command:`ipcluster` command contains the logic for starting them in
    different contexts. However, once the controller and engines have started,
    everything is the same. This allows you to write your code once, and then
    run on multicore CPUs, cluster and supercomputers.

Multiengine interface
=====================

There are currently two clients for working with an IPython cluster:

:class:`IPython.kernel.client.MultiEngineClient`
    This client gives direct, explicit access to each engine. When using this client, the user
    has full control over which engine executes code or receives a Python 
    object.
    
:class:`IPython.kernel.client.TaskClient`
    This client hides the identities of the engines from the user behind
    a dynamic load balancing.

Here is an overview of the API for 
:class:`IPython.kernel.client.MultiEngineClient`:

Creation and control
--------------------

:class:`MultiEngineClient(furl_or_file='')`
    Create a multiengine client by a FURL or a FURL containing file.

:attr:`MultiEngineClient.targets`
    The target engines to apply all commands to (``'all'``, or a list of ids).

:attr:`MultiEngineClient.block`
    Should all commands block or not.

:attr:`MultiEngineClient.get_ids()`
    Get the ids of the active engines.

Code execution
--------------

:attr:`MultiEngineClient.execute(lines, targets=None, block=None)`
    Execute lines of Python code (as strings) on target engines.

:attr:`MultiEngineClient.map(func, *sequences)`
    Parallel version of Python's builtin map. No load balancing.

Data movement
-------------

:attr:`MultiEngineClient.push(namespace, targets=None, block=None)`
    Push a dict of keys and values into the namespace of target engines.

:attr:`MultiEngineClient.pull(keys, targets=None, block=None)`
    Pull values by keys from the namespace of target engines.

:attr:`MultiEngineClient.push_function(namespace, targets=None, block=None)`
    Same as :meth:`push`, but for functions.

:attr:`MultiEngineClient.puLL_function(keys, targets=None, block=None)`
    Same as :meth:`pull`, but for functions.

:attr:`MultiEngineClient.scatter(key, sequence, targets=None, block=None)`
    Scatter the sequence to target engines as key.

:attr:`MultiEngineClient.gather(key, targets=None, block=None)`
    Gather the sequence named key from the target engines.

Task interface
==============

Task client
-----------

:class:`IPython.kernel.client.TaskClient(furl_or_file='')`
    Create a task client for a FURL or file containing a FURL.

:attr:`TaskClient.run(task, block=False)`
    Run a task on the cluster and return its task id.

:attr:`TaskClient.get_task_result(taskid, block=False)`
    Get a task's result by task id.

:attr:`TaskClient.barrier(taskids)`
    Wait for a set of tasks to complete.

Task objects
------------

:class:`IPython.kernel.client.MapTask(func, args=None, kwargs=None)`
    Create a task by a function and its arguments. The task result
    is simply ``func(*args, **kwargs)``.

:class:`IPython.kernel.client.StringTask(code, pull=None, push=None)`
    Create a task using lines of python code and data to push as
    input and pull as results.

When to use IPython
===================

* You want to scale from multicore CPUs to cluster and supercomputers.
* You want to run on systems with batch systems.
* You want a high level API, but still want MPI integration.
* You don't mind the extra dependencies of IPython.
* You want everything to be usable interactively.
* You have the time and effort to learn a complex API.

Examples
========

Prime numbers
-------------

Random matrices
---------------