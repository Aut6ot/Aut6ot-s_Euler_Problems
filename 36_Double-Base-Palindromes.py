# treat the number like a string
def check_palindrome(num):
    num = str(num)
    is_palindrome = True
    start_index = 0
    end_index = -1
    # assuming start at 10 -
    if len(num) % 2 == 0:
        # if it's even
        times_to_loop = int(len(num) / 2)
    else:
        # if it's odd
        times_to_loop = int((len(num) - 1) / 2)
    for x in range(0, times_to_loop):
        if num[start_index] != num[end_index]:
            is_palindrome = False
        start_index += 1
        end_index -= 1
    return is_palindrome


def find_palindrome_sum():
    palindrome_sum = 25  # under 10 the numbers 1, 3, 5, 7, and 9 are palindromic. and i don't wanna make the edge case for them.
    curr_num = 10
    count_max = 1e6
    while curr_num < count_max:
        binary = bin(curr_num)
        binary = binary[2:]
        if check_palindrome(binary) and check_palindrome(curr_num):
            print(f"Both {curr_num} and its binary version {binary} are palindromes!")
            palindrome_sum += curr_num
        curr_num += 1
    print(f"PALINDROME SUM: {palindrome_sum}")


find_palindrome_sum()
