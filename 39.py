#you can use index number {0}
#to be sure the arguments are placed in the correct placeholders:


quantity = 3
itemno = 567
price = 49.95

myorder = "i want pay {2} dollars for {0} pieces of item {1} "

print(myorder.format(quantity,itemno,price))