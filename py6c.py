def hello():
    print("Hello")
hello()
print("Hello is", hello)

hi = hello

# Function Overwriting

def hello():
    print("Bye")

print("Now hello is", hello)


hi = hello
del hi

hello()