
# ================================= The Observed PIN ================================= #

# Alright, detective, one of our colleagues successfully observed our target person,
# Robby the robber. We followed him to a secret warehouse,
# where we assume to find all the stolen stuff.
# The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘

# He noted the PIN 1357, but he also said, it is possible that each of the digits
# he saw could actually be another adjacent digit (horizontally or vertically,
# but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
# And instead of the 5 it could also be the 2, 4, 6 or 8.

import itertools

observed = "369"

pin_dict = {
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["5", "7", "8", "9", "0"],
    "9": ["6", "8", "9"],
    "0": ["0", "8"]
}


def get_pins(observed):
    # makes list of matching values for each item in the string
    item_vals = [pin_dict[i] for i in observed]

    # makes list of tuples containing all possible combinations according to item values
    val_combos = list(itertools.product(*item_vals))

    # joins items in each tuple and returns them as a list of individual strings
    return ["".join(n) for n in val_combos]


print(get_pins(observed))


# output >>
#   ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']



