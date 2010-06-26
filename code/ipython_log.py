#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
import issprime1
_ip.system("ls -F ")
import isprime1
isprime(2**10-1)
isprime1.isprime(2**10-1)
isprime1.isprime(2**10-2)
isprime1.isprime(2**10-3)
[isprime(n) for n in xrange(100)]
[isprime1.isprime(n) for n in xrange(100)]
map(isprime1.isprime, xrange(10))
_ip.magic("timeit map(isprime1.isprime, xrange(10000,10500))")
_ip.magic("timeit map(isprime1.isprime, xrange(10000,11000))")
_ip.magic("timeit map(isprime1.isprime, xrange(10000,15000))")
_ip.magic("timeit map(isprime1.isprime, xrange(10000,20000))")
_ip.magic("timeit map(isprime1.isprime, xrange(0,20000))")
_ip.magic("timeit map(isprime1.sumprimes, xrange(100))")
_ip.magic("timeit map(isprime1.sum_primes, xrange(100))")
_ip.magic("timeit map(isprime1.sum_primes, xrange(500))")
log
_ip.magic("logon ")
_ip.magic("logstart ")

_ip.system("ls -F ")
_ip.magic("timeit map(isprime1.sum_primes, xrange(500))")
_ip.magic("timeit map(isprime1.sum_primes, xrange(10000, 10500))")
import isprime1
[isprime1.isprime(n) for n in range(20)]
import prime1
[prime1.isprime(n) for n in range(20)]
prime1.sum_primes(100)
_ip.magic("timeit map(prime1.isprime, xrange(20000))")
_ip.magic("timeit map(prime1.sum_primes, xrange(1000,2000))")
_ip.magic("Exit ")
