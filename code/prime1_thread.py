import time
from pool import SimpleThreadPool
from isprime1 import isprime, sum_primes

nworkers = 2
pool = SimpleThreadPool(nworkers)

if __name__ == '__main__':
    t1 = time.clock()
    pool.map(isprime, xrange(0,10000))
    t2 = time.clock()
    print "[isprime] Total time for %i threads: %f s" % (nworkers, t2-t1)

    t1 = time.clock()
    pool.map(sum_primes, xrange(0,10000))
    t2 = time.clock()
    print "[sum_primes] Total time for %i threads: %f s" % (nworkers, t2-t1)

