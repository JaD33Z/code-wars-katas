
# --------------------------- Even-times-last  ------------------------------ #

# Given a sequence of integers, return the sum of all the integers
# that have an even index, multiplied by the integer at the last index.
# If the sequence is empty, you should return 0



numbers = [4,700,52,2,31,1,14,45,7]



def even_last(numbers):
    if not numbers:
        return 0
    
    else:
        x = [val for key, val in enumerate(numbers) if key % 2 == 0]
        
    return sum(x) * numbers[-1]



print(even_last(numbers))



# output: 
            756
    
    
    
    
    
    
    
    
