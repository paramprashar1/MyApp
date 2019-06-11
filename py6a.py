def applyPromoCode(code, amount):
    if code == "FLAT 50":
        discount = amount*0.5
        print("Please pay \u20b9",amount-discount)
    elif code == "FLAT 30":
        discount = amount*0.3
        print("Please pay \u20b9",amount-discount)
    elif code == "FLAT 10":
        discount = amount*0.1
        print("Please pay \u20b9",amount-discount)
    else:
        print("No discount")

def getDiscount(code, amount):
    discount=0.0

    if code == "FLAT 50":
        discount = amount*0.5
    elif code == "FLAT 30":
        discount = amount*0.3
    elif code == "FLAT 10":
        discount = amount*0.1
    else:
        discount = 0.0
    return discount



totalBillAmt = 1000
dis = getDiscount("FLAT 50", 1000)
print("Discount is", dis)
print("Please pay",totalBillAmt-dis)

