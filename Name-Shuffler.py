
# ----------- Name Shuffler -------------- #

# Write a function that returns a string
# in which firstname is swapped with last name.

# name_shuffler('john McClane'); => "McClane john"



str_ = 'john McClane'

def name_shuffler(str_):
    x = str_.split()
    x = " ".join(x[::-1])
    return x



print(name_shuffler(str_))

# example output:

#   McClane john
