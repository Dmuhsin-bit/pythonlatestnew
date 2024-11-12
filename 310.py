#the findall() function

#the findall() function returns a list containing all matches.

#print a list of all matches ?

import re

txt = "the rain in spain"
x = re.findall("ai",txt)
print(x)
