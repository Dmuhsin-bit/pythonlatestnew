#you can control the number of replacements
# by specifying the count parameter !


# replace the first 2 occurrence ?

import re

txt = "the rain in spain"

x = re.sub("\s","9",txt,2)
print(x)
