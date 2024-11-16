#6#Check if File exist ?

#To avoid getting an error,
# you might want to check if
# the file exists before you try to delete it:

#Check if file exists, then delete it ?

import os
if os.path.exists("myfile0.txt"):
  os.remove("myfile0.txt")
else:
  print("The file does not exist")
  