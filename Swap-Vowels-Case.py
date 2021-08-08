

# ------------------------ Strings: Swap Vowels' Case ------------------------- #


# Challenge:
#
# Given a string, return a copy of the string with the vowels' case swapped.
#
# For this kata, assume that vowels are in the set "aeouiAEOUI".
#
# Example: Given a string "C is alive!", your function should return "C Is AlIvE!"
#
# Addendum: Your solution is only required to work for the ASCII character set.
#
# Please make sure you only swap cases for the vowels.


vowels = "aeouiAEOUI"

st = "C is alive!"


def swap_vowel_case(st):
    new_s = "".join([i.swapcase() if i in vowels else i for i in st])
    return new_s


# Or


def swap_vowel_case(st):
    new_s = ""
    for i in st:
        if i in vowels:
            x = i.swapcase()
            new_s += x
        else:
            new_s += i
    return new_s


print(swap_vowel_case(st))


# example output:

#       C Is AlIvE!

