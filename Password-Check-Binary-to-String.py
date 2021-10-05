
# ----------------------------  Password Check - Binary to String ---------------------------- #

# A wealthy client has forgotten the password to his business website,
# but he has a list of possible passwords.
# His previous developer has left a file on the server with the name password.txt.
# You open the file and realize it's in binary format.

# Write a script that takes an array of possible passwords and a string
# of binary representing the possible password.
# Convert the binary to a string and compare to the password array.
# If the password is found, return the password string, else return false;


pass_list = ['password123', 'admin', 'admin1']
bits = '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'


def decode_pass(pass_list, bits):
    # turn 'bits' string to list
    bits_ls = bits.split()
    # define an empty string to add letter by letter during iteration
    bits_as_str = ""

    for bin_value in bits_ls:
        # convert binary items to integers, base 2, decimal places
        x = int(bin_value, 2)
        # then integer to ascii letters value of that number
        y = chr(x)
        bits_as_str += y

    # check if the converted binary string matches any of the passwords in pass_list
    if bits_as_str in pass_list:
        return bits_as_str

    else:
        return False


print(decode_pass(pass_list, bits))


# output >>
#   password123


# shortened version of same solution

def decode_pass(pass_list, bits):
    bits_as_str = "".join([chr(int(i, 2)) for i in bits.split()])
    if bits_as_str in pass_list:
        return bits_as_str
    else:
        return False

