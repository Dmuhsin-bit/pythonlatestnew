#the split() function


#the split() function
#returns a list where the string has been split at each match:

#split at each white-space character ?

import re
txt = "the rain in spain"

x = re.split("\s",txt)
print(x)

