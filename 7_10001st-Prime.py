
# SCRAP THIS & REUSE OLD CODE
# def check_if_prime(num):
#     found_composite = False
#     for x in range(num - 1, 2, -1):
#         if num % x == 0:
#             found_composite = True
def is_prime(x):
    found_composite = False
    i = 1
    while i < x - 1 and found_composite is False:
        y = x - i
        if x % y == 0:
            found_composite = True
        else:
            i += 1

    if found_composite is True:
        return False
    else:
        return True


def find_the_prime(count_to):
    count = 0
    potential_prime = 1
    while count < count_to:
        potential_prime = potential_prime + 1
        if is_prime(potential_prime):
            count = count + 1
            print(count)

    print(f"The {count_to}st Prime is: {potential_prime}")


find_the_prime(10001)
