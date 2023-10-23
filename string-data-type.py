myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

firstString = "water"                       # Exercise 2: Working with string concatenation

secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")         # Exercise 3: Working with input strings


print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))
