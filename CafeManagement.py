import datetime


menu={'vada':15,'samosa':15,'coffee':20,'tea':20,'freshjuice':50,'candy':10}
print("ABC Cafe".center(20))
print(" Menu ".center(20,'-'))
for items,price in menu.items():
    pricelist=str(price)
    print(items.capitalize(),pricelist.rjust(20-len(items)))
print("")
print("Your, Order Please!")
print("\n")
totalamount=0
orderlist={}
while(True):
    ordereditem=input("Enter your order:  ")
    if ordereditem.lower() in menu:
        totalamount+=menu[ordereditem]
        if ordereditem in orderlist:
           orderlist[ordereditem]+=1
        else:
            orderlist[ordereditem]=1
        anotherorder=input("Do you anything else?(Yes/No)   ")
        if anotherorder.lower() =='yes':
           continue
        if anotherorder != 'yes':
            break
    else:
        print("Sorry! We don't have this.")
        continue
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("\n\n")
print("ABC coffee".center(40))
print("Orders confrimed at: ",formatted_datetime)
print('-'*43)
for items,price in orderlist.items():
    print(items,str(price).rjust(40-len(items)))
print('-'*43)
print("Total Amount:","".join(["Rs.",str(float(totalamount)).rjust(27)]))
        

