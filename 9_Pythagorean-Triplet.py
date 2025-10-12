import math


def find_triplet():
    for i in range(1, 500):
        for y in range(1, 500):
            a = i
            b = y
            c = math.sqrt(a ** 2 + b ** 2)
            if a + b + c == math.floor(a + b + math.sqrt(a**2 + b**2)):
                # print(f"{a} {b} {int(c)} are a Pythagorean Triplet!")
                # print(f"sum = {a + b + c}")
                if a + b + c == 1000:
                    print(f"FOUND IT!!! a = {a}, b = {b}, c = {c}")
                    solution_product = a * b * c
                    print(f"Their product: {solution_product}")
                    solution = (a, b, c)
                    return solution


find_triplet()

