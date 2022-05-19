# h = "         Hello World!         "
# a = "Hello World!"
# print(h)

# d = 'I said "Arsenal\'s top 4 hopes are done"'
# print(d)

# STRING INDEXING AND SLICING
# print(h[1])
#
# print(h[3:8])
#
# print(h[1:-1:3])

# Methods

# print(h.lower())
# print(h.lstrip())
# print(h.rstrip())
# print(h.strip())
# print(a.count("l"))
# print(h.upper())
# print(a.capitalize())
# print(h.replace("World", "Wereld"))
#
# a = "Mr"
# b = "Blue"
# c = "Sky"
#
# print(a + " " + b + " " + c)
#
# d = "Mambo"
# e = "Number"
# f = 5
#
# print(d + e + str(f))
#
# print(f"The next song is: {d} {e} {f}")
#
# name = "Lassie"
# years = 7
# height_cm = 60.7
#
# print(f"{name} is {years * 7} and height of {height_cm}")

# name = str(input("What's your name?\n"))
# age = int(input("How old are you?\n"))
# height = float(input("Height in metres?\n"))
#
# print(f"Hello {name}, you are {age} years old and {height} m tall. Thanks for talking to me")

h = "DFD"

print(h.isalpha()) #All string are alphabetical characters
print(h.islower()) #All lower case
print(h.isupper()) #All upper case
print(h.endswith("?")) #In the name
print(h.startswith("?")) #In the name