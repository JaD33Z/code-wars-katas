
# ---------------------------------------- Last Survivor ----------------------------------------- #


# You are given a string of letters and an array of numbers.
# The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
# After each removal the size of the string decreases (there is no empty space).
# Return the only letter left.

# Example:

# let str = "zbk", arr = [0, 1]
#     str = "bk", arr = [1]
#     str = "b", arr = []
#     return 'b'


# Notes:
# The given string will never be empty.
# The length of the array is always one less than the length of the string.
# All numbers are valid.
# There can be duplicate letters and numbers.



letters = "zbk"
coords = [0, 1]

def last_survivor(letters, coords):
    r_letters = list(letters)
    # turn letters into list form

    # iterate through the list of integers in coords
    for c in coords:

        # remove the letter that has a matching index of the coord value in cords
        r_letters.pop(c)

    # fill in empty spaces and return the remaining letter/letters as a string
    return "".join(r_letters)


print(last_survivor(letters, coords))


## Example output:
                    # 'b'
















