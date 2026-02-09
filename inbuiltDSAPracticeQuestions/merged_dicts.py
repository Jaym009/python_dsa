def merge_dictionries(dicts):
    merged_dict = {}
    for dictionary in dicts:
        merged_dict.update(dictionary)
    print(merged_dict)
    return merged_dict

def merge_dictionries_with_sum(dicts):
    merged_dict = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value
    print(merged_dict)
    return merged_dict

merge_dictionries([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5}])
merge_dictionries_with_sum([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5}])