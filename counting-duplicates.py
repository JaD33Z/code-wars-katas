# Counting Duplicates

# insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can
# be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Examples:
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)

text = 'oHh8XQSiNGoooOHMfV29gRAZ44Zdurc7IelXILfpcautQQrfSFM7oXWhhUcUKBpdNAah9DPidgNcP9tAmJe6mlMk6'

def duplicate_count(text):
    dups = 0
    str = text.lower()
    x = [str.count(i) for i in str]
    text_d = dict(list(zip(str, x)))
    return sum([dups +1 for num in text_d.values() if num > 1])


print(duplicate_count(text))

#output >>> 25
