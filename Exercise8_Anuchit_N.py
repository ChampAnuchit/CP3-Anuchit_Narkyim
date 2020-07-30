usernameInput = input("Username :")
passwordInput = input("Password :")

#ราคาสินค้า
Price_Milk = 3
Price_Water = 2.5
Price_Tea = 2

if usernameInput == 'admin' and passwordInput == '4567':
    print("----Login successful----")
    print("List          Price")
    print("==================")
    print("1   Milk       ",Price_Milk)
    print("2   Water      ",Price_Water)
    print("3   Tea        ",Price_Tea)
    print("==================")

    userSelected = int(input("กรอกตัวเลขรายการที่เลือก >>"))
    amount = int(input("กรุณาระบุจำนวน >>"))

    if userSelected == 1:
        Price_summaryMilk = amount * Price_Milk
        print("ราคาการสั่งซื้อ = ",Price_summaryMilk)

    elif userSelected == 2:
        Price_summaryWater = amount * Price_Water
        print("ราคาการสั่งซื้อ = ", Price_summaryWater)

    elif userSelected == 3:
        Price_summaryTea = amount * Price_Tea
        print("ราคาการสั่งซื้อ = ", Price_summaryTea)
    else:
        print("ไม่มีรายการที่ต้องการ")
else:
    print("====Login error====")