
# ----------------------------------- Will-all-continents-be-represtented ---------------------------------- #


# You will be given a sequence of objects (associative arrays in PHP)
# representing data about developers who have signed up to attend the next coding meetup
# that you are organising.

# Your task is to return:

# true if all of the following continents / geographic zones

# will be represented by at least one developer:

# 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.

# false otherwise




#  example test array -

lst =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]



zones = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']



def all_continents(lst):
    arr = []
    for i in range(len(lst)):
        continent = lst[i]['continent']
        arr.append(continent)
        
        if set(arr) == set(zones):
            return True
        
    else:
        return False
  


print(all_continents())
 
    
    
# output:

        True

    
    
