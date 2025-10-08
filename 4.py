y = 900  # min
x = 999  # max

b = y
c = x


def is_palindrome(num):
    my_str = str(num)
    length = 6
    half_len = 3
    if my_str[3] == my_str[2] and my_str[4] == my_str[1] and my_str[5] == my_str[0]:
        return True
    else:
        return False


palindrome = 9009

for z in range(y, x):
    for a in range(b, c):
        test_me = 900009
        my_num = z * a
        if is_palindrome(my_num):
            if my_num > palindrome:
                palindrome = my_num
            # print(f"{my_num}; aka {z} * {a}, is {is_palindrome(my_num)}")

print(f"Largest Palindrome Found: {palindrome}")
