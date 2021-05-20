# Fans of The Wire will appreciate this one.
# For those that haven't seen the show, the Barksdale Organization
# has a simple method for encoding telephone numbers exchanged via pagers:
# "Jump to the other side of the 5 on the keypad, and swap 5's and 0's."
# Here's a keypad for visualization.

# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# Write a function called decode().
# Given an encoded string, return the actual phone number in string form.

string = "4103452323"

# as list comprehension
def decode(string):
    decoded_num = ""
    return "".join([decoded_num + "5" if i == "0" else decoded_num + "0" if i == "5" else decoded_num + str(10 - int(i)) for i in string])

print(decode(string))

# output: 6957608787

# as for loop w/ conditionals
def decode(string):
    decoded_num = ""
    for i in string:
        if i == "0":
            decoded_num += '5'
        elif i == "5":
            decoded_num += '0'
        else:
            decoded_num += str(10 - int(i))
    return decoded_num

print(decode(string))

# output: 6957608787













