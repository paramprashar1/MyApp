#Conditional Constructs
"""
total=1055
print("Can we give 40% off as discount?",total>100)

#if

if total>=100:
    print("Flat 40% off as discount")
    disount=0.4*total
    gtotal=disount+total
    print(gtotal)
else:
    print("No discounts available")
    gtotal=total
    print(gtotal)
"""
#Ladder If
total=500

if total>100:
    disount=0.1*total
elif total>50 and total<100:
    disount=0.05*total
else:
    disount=0

print(disount)

#Nested If
isInternetOn=True
isGPSOn=False


