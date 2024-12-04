def sort_dict_by_keys(input_dict):
    return dict(sorted(input_dict.items()))
data = {'b': 2, 'a': 3, 'c': 1}
sorted_by_keys = sort_dict_by_keys(data)
print("Dictionary sorted by keys:", sorted_by_keys)

def sort_dict_by_values(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))
sorted_by_values = sort_dict_by_values(data)
print("Dictionary sorted by values:", sorted_by_values)
