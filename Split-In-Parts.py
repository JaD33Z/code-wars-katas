
# ==================================== Split In Parts  ==================================== #


# Split the below string into other strings of size #3
#
# 'supercalifragilisticexpialidocious'

# Will return a new string
# 'sup erc ali fra gil ist ice xpi ali doc iou s'
# Assumptions:

# String length is always greater than 0
# String has no spaces
# Size is always positive



s = "supercalifragilisticexpialidocious"
part_length = 3


def split_in_parts(s, part_length):
    return " ".join([s[i:i + part_length] for i in range(0, len(s), part_length)])



## Or:



def split_in_parts(s, part_length):
    ls = []
    for i in range(0, len(s), part_length):
        ls.append(s[i:i + part_length])
    new_ls = " ".join(ls)
    return new_ls


print(split_in_parts(s, part_length))

# example output:

#     sup erc ali fra gil ist ice xpi ali doc iou s


