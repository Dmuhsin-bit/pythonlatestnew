def find_permutations(string, step=0):
    if step == len(string):
        print("".join(string))
    else:
        for i in range(step, len(string)):
            string_copy = [c for c in string]
            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
            find_permutations(string_copy, step + 1)
string = input("Enter a string: ")
print("All permutations of the string are:")
find_permutations(string)
