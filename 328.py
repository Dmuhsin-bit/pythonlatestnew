#finally
#the finally block , if specified,
#will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")
