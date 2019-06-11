# Built-Ins on strings
# Strings are IMMUTABLE
name = "Fionna Flynn"
newName = name.upper() # Modification operation creates a new string # Capitalizes all letters
print(name)
print(newName)

quote = "be exceptional"
print(hex(id(quote)))
quote = quote.capitalize()

print(hex(id(quote)))
print(quote)


names="John, Jenny, Jim, Jack, Jow"
idx=names.index("o")
print(idx)
idx=names.index("Jenny")
print(idx)
names=names.replace("J","K")
idx=names.index("K")
print(idx)
print(names.count("n",0,len(names)))
data=names.split(",")
print(data,type(data))

for n in data:
    print(n.strip())
#Removes white space

quote="Work hard and get Luckier"
data=quote.split(" ")
print(data)
# HW: In a string find a word with maximum occurrence

salutation="Mr."
firstName="George"
data=salutation+firstName
print(data)
number=(input("Enter a number"))
if number.isdigit():
    num=int(number)
    print("You entered ",number)

songName="Hello.mp3"
if songName.endswith(".mp3"):
    print("Play audio file")
else:
    print("Invalid file format")

# Explore other built ins using names.
