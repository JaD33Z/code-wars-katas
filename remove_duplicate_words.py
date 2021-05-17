

# Your task is to remove all duplicate words
# from a string, leaving only single (first) words entries.

#  example:
s = "my cat is my cat fat"

def remove_duplicate_words(s):
    set_s = []
    s = s.split()
    for i in s:
        if i not in set_s:
            set_s.append(i)
    x = " ".join(set_s)
    return x

print(remove_duplicate_words(s))

# output = "my cat is fat"











