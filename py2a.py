johnsAge=30
print(johnsAge,hex(id(johnsAge)))

jenniesAge=30
print(jenniesAge,hex(id(jenniesAge)))

#2 diff ref pointing to same location (up)

del (johnsAge)
print(jenniesAge)
