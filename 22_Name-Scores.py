alphabetic_values = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}


def store_names(file):
    names = []
    word_open = False
    curr_name = ""
    for x in file:
        if x == '"':
            if word_open is False:
                # Start of Name
                word_open = True
            else:
                # End of Name
                word_open = False
                # process name, add to list
                names.append(curr_name)
                curr_name = ""
        elif x == ",":
            pass
        else:
            # this is a letter in the name
            curr_name = "".join([curr_name, x])
    return names


def get_alphabetic_value(name):
    # print(f"The length of {name} is {len(name)}")
    total = 0
    for x in range(0, len(name)):
        letter_value = alphabetic_values[name[x]]
        total += letter_value
    return total


def get_name_scores():
    name_scores = []
    with open('22.txt') as f:
        file_contents = f.readline()
        names = store_names(file_contents)
        names.sort()
        name_position = 1
        for name in names:
            name_score = get_alphabetic_value(name) * name_position
            name_scores.append(name_score)
            name_position += 1
        # All name scores have been obtained. Now get the final sum of all of them.
        final_total = 0
        for x in name_scores:
            final_total += x
        print(f"Final Total of all Name Scores: {final_total}")


get_name_scores()
