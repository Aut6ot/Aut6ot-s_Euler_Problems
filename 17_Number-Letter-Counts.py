tens = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
}

teens = {
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8
}

double_digit_prefixes = {
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6
}

TEN = 3
HUNDRED = 7
THOUSAND = 8
AND = 3


def num_letter_counts():
    # 1 - 19
    total = 0
    first_19 = sum(tens.values()) + TEN + sum(teens.values())
    twenty_thru_99 = 0
    # 20 - 99
    for first_value in range(20, 100, 10):
        # add the 20/30/40...
        twenty_thru_99 += double_digit_prefixes[first_value]
        # 21, 22...29
        for second_value in range(1, 10):
            local_sum = double_digit_prefixes[first_value] + tens[second_value]
            twenty_thru_99 += local_sum
    one_thru_99 = first_19 + twenty_thru_99
    total += one_thru_99
    # 101 - 199, 201-299, etc.
    for x in range(1, 10):
        # 'one/two/three hundred and' prefixes all numbers 101-999
        total += ((tens[x] + HUNDRED + AND) * 99) + one_thru_99
    # 100, 200...900
    hundreds = (sum(tens.values()) + (9 * HUNDRED))
    total += hundreds
    # add 1000
    total += tens[1] + THOUSAND
    print(f"FINAL TOTAL: {total}")


num_letter_counts()
