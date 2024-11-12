#Create an iterator that returns numbers,
# starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5etc.)?

class mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Use for loop to automatically call next until StopIteration is raised
#for num in myclass:
#print(num)