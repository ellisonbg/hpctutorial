.. _conclusion:

===================
Concluding thoughts
===================

The tools
=========

* Unlike just a few years ago, there are many tools for parallelizing
  Python code. Many others (parallel Python, Disco) that we haven't mentioned.
* I get the feeling that we are still in the dark ages though.
* The GIL in CPython is hindering, but not stopping, efforts to create better tools for parallelizing
  Python code. Jython and IronPython present interesting opportunities.

Parallelizing your code
=======================

* No "one size fits all" tool or approach.
* You have to pay attention to things like bottlenecks, Amdahl's law
  and hardware architecture.
* You have to think differently about your programs.
