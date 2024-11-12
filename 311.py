#returns an empty list if no match was found !

import re

txt = "the rain in spain"
x = re.findall("portugal", txt)
print(x)
