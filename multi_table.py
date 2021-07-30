
# -------------------------------- Multiplication table for number --------------------------------- #



number = 5



def multi_table(number):
    
    return "\n".join([f"{i} * {number} = {i*number}" for i in range(1, 11)])



print(multi_table(number))



# output: 

            # 1 * 5 = 5
            # 2 * 5 = 10
            # 3 * 5 = 15
            # 4 * 5 = 20
            # 5 * 5 = 25
            # 6 * 5 = 30
            # 7 * 5 = 35
            # 8 * 5 = 40
            # 9 * 5 = 45
            # 10 * 5 = 50
            
            
