# read in 1st 10 digits. add to total. move to next sequence.
total = 0
add_me = 0

with open("nums.txt") as sum_file:
    for x in range(1, 101):
        add_me = int(sum_file.readline())  # TURN INTO INT!!!
        total += add_me
        # print(f"add_me on line {x} is {add_me}")
        print(f"R_TOTAL: {total}")
    print(f"F_TOTAL: {total}")
