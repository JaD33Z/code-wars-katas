# Implement a function that receives two IPv4 addresses,
# and returns the number of addresses between them
# (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings.
# The last address will always be greater than the first one.

# example test - ips_between("20.0.0.10", "20.0.1.0")  ==  246

def ips_between(start, end):
    ip_sum = 0
    addr_span = [int(b) - int(a) for a,b in zip(start.split("."), end.split("."))]
    for i in addr_span:
        ip_sum =  ip_sum * 256
        ip_sum = ip_sum + i
    return ip_sum