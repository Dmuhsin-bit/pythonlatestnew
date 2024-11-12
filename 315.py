#you can control the number of occurrences
#by specifying the maxsplit parameter :


#split the string only at the first occurrence ?

import re

txt = "the rain in spain"

x = re.split("\s",txt,1)
print(x)
