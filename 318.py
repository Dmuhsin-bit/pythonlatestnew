#match object


#a match object is an object containing
#information about the search and the result.
#if there is no match,
#the value none will be returned, instead of the match object.

#do a search that will return a match object ?

import re

txt = "the rain in spain"
x = re.search("ai",txt)
print(x) #this will print an object
