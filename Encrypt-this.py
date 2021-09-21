
# =========================== ENCRYPT-THIS! =========================== #

# Description:

# You want to create secret messages which can be deciphered by the Decipher this! kata.
# Here are the conditions:
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter


text = "A wise old owl lived in an oak"

def encrypt_this(text):
    ls = []
    text = text.split()
    for i in text:
        if len(i) <= 1:
            i = str(ord(i))
            ls.append(i)
        elif len(i) > 2:
            i = str(ord(i[0])) + i[-1] + i[2:-1] + i[1]
            ls.append(i)
        elif len(i) == 2:
            i = str(ord(i[0])) + i[-1]
            ls.append(i)
    return " ".join(ls)


print(encrypt_this(text))


# output >>
#   65 119esi 111dl 111lw 108dvei 105n 97n 111ka




