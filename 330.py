#raise an exception
from logging import exception

#as a python developer you can choose to throw an exception
#if a condition occurs.
#to throw (or raise) an exception, use the raise keyword.
#raise an error and stop the program if x is lower than 0 ?

x = -1

if x < 0:
    raise exception("sorry,no numbers below zero")
