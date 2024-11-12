#print the string passed into the function ?

import re

txt = "the rain in spain"

x = re.search(r"\bs\w+",txt)
print(x.string)
