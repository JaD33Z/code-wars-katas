
# --------------------- ALL-STAR-CODE-CHALLENGE --------------------- #

# Create a function named rotate() that accepts
# a string argument and returns an array of strings
# with each letter from the input string being rotated to the end.
# Note: The original string should be included in the output array The order matters.
# Each element of the output array should be the rotated version of the previous element.
# The output array SHOULD be the same length as the input string
# The function should return an emptry array with a 0 length string, '', as input




def rotate(str_):
    l = []
    k = +1
    for i in range(k, len(str_) +1):
        x = str_[i:] + str_[:i]
        l.append(x)
    return l


print(rotate("Hello"))


# example test - rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]


