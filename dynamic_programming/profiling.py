import os
import fibonacci

try:
    import cProfile as pr
except ImportError:
    import profile as pr

def format_ordinal(num):
    suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16
    return str(num) + suffixes[num % 100]

functions = [
    fibonacci.fib,
    fibonacci.m_fib,
    fibonacci.lru_fib
]

n = 32

for func in functions:
    for i in range(2):
        print(
            "Calling '%s' with n = %d, %s pass:" %
                (func.__name__, n, format_ordinal(i + 1))
        )
        input('(Press ENTER to continue)')
        code = 'fibonacci.%s(%d)' % (func.__name__, n)
        print(code)
        pr.run(code)
