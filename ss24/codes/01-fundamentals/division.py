#!/usr/bin/env python

### ANCHOR: naive_division
def naive_div(a, b):
    r = -1
    while a >= 0:
        a -= b
        r += 1
    return r
### ANCHOR_END: naive_division

### ANCHOR: division
def div(a, b):
    n = a.bit_length()
    tmp = b << n
    r = 0
    for _ in range(0, n + 1):
        r <<= 1
        if tmp <= a:
            a -= tmp
            r += 1
        tmp >>= 1
    return r
### ANCHOR_END: division

if __name__ == '__main__':

    ### ANCHOR: timing
    from random import randrange
    from time import perf_counter
    
    def time_division(func, na, nb, cycles=1):
        total_time = 0.0
        for i in range(0, cycles):
            a = randrange(0, na)
            b = randrange(1, nb)
    
            t_start = perf_counter()
            func(a, b)
            t_stop = perf_counter()
    
            total_time += (t_stop - t_start)
    
        return total_time / float(cycles)
    ### ANCHOR_END: timing
    
    na = 100_000
    nb = 10
    cycles = 1_000
    
    t1 = time_division(naive_div, na, nb, cycles)
    t2 = time_division(div, na, nb, cycles)
    print(f'naive_div: {t1 * 1e6:.6f} us')
    print(f'div: {t2 * 1e6:.6f} us')
