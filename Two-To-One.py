
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string,
# the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# longest(a, b) -> "abcdefklmopqwxy"
# b = "xxxxyyyyabklmopq"
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

# example:
a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"


# shortened version

def longest(a1, a2):
    a3 = a1 + a2
    new = set(a3)
    return "".join(sorted(new))



# procedural solution

def longest(a1, a2):
    ls =[]
    ls.append(a1)
    ls.append(a2)
    x = "".join(ls)
    y = set(x)
    s = sorted(y)
    s = "".join(s)
    return s


print(longest(a1, a2))

# example output:
#               'abcdefklmopqwxy'



@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
