def reciprocal_cycles():
    hi_score = 0
    d = 1
    pattern = []
    pattern_to_compare = []
    pattern_len = 1
    pattern_fractions = []
    while d < 10:
        fraction = 1 / d
        number_str = str(fraction)
        print(f"NUM: 1/{d}")
        for _ in range(2, len(number_str)):
            if bool(pattern) and number_str[_] in pattern:
                print("Pattern?")
                pattern_to_compare.append(number_str[_])
                pattern_len += 1
                pattern_fractions.append(str(1/_))
            pattern.append(number_str[_])
            print(number_str[_])
        print(f"{number_str} has a longest pattern length of {pattern_len}")
        pattern.clear()
        pattern_len = 1
        # look at the str and determine if there's a repeating pattern in numbers. keep track of the highest length of ones with patterns.
        d += 1
    print(f"POTENTIAL PATTERNS:")
    print(pattern_fractions)


reciprocal_cycles()