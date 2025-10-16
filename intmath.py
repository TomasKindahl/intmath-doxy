import math
def isprime(n):
    '''!
    @brief isprime(n) – Returns True if n is a prime number, else False.
    @param n Integer to check for primality.
    @return Boolean indicating if n is prime.
    @note Example usage:\n
    `>>> isprime(11)`\n
    `True`\n
    `>>> isprime(15)`\n
    `False`\n
    '''
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p*p <= n:
        if n % p == 0:
            return False
        p += 2
    return True
def nextprime(n):
    '''Returns the next prime number greater than n.
    examples:
    >>> nextprime(10)
    11
    >>> nextprime(14)
    17
    '''
    if n <= 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return nextprime(n-1)
    if isprime(n+2):
        return n+2
    return nextprime(n+2)
def primefactors(n):
    '''Returns a list of prime factors of n.
    examples:
    >>> primefactors(28)
    [2, 2, 7]
    >>> primefactors(100)
    [2, 2, 5, 5]
    '''
    factors = []
    p = 2
    while n > 1:
        if n % p == 0:
            factors.append(p)
            n = n // p
        else:
            p = nextprime(p)
    return factors
def power(c, n):
    '''Returns c raised to the power of n.
    examples:
    >>> power(2, 3)
    8
    >>> power(5, -2)
    0.04
    '''
    if type(n) != int:
        return math.pow(c,n)
    elif n < 0:
        return 1/power(c, -n)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return power(c*c, n//2)
    else:
        return c * power(c, n-1)
_fact_mem = {0: 1}
def factorial(n):
    '''Returns the factorial of n.
    examples
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    '''
    if n < 0:
        return None
    elif n in _fact_mem:
        return _fact_mem[n]
    else:
        res = n*factorial(n-1)
        _fact_mem[n] = res
        return res
_fib_mem = {1: 0, 2: 1}
def fibbonacci(n):
    '''Returns the nth Fibonacci number.
    examples:
    >>> fibbonacci(5)
    3
    >>> fibbonacci(10)
    34
    '''
    if n < 0:
        return None
    if n in _fib_mem:
        return _fib_mem[n]
    else:
        res = fibbonacci(n-1) + fibbonacci(n-2)
        _fib_mem[n] = res
        return fibbonacci(n-1) + fibbonacci(n-2)
def combination(n, k):
    '''Returns the number of combinations of n items taken k at a time.
    examples:
    >>> combination(5, 2)
    10
    >>> combination(10, 3)
    120
    '''
    if n == k or k == 0:
        return 1
    elif k > 0:
        return (combination(n, k-1)*(n-k+1)) // k
    elif k < n:
        return (combination(n-1, k)*n) // (n - k)
    elif n > 0 and k > 0:
        return (combination(n-1, k-1)*n) // k
    else:
        return None
