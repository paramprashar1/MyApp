n=int(input())

for i in range(1,n+1):
    ah=hex(i)
    ah2=ah.strip("0x")
    ab=bin(i)
    ab2=ab.strip('0b')
    ao=oct(i)
    ao2=ao.strip("0o")
    print(i," ",ao2," ",ah2," ",ab2)


