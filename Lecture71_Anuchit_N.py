Manulist = []
pricelist = []
totalprice = []

def ShowBill():
    print("----Myfood----")
    for i in range(len(Manulist)):
        print(Manulist[i],pricelist[i])
        totalprice.append(pricelist[i])
    print("ราคารวม :",sum(totalprice))

while True:
    manuName = input("Enter your manu :")
    if manuName.lower() == "exit":
        break
    else:
        manuPrice = int(input("Enter your Price :"))
        Manulist.append(manuName)
        pricelist.append(manuPrice)

#print(Manulist,pricelist)

ShowBill()