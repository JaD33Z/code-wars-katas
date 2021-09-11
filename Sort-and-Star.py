
# ============================= Sort and Star ================================ #


# You will be given a vector of strings. You must sort it
# alphabetically (case-sensitive, and based on the ASCII values of the chars)
# and then return the first value. The returned value must be a string,
# and have "***" between each of its letters.
# You should not remove or add elements from/to the array.

# test.assert_equals(two_sort(["bitcoin", "take", "over", "the",
#                              "world", "maybe", "who", "knows", "perhaps"]),

# expected output -
#                  'b***i***t***c***o***i***n')


array = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]


def two_sort(array):
    sr = sorted(array)
    return "***".join(min(sr))


print(two_sort(array))


# Output :
#   b***i***t***c***o***i***n
