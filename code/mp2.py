"""A simple example of multiprocessing's pool API."""

import os
from multiprocessing import Pool

def f(x):
    return x**10

if __name__ == '__main__':
    p = Pool()  # default is cpu_count()

    print p.apply(f, (10,))

    result = p.apply_async(f, (10,))
    print result.get(timeout=1.0)

    print p.map(f, xrange(1001))

    result = p.map_async(f, xrange(1001))
    result.wait()
    assert result.successful(), "exception was raised."
    print result.get()

    p.close()
    p.join()