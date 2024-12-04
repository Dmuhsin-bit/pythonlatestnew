def merge(dict1,dict2):
    merge_dict = dict1.copy()
    merge_dict.update(dict2)
    return merge_dict

dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5}
result=merge(dict1,dict2)
print("merged dictionary:",result)
