def get_factorial(x):
    start_num = x
    total = x
    x -= 1
    while x > 1:
        total = total * x
        x -= 1
    print(f"The factorial of {start_num} is {total}")
    return total


def get_digit_sum(x):
    # sum of digits of x
    num_len = len(str(x))
    digit_sum = 0
    for _ in range(0, num_len):
        curr_num = int(str(x)[_])
        digit_sum += curr_num
    print(f"Digit Sum: {digit_sum}")


get_digit_sum(get_factorial(100))
