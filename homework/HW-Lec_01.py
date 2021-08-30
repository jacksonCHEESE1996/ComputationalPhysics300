# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:20:38 2021

Brian Kerlin
8/29/2021
PHYS300
"""

#Write a function here to compute fibonacci number
def Fibonacci(N):
    '''
    This program is to calculate fibonacci number
    Input: N (must be a positive integer number) 
    output: the Fibonacci series
    '''

    Fib_series = []
    count = 0
    while count < N:
        if count < 2:
            Fib_series.append(1)
        else:
            Fib_series.append(Fib_series[-1] + Fib_series[-2])
        count = count + 1
    return Fib_series

#print(Fibonacci(-1))
#print(Fibonacci(1))
#print(Fibonacci(2))
#print(Fibonacci(3))
#print(Fibonacci(4))
print(Fibonacci(200))
#print(len(Fibonacci(200)))