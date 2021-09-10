
# ============================ Highest and Lowest ============================ #

# In this little assignment you are given a
# string of space separated numbers,
# and have to return the highest and lowest number.

# Example:

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

numbers = ("-932 242 371 698 824 336 -497 657 93 -273 23 294 38 -247 837")

def high_and_low(numbers):
    ls = []
    numbers = numbers.split()
    for i in numbers:
        x = int(i)
        ls.append(x)
    a = str(max(ls))
    b = str(min(ls))

    return f"{a} {b}"


# Shortened version:

def high_and_low(numbers):
    numbers = numbers.split()
    nums = [int(i) for i in numbers]
    return f"{str(max(nums))} {str(min(nums))}"


# Output:
#   837 -932
