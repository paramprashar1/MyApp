# Dictionaries
employee = {"eid": 101, "name": "John", "salary": 30000}
print(employee)
# eid is key and  101 is value
print(max(employee))
print(min(employee))
print(len(employee))
employee["eid"] = 222   # updating values of keys KEYS cant be changed but there values can be
print(employee["eid"])
print(list(employee.items()))
print(list(employee.keys()))
print(list(employee.values()))

keys = list(employee.keys())
print("Keys:", keys)
for key in keys:
    print(key, "=>", employee[key])

# Explore dictionary of dictionaries
#list of dictionaries