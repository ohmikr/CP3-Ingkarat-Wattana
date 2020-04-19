MenuList = []
PriceList = []

def ShowBill():
    print("----Your Bill----")
    for Number in range(len(MenuList)):
        print(MenuList[Number],PriceList[Number])
    Total = str(sum(PriceList))
    print("Total", Total)
while True:
    MenuName = input("Please Enter Your Menu:")
    if(MenuName.lower() == "exit"):
        break
    else:
        MenuPrice = int(input("Price:"))
        MenuList.append(MenuName)
        PriceList.append(MenuPrice)

ShowBill()
