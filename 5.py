# This Solution Works for finding the example case, 1-10

# a = 1
# b = 11
# test_num = 10
#
#
# def smallest_multiple(my_int):
#     print(f"Testing {my_int}")
#     all_divide = True
#     for x in range(a, b):
#         if my_int % x != 0:
#             all_divide = False
#             break
#
#     if not all_divide:
#         smallest_multiple(my_int + test_num)
#     else:
#         print(f"Smallest Multiple of {test_num} is {my_int}")
#         return my_int
#
#
# smallest_multiple(10)

import sys
sys.setrecursionlimit(10**8)

a = 11
b = 20
test_num = 20


def smallest_multiple(my_int):
    print(f"Testing {my_int}")
    all_divide = True
    for x in range(a, b):
        if my_int % x != 0:
            all_divide = False
            break

    if not all_divide:
        smallest_multiple(my_int + test_num)
    else:
        print(f"Smallest Multiple of {test_num} is {my_int}")
        return my_int


smallest_multiple(20)


