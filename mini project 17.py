def find_key_of_max_value(input_dict):
    return max(input_dict, key=input_dict.get)

data = {'a': 10, 'b': 20, 'c': 15}
max_key = find_key_of_max_value(data)
print("Key with the maximum value:", max_key)
