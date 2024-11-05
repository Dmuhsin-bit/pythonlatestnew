#Task: Write a Python function called summarize_numbers
# Create a function that can take an arbitrary number of numerical arguments.
# The function should print the following:
# The total sum of the numbers.
# The average of the numbers.
# If no numbers are provided, it should print: "No numbers provided."
# Call the function with the numbers 10, 20, and 30.

def summarize_numbers(*num):
    sum = 0
    avg = 0
    if not num:
        print("No numbers provided")
        return
    else:
        for n in num:
            sum = sum + n
        avg = sum/(len(num))
        print("Sum=",sum)
        print("Average=",avg)

summarize_numbers(1,2,3,4)
summarize_numbers()