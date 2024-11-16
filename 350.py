#simple pyramid pattern program in Python:
# Number of rows
n = 5

# Outer loop for each row
for i in range(1, n + 1):
    # Print spaces for alignment
    print(' ' * (n - i), end='')
    # Print stars
    print('*' * (2 * i - 1))
    