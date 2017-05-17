#!/usr/bin/env python3

"""Time CLI didactic utility"""

from time import strftime, localtime
import calendar

commands = {}

def command(option=None):
    def decorator(f):
        initial = f.__name__[0] if option is None else option
        commands[initial] = f
        return f
    return decorator

@command('n')
def time():
    print(strftime('%H:%M:%S'))

@command()
def day():
    print(strftime('%A, %B %d, %Y'))

@command()
def month():
    calendar.prmonth(*localtime()[:2])

@command()
def year():
    calendar.prcal(localtime()[0])

def main(argv):
    if len(argv) > 1 and argv[1] in commands:
        commands[argv[1]]()
    else:
        options = '|'.join(sorted(commands))
        print(f'Usage:  {argv[0]} {options}')

if __name__ == '__main__':
    import sys
    main(sys.argv)
