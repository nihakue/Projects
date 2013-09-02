#!/usr/bin/env python

cache = {0:0, 1:0, 2:1}

def fib(n):
    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

def main():
    fib_num = 0
    fib_num = int(raw_input('which number do you need?\n'))
    numth_num = str(fib(fib_num))
    
    if fib_num:
        print "the %dth number in fib is: %d" % (fib_num, fib(fib_num))

if __name__ == '__main__':
    main()