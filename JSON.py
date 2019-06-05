import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])




# a Python object (dict):
z= {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
t = json.dumps(z)

# the result is a JSON string:
print(t)