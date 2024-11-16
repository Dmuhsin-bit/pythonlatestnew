# #1-Define the Number of Rows:
# n = 5
#
# #2-Outer Loop (for each row):
# #for i in range(1, n + 1):
# #This loop iterates from 1 to n (inclusive), creating one row per iteration.
# # Each iteration builds one row of the pyramid pattern.
#
# 3-Print Spaces for Alignment:
# print(' ' * (n - i), end='')
# (n - i) calculates the number of spaces required for alignment.
# In each row, the number of spaces decreases as i increases.
# For example:
# Row 1: n - i = 5 - 1 = 4 spaces
# Row 2: n - i = 5 - 2 = 3 spaces
# Row 3: n - i = 5 - 3 = 2 spaces
# The end='' argument ensures the spaces and stars print on the same line.
# 4-Print Stars:
# print('*' * (2 * i - 1))
# 2 * i - 1 determines the number of stars in each row.
# For example:
# Row 1: 2 * 1 - 1 = 1 star
# Row 2: 2 * 2 - 1 = 3 stars
# Row 3: 2 * 3 - 1 = 5 stars
# This pattern of odd numbers (1, 3, 5, etc.) creates the pyramid shape.

