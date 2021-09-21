
# ================ Safen User Input Part I - HTML Special Chars =================== #


# Your mission is to implement a function htmlspecialchars()
# that converts the following potentially harmful characters:

# < --> &lt;
# > --> &gt;
# " --> &quot;
# & --> &amp;


data = "<h2>Hello World</h2>"

char_dict = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}


def html_special_chars(data):
    return "".join([char_dict[i] if i in char_dict else i for i in data])


print(html_special_chars(data))


# output >>
#   &lt;h2&gt;Hello World&lt;/h2&gt;
