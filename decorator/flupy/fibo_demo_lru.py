from functools import lru_cache
from clockdeco import clock

@lru_cache() # applied last
@clock       # applied first
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(7))
