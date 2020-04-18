def Login():
    Username = input("Username:")
    Password = input("Password:")
    if Username == "admin" and Password == "admin1234":
        return True
    else:
        return False
def ShowMenu():
    print("Successful!")
    print("-----Ingkarat Store-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def SelectMenu():
    UserSelected = int(input(">>:"))
    return UserSelected
def VatCal():
    Price = int(input("ราคาสินค้า:"))
    Vat = 7
    Result = Price + (Price * Vat / 100)
    return Result
def PriceCal():
    Price1 = int(input("ราคาสินค้าชิ้นที่หนึ่ง:"))
    Price2 = int(input("ราคาสินค้าชิ้นที่สอง"))
    return ("Total", Price1+Price2)

Login()
ShowMenu()
SelectMenu()
    if VatCal()
    elif PriceCal()
else:
    print("Login Fail!")