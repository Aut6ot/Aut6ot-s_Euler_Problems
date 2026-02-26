import math


def fib(x):
    f1 = 1
    f2 = 1
    counter = 2
    num_digits = 0
    digit_max = 0
    curr_fib = 0
    while num_digits < x - 1:
        curr_fib = f1 + f2
        counter += 1
        f2 = f1
        f1 = curr_fib
        # count length of curr_fib, for the next loop
        num_digits = math.floor(math.log10(abs(curr_fib)))
        if num_digits > digit_max:
            digit_max = num_digits

    # test case - stop at 3 digits
    print(f"The index of the Fibonacci Number with {x} digits is: {counter}")


fib(1000)
