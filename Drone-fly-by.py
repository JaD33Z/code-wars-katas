
# You will be given two strings: lamps and drone.
# lamps represents a row of lamps, currently off, each represented by x.
# When these lamps are on, they should be represented by o.
# The drone string represents the position of the drone T (any better suggestion for character??)
# and its flight path up until this point =. The drone always flies left to right,
# and always begins at the start of the row of lamps. Anywhere the drone has flown,
# including its current position, will result in the lamp at that position switching on.

# Return the resulting lamps string.


def fly_by(lamps, drone):
    if len(lamps) > len(drone):
        span = len(lamps) - len(drone)
        off = -1 * int(span)
        string = ["o" for i in lamps[0:off]]
        left = -1 * off
        string.append("x" * left)
        new_string = "".join(string)
        return new_string

    else:
        other = ["o" for i in lamps[::-1]]
        return "".join(other)