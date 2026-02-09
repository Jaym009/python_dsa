def is_palindromic_tuple(tup):
    tup_temp = []
    tup_list = list(tup)
    for i in range(len(tup_list)-1, -1, -1):
        tup_temp.append(tup_list[i]) 
    if tuple(tup_temp) == tup:
        print(True)
        return True
    else:
        print(False)
        return False
    
def is_palindromic_tuple_alternate(tup):
    return tup == tup[::-1]

def is_palindromic_tuple_alternate_reversed(tup):
    tup_reversed = tuple(reversed(tup))
    return tup == tup_reversed

is_palindromic_tuple((1, 2, 3, 2, 1))
is_palindromic_tuple_alternate((1, 2, 3, 2, 1))
is_palindromic_tuple_alternate_reversed((1, 2, 3, 2, 1))