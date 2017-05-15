import functools

from clockdeco import clock

@clock  # applied last
@functools.lru_cache() # applied first
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(20))
