amicable_numbers = []


def is_amicable_pair(a):
    # Check d(a) == b; then check d(b) == a. Return True.
    if a not in amicable_numbers:
        # Evaluate 'a' ==============
        a_divisors = []
        b_divisors = []
        for x in range(1, a):
            if a % x == 0:
                a_divisors.append(x)
        a_sum = sum(a_divisors)
        # Evaluate 'b' ==============
        b = a_sum
        for x in range(1, b):
            if b % x == 0:
                b_divisors.append(x)
        b_sum = sum(b_divisors)
        # Add pair to list =====================
        if a_sum == b and b_sum == a and a != b:
            amicable_numbers.append(a)
            amicable_numbers.append(b)
            return True
        else:
            return False
    else:
        return True


def sum_amicable_numbers(min_range, max_range):
    for x in range(min_range, max_range):
        is_amicable_pair(x)
    print(f"Amicable Pairs between {min_range} to {max_range}: {amicable_numbers}")
    total = sum(amicable_numbers)
    print(f"TOTAL: {total}")


sum_amicable_numbers(1, 10000)
