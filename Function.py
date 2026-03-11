def GRNtoDollar(grn):

    doll = grn/(privat+1)
    print(grn)
    print(doll)
def DollartoGRN(doll):

    grn = doll*(privat-1)
    print(grn)
    print(doll)
privat = 54
grn = int(input("Кількість грн"))
GRNtoDollar(grn)

doll = int(input("Кількість дол"))
DollartoGRN(doll)