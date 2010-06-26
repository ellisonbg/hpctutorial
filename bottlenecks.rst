.. _bottlenecks:

=======================
Performance Bottlenecks
=======================

There is some computational resource (CPU cycles, memory speed,
disk IO, network IO) that prevents your program from being any faster
than it is. This is the bottleneck in the program, and you need to understand
it. More on this later.

.. warning::
    It is quite easy to assume that the bottleneck in a program is raw CPU
    cycles. But, with the architecture of today's CPUs, in particular the 
    memory subsystem, this is not always the case. Many computations are
    memory or IO bound, especially on multicore CPUs.

Bottleneck: the part of your program that is determining the execution time.
If you remove or mitigate the bottleneck, execution time will decrease. If you
don't remove or mitigate the bottleneck, execution time won't decrease
significantly no matter what you do!

Bottlenecks
===========

Raw CPU cycles
--------------

FLOPS = Floating Point Operation Per Second

Most of us start by assuming that CPU cycles

Disk IO
-------

Network IO
----------

Memory bandwidth
----------------

Give simple example of memory bandwidth.

Communication overhead
----------------------

Bottlenecks and parallel hardware architectures
===============================================

It is important to understand how these bottlenecks are affected by various
parallel hardware architectures. The hope is that parallel hardware will
remove or remediate the bottlenecks and thus improve the performance of the
program when it is parallelized. As we will see, however, in some cases
parallel hardware will worsen existing bottlenecks and even create new ones.

In the following we develop an extremely simple model of different parallel
hardware to help us understand these effects.

Single core CPU
---------------

F = FLOPs
M = Memory bandwidth
D = Disk bandwidth

Multicore CPU
-------------

C = Number of identical cores

FLOPS = C*F
Memory bandwidth per core = M/C
Disk bandwidth = D

Multiple cores increase available FLOPS.
Multiple cores don't necessarily increase memory bandwidth. Can even decrease
memory bandwidth per core.
Multiple cores don't increase disk IO
Multiple cores don't increase network IO

* Multicore CPUs will only help if you are CPU bound.
* Multicore CPUs will likely not help if you are memory bound.

Cluster or supercomputer
------------------------

A cluster of possibly multicore CPUs

N nodes, C cores each

FLOPS = N*C
Memory bandwidth per core = N/C
Disk IO = N

A cluster is amore balanced approach

GPU
---

* Great FLOPS
* Great memory bandwidth
* No IO imporovement.

GPUs only help if you are CPU or memory bound.


