def sum_square_difference():
    sum_of_squares = 0
    square_of_sum = 0
    for x in range(1, 101):
        sum_of_squares = sum_of_squares + x**2
        square_of_sum = square_of_sum + x
        print(f"{square_of_sum}, {sum_of_squares}")

    ans = (square_of_sum ** 2) - sum_of_squares
    print(f"{square_of_sum ** 2}, {sum_of_squares}")
    print(f"Answer: {ans}")


sum_square_difference()
