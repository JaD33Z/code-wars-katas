# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
# example test- test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

def find_it(seq):
    seq_size = len(seq)
    for i in range(0, seq_size):
        count = 0
        for j in range(0, seq_size):
            if seq[i] == seq[j]:
                count += 1

        if (count % 2 != 0):
            return seq[i]
    return -1