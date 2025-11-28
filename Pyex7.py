#ex1

def common_elements(a, b):
    intersection = set(a) & set(b)
    return list(intersection)

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(common_elements(a, b)) 

#ex2
def remove_duplicates(seq):
    return list(set(seq))
nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))  
 
#ex3
def are_disjoint(set1, set2):
    return set(set1).isdisjoint(set(set2))
a = {1, 2, 3}
b = {4, 5, 6}
print(are_disjoint(a, b))
c={3,4}
print(are_disjoint(a, c))