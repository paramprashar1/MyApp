file = open("py11.py","r")
print(type(file))
fileContents=file.read()

print(type(fileContents))
print()
print(fileContents)

print(len(fileContents))
print("Re read")
fileContents=file.read()
print(fileContents)
#Once read file cant be re read
#You need to opn it again
#Read a file and create a dictionary hich tells how many classes and objects exist
#KEys will be class names and values will be class counts