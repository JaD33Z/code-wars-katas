
# ------------------------------------- Sum-of-parts -------------------------------------- #


# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
#ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []



# The function parts_sums (or its variants in other languages) will
# take as parameter a list ls and return a list of the sums of its parts as defined above


# example test: 


ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]


def parts_sums(ls):
    arr = [0] * (len(ls)+1)
    for index, value in enumerate(reversed(ls)):
        arr[len(ls) - index -1] += arr[len(ls) - index] + value
    return arr


print(parts_sums(ls))


# example output:

#            [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]



