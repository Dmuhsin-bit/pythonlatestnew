#Write a Python program that:

#Initializes a variable j with the value 0.

#Uses a while loop to iterate as long as j is less than 5.

#In each iteration, increase the value of j by 1.

#If j is equal to 2, use the continue statement to skip the
# rest of the loop's body and continue to the next iteration.

#Print the value of j for all other iterations.

j =0
while j < 5:
    j= j+1
    if j == 2:
        continue
    print(j)