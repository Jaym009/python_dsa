def is_subset(lst1, lst2):
    # Your code goes here
    temp_list = []
    for i in lst1:
        for j in lst2:
            if i == j:
                temp_list.append(j)
                
    print(temp_list == lst1)
    return temp_list == lst1
lst1 = [1,6]
lst2 = [1,2,3,4,5]
is_subset(lst1, lst2)
