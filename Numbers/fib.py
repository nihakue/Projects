#!/usr/bin/env python
'''Simply gets a number, 
and returns the numberth number in the fibonacci sequence
'''

import sys

cache = [0, 1]

def fib(n):
    n = n - 2 # we know the first two numbers...
    while n:
        cache.append(cache[-1] + cache[-2])
        n -= 1
    print "you created a list with a memory footprint of %d \
    bytes" % (sys.getsizeof(cache))
    return cache[-1]


def main():
    num = 0
    num = int(raw_input('which number of the fibonacci sequenece do you need?\n'))
    fib_num = fib(num)
    
    if fib_num:
        print "The %sth number in the fibonacci sequence is: %d" % (num, fib_num)

if __name__ == '__main__':
    main()