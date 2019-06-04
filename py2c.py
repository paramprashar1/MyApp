#Tuple
ages1=(10,20,30,40,50,30)
#List
ages2=[10,20,30,40,50,30]
#Set
ages3={10,20,30,40,50,30}
print(ages1,hex(id(ages1)),type(ages1))
print(ages2,hex(id(ages2)),type(ages2))
print(ages3,hex(id(ages3)),type(ages3))

#Tuple : Immutable - cant be changed - we cant add, del or update data in Runtime - Tuple is just read only
#ex the above menu bar file, edit, view

#List : Mutable - can be changed - add, del or update will work

#Set : Unique & Mutable - can't put duplicate data in set
#ex roll nos, reg nos, username

#HW How will you read data from set
# Draw mem rep of above multi value containers
print(ages1[1])
print(ages2[1])
#print(ages3[1])


