def VatCal(TotalPrice):
    TotalPrice = int(input("Product Price:"))
    Result = TotalPrice+(TotalPrice*7/100)
    return Result

print(VatCal(()))