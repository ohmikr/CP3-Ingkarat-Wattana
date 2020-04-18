UserName = input("Username:")
Password = input("Password:")
PriceXS = 23000
PriceX = 19000
Price8 = 17999
Price7 = 13000
Price4 = 1500
if UserName == "admin" and Password == "admin1234":
    print("Login Successful!")
    print("**********Welcome to Ingkarat Store**********")
    print("1. Iphone XS", PriceXS, "THB")
    print("2. Iphone X",  PriceX,  "THB")
    print("3. Iphone 8",  Price8,  "THB")
    print("4. Iphone 7",  Price7,  "THB")
    print("5. Iphone 4",  Price4,  "THB")
    Product = int(input("What would you like to buy?:"))
    Quantity = int(input("How many do you want?"))
    if Product == 1:
        print("Total", Quantity*PriceXS, "THB")
        print("-----Thank You-----")
    elif Product == 2:
        print("Total", Quantity*PriceX, "THB")
        print("-----Thank You-----")
    elif Product == 3:
        print("Total", Quantity*Price8, "THB")
        print("-----Thank You-----")
    elif Product == 4:
        print("Total", Quantity*Price7, "THB")
        print("-----Thank You-----")
    elif Product == 5:
        print("Total", Quantity*Price4, "THB")
        print("-----Thank You-----")
else:
    print("Login error, Please try again")