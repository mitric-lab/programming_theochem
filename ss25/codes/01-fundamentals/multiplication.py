#!/usr/bin/env python

### ANCHOR: naive_multiplication
def naive_mul(a, b):
    r = 0
    for i in range(0, a):
        r += b
    return r
### ANCHOR_END: naive_multiplication

### ANCHOR: multiplication
def mul(a, b):
    r = 0
    for _ in range(0, a.bit_length()):
        if a & 1 != 0:
            r += b
        b <<= 1
        a >>= 1
    return r
### ANCHOR_END: multiplication

if __name__ == '__main__':
    
    ### ANCHOR: timing
    from random import randrange
    from time import perf_counter
    
    def time_multiplication(func, n, cycles=1):
        total_time = 0.0
        for i in range(0, cycles):
            a = randrange(0, n)
            b = randrange(0, n)
            
            t_start = perf_counter()
            func(a, b)
            t_stop = perf_counter()
            
            total_time += (t_stop - t_start)
    
        return total_time / float(cycles)
    ### ANCHOR_END: timing
    
    n = 100_000
    cycles = 1_000
    
    t1 = time_multiplication(naive_mul, n, cycles)
    t2 = time_multiplication(mul, n, cycles)
    print(f'naive_mul: {t1 * 1e6:.6f} us')
    print(f'mul: {t2 * 1e6:.6f} us')
