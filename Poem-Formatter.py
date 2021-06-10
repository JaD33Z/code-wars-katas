# Format one line string into poem layout

poem = 'Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.'

def format_poem(poem):
    return ".\n".join(poem.split('. '))

print(format_poem(poem))

# output:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
