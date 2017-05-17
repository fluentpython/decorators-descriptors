from __future__ import print_function

import sys
from timeit import timeit
from glob import glob

from imp import reload

REPEAT = 10**5
SETUP = '''from bulkfood import LineItem'''
CMD = '''
seed = LineItem('sesame seed', 250, 5.30)
t = seed.subtotal()
for i in range(20):
    p = seed.price
    if i % 10 == 0:
        seed.price = p * 1.1
        t = seed.subtotal()
'''

print('Creating %s instances in each step' % REPEAT)
print()
print('-----  -----  -----------')
print('step   time   inst/second')
print('-----  -----  -----------')
for i, dir_name in enumerate(glob('?')):
    sys.path.append(dir_name)
    if i == 0:
        import bulkfood
    else:
        reload(bulkfood)
    t = timeit(CMD, SETUP, number=REPEAT)
    print('  %s    %.3f %11d' % (dir_name, t, REPEAT/t))
    sys.path.pop()
print('-----  -----  ------------')
