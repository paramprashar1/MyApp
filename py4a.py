"""
Sequence in Python is a MULTI Value container
List
Tuple
String
Set
Diictionary

Operations on sequence

Concatination
Repititions
Membership testing
slicing
indexing


"""
"""
students=["John","Jim","Jack","Jenny"]
print(students,type(students))

#Concat
print(students+["Fiona","George"])
print(students)

#Repitition
print(students*2)

#Membership Testing
print("John" in students)
print("Param" not in students)

#Slicing
print(students[1:4])   #begin with 1 go to less than 4
print(students[1:6])   #begin with 1 go to less than 6 

#Indexing
print(students[1])
"""

"""
students2=("John","Jim","Jack","Jenny")
print(students2,type(students2))
print(students2+("Fiona","George"))
print(students2*2)
print("John" in students2)
print(students2[1:4])   #begin with 1 go to less than 4
"""
students={"John","Jim","Jack","Jenny"}
print(students,type(students))
#print(students+{"Fiona","George"})
#print(students*2)
print("John" in students)
#print(students[1:4])   #begin with 1 go to less than 4
print(students[1])

#in sets ony memb test is supported, tuples, list support all 5 operations

