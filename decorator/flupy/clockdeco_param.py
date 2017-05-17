# clockdeco_param.py

"""
>>> @clock()
... def snooze(seconds):
...     time.sleep(seconds)
...
>>> snooze(.1)  # doctest: +ELLIPSIS
[0.10...s] snooze(0.1) -> None
>>> clock('{name}: {elapsed}')(time.sleep)(.2)  # doctest: +ELLIPSIS
sleep: 0.20...
>>> clock('{name}({args}) dt={elapsed:0.2f}s')(time.sleep)(.2)
sleep(0.2) dt=0.20s
"""

import time
from functools import wraps

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @wraps(func)
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
