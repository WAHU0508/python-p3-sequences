#!/usr/bin/env python3

def print_fibonacci(length):
    my_fibonacci = []
    if (length == 0):
        print(my_fibonacci)
    elif (length == 1):
        my_fibonacci.append(0)
        print(my_fibonacci)
    elif (length == 2):
        my_fibonacci.append(0)
        my_fibonacci.append(1)
        print(my_fibonacci)
    else:
        my_fibonacci.append(0)
        my_fibonacci.append(1)
        i = 2
        while i < length:
            next_fibonacci = my_fibonacci[i - 1] + my_fibonacci[i - 2]
            my_fibonacci.append(next_fibonacci)
            i += 1
        print(my_fibonacci)
