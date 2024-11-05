#Write a Python function called greet_friends
# that can take an arbitrary number of friend names as arguments.
# The function should print a greeting for each friend
# in the format: "Hello, [friend_name]!".
# If no names are provided,
# the function should print: "No friends to greet."
# Call the function with the names "Alice", "Bob", and "Charlie".
from multiprocessing.util import is_exiting


def greet_frnds(*frnds):
   if not frnds:
       print("NO friend to greet")

   else:
        for frnd in frnds:
            print(f"Hello {frnd}!")

greet_frnds("Alfi","Ammu","Anu")

greet_frnds()