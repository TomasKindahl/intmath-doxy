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
    '''!
    @brief nextprime(n) – Returns the next prime number greater than n.
    @param n Integer search starting from.
    @return The next prime number greater than n.
    @note Example usage:\n
    `>>> nextprime(10)`\n
    `11`\n
    `>>> nextprime(14)`\n
    `17`\n
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
    '''!
    @brief primefactors(n) – Returns a list of all prime factors of n.
    @param n Integer to factor.
    @return List of prime factors of n.
    @note Example usage:\n
    `>>> primefactors(28)`\n
    `[2, 2, 7]`\n
    `>>> primefactors(100)`\n
    `[2, 2, 5, 5]`\n
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
    '''!
    @brief power(c, n) – Returns c raised to the power of n.
    @param c Base number.
    @param n Exponent (can be negative or non-integer).
    @return c raised to the power of n.
    @note Example usage:\n
    `>>> power(2, 3)`\n
    `8`\n
    `>>> power(5, -2)`\n
    `0.04`\n
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
    '''!
    @brief factorial(n) – Returns the factorial of n.
    @param n Non-negative integer to compute the factorial of.
    @return factorial of n.
    @note Example usage:\n
    `>>> factorial(5)`\n
    `120`\n
    `>>> factorial(10)`\n
    `3628800`\n
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
    '''!
    @brief fibbonacci(n) – Returns the nth Fibonacci number.
    @param n Positive integer indicating the position in the Fibonacci sequence.
    @return The nth Fibonacci number.
    @note Example usage:\n
    `>>> fibbonacci(5)`\n
    `3`\n
    `>>> fibbonacci(10)`\n
    `34`\n'''
    if n < 0:
        return None
    if n in _fib_mem:
        return _fib_mem[n]
    else:
        res = fibbonacci(n-1) + fibbonacci(n-2)
        _fib_mem[n] = res
        return fibbonacci(n-1) + fibbonacci(n-2)
def combination(n, k):
    '''!
    @brief combination(n, k) – Returns the number of combinations of n items taken k at a time.
    @param n Total number of items.
    @param k Number of items to choose.
    @return Number of combinations of n items taken k at a time.
    @note Example usage:\n
    `>>> combination(5, 2)`\n
    `10`\n
    `>>> combination(10, 3)`\n
    `120`\n
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
