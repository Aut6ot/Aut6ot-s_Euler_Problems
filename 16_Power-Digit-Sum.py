def power_digit_sum(base, power):
    my_num = int(base ** power)
    digit_sum = 0
    my_num_len = len(str(my_num))
    for x in range(0, my_num_len):
        curr_num = int(str(my_num)[x])
        digit_sum += curr_num
    print(f"Digit_Sum: {digit_sum}")
    return digit_sum


power_digit_sum(2, 1000)
