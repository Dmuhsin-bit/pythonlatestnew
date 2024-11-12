#print the position(start- and end-position) of
#the first match occurence!


#the regular expression looks for any words
# that starts with an upper case "s" ?

import re


txt = "the rain  in spain"
x= re.search(r"bs\w+",txt)
print(x)



