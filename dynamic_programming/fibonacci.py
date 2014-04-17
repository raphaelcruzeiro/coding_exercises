import functools

def memoize(f):
    """
    http://en.wikipedia.org/wiki/Memoization
    """
    cache = {}
    @functools.wraps(f)
    def wrapper(n):
        if n in cache:
            return cache[n]
        x = f(n)
        cache[n] = x
        return x
    return wrapper

def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

@memoize
def m_fib(n):
    if n < 2:
        return n
    return m_fib(n - 2) + m_fib(n - 1)


# https://docs.python.org/dev/library/functools.html#functools.lru_cache
@functools.lru_cache(maxsize=32)
def lru_fib(n):
    if n < 2:
        return n
    return lru_fib(n - 2) + lru_fib(n - 1)

def test():
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    assert [fib(x) for x in range(16)] == fibonacci
    assert [m_fib(x) for x in range(16)]  == fibonacci
    assert [lru_fib(x) for x in range(16)]  == fibonacci

    print('Passed!')
