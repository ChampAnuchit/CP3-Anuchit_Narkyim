def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":

        return showMenu()

    else:
        return "เข้าสู่ระบบไม่สำเร็จ"

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator(int(input("Price :")))
    elif userSelected == 2:
        return priceCalculator()


def vatCalculator(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result



def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print("ราคาสินค้ารวม vat =",end=' ')
    return vatCalculator(price1 + price2)


print(login())