#print the part of the string where there was a match.

#the regular expression
#looks for any words that starts with an upper case "s":
import re

txt = "the rain in spain"
x = re.search(r"\bs\w+",txt)
print(x.group())

