
# ================================ Character with longest consecutive repetition ================================ #


# For a given string s find the character c (or C)
# with longest consecutive repetition and return:
# (c, l) = ('', 0)

# example tests -

# ["aaaabb", ('a', 4)],
# ["bbbaaabaaaa", ('a', 4)],
# ["cbdeuuu900", ('u', 3)],
# ["abbbbb", ('b', 5)],
# ["aabb", ('a', 2)],
# ["ba", ('b', 1)],
# ["", ('', 0)],


chars = "bbbaaaaabbbbaa"



def longest_repetition(chars):
    x = len(chars)
    count = 0
    res = ""
    for i in range(x):
        occurs = 1
        for j in range(i + 1, x):
            if (chars[i] != chars[j]):
                break
            occurs += 1
        if occurs > count:
            count = occurs
            res = chars[i]
    return res, count



print(longest_repetition(chars))
    # output = ('a', 5)

