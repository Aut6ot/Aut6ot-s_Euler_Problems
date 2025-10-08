# BIG_PRIME = 13195
BIG_PRIME = 600851475143
MEGA_PRIME = 600851475143  # 600b!
prime_factors = []


def check_if_prime(x):
    found_composite = False
    i = 1
    while i < x - 1 and found_composite is False:
        y = x - i
        print(f"{x} % {y} == {x % y}")
        if x % y == 0:
            found_composite = True
            print(f"Found a Composite!!! ({x})")
        else:
            i += 1

    if found_composite is True:
        return False
    else:
        print(f"Found a Prime!!! ({x})")
        return True


def find_prime_factors(alpha_prime):
    finished = False
    beta_prime = 2
    while not finished:
        # check_if_prime(beta_prime)
        # Generate new prime
        while not (check_if_prime(beta_prime)):
            beta_prime += 1
        print(f"beta_prime is {beta_prime}")
        if alpha_prime % beta_prime == 0:
            print(f"Found a factor! {beta_prime}")
            prime_factors.append(beta_prime)
            finished = True
            # recursion!!!
        else:
            beta_prime += 1

# while find_prime_factors(x) --> x is False


def all_together(start_num):
    while check_if_prime(start_num) is False:
        find_prime_factors(start_num)
        new_num = start_num / prime_factors[-1]
        start_num = new_num
    prime_factors.append(start_num)
    print(f"Reached the end with a final start_num of: {start_num}")


# # find a way to make this into a loop or function
# find_prime_factors(BIG_PRIME)  # 13,195
# a = BIG_PRIME / prime_factors[-1]
# find_prime_factors(a)  # 2,639
# b = a / prime_factors[-1]
# find_prime_factors(b)  # 377
# c = b / prime_factors[-1]
# find_prime_factors(c)  # 29
#
# if c % prime_factors[-1] == 0 and c > prime_factors[-1]:
#     find_prime_factors(c / prime_factors[-1])
# else:
#     print(f"Reached the end! Cannot divide {c} by {prime_factors[-1]}")

all_together(BIG_PRIME)

print("Primes Factors Found:")
for _ in prime_factors:
    print(_)
