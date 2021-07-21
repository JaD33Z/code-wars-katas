## SQUARE ALL DIGITS

# Welcome. In this kata, you are asked to square every digit
# of a number and concatenate them.

# For example, if we run 9119 through the function,
# 811181 will come out, because 92 is 81 and 12 is 1.


# List comprehension solution (more 'pythonic' way...):

num = 9119

def square_digits(num):
    st_ls = [int(i) ** 2 for i in str(num)]
    i_ls = "".join([str(y) for y in st_ls])
    return int(i_ls)

# output:
#   811181


# Standard procedural solution, iteration with for loops:

num = 9119
ls = []
ys = []

def square_digits(num):
    new_num = str(num)
    for i in new_num:
        x = int(i)**2
        ls.append(x)
    for y in ls:
        x = str(y)
        ys.append(x)
    h = "".join(ys)
    return int(h)

# output:
#   811181
