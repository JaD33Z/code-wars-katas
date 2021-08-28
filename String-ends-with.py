
# ================================ String Ends With? ================================ #

# Complete the solution so that it returns true
# if the first argument(string) passed in ends with the 2nd argument
# (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


string = 'abc'
ending = 'bc'


def solution(string, ending):
    e = len(ending)
    return string[-e:] == ending or e < 1


print(solution(string, ending))


# output -
#   True

