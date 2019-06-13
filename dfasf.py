n=int(input("Enter the amt"))
promoC=''
if n>1000:
    print("The available promocodes are FLAT50, FLAT30 and FLAT10, Enter to apply")
    promoC=input()
    if promoC=='FLAT50':
        discount=0.5*n
    elif promoC=='FLAT30':
        discount=0.3*n
    elif promoC=='FLAT10':
        discount=0.1*n
    else:
        discount=0
elif n>500 and n<=1000

print(n-discount)