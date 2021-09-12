
# =================================== Who likes it? =================================== #


# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing
# the names of people that like an item. It must return
# the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

names = ['Alex', 'Jacob', 'Mark', 'Max']


def likes(names):
    comments = ["likes this", "and", "like this", "no one", "others like this"]
    res = len(names)

    if res == 0:
        return f"{comments[3]} {comments[0]}"

    if res == 1:
        return f"{names[0]} {comments[0]}"

    if res == 2:
        return f"{names[0]} {comments[1]} {names[1]} {comments[2]}"

    if res == 3:
        return f"{names[0]}, {names[1]} {comments[1]} {names[2]} {comments[2]}"

    if res > 3:
        num_left = res - 2
        return f"{names[0]}, {names[1]} {comments[1]} {num_left} {comments[4]}"


print(likes(names))

# Output -
#       Alex, Jacob and 2 others like this
