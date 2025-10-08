# This is a solution to the Project Euler Problem #2
# Objective: Returns the sum of all even Fibonacci numbers less than 4 million in value
# =====================================================================================
def even_fib():
    a = 1
    b = 2
    total = 2  # include 2
    while b < 4e6:
        mysum = a + b
        if mysum % 2 == 0:
            total += mysum
        a = b
        b = mysum
    print(f"Total: {total}")


even_fib()


