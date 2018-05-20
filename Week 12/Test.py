##############################################################################
#Rico Cintron
#Intro to programming
#3/28/2016
#Stock Portfolio 1
###############################################################################
#Allows unique name input
x = input("Please enter your name")
print()
#prints hello, name
print ("Hello,",x)
#Displays current ownership, as well as creates first dictionary
print ("You currently own the following stocks:")
Names = {"BA":"Boeing","ORCL":"Oracle","SNE":"Sony"}
#displays 1st dictionary
print (Names)
print()
print()
print("Your stock value will be listed below. Please note, 1st # listed is orginal price paid, 2nd # is current market value")
print()
#Generates buy/sell prices for aformentoned stocks
Boeingprice = [131.54,131.51]
Oracleprice = [41.18,40.77]
Sonyprice = [17.42,25.53]

#Using pricing, attatches that data to stock name
Prices = {"BA":Boeingprice,"ORCL":Oracleprice,"SNE":Sonyprice}
print (Prices)
#Displays 2nd dictionary
print()
print()
print("Additional information releating to quantity of stocks owned and risk will be displayed")
print("Quantity 1st, Risk 2nd")
#Generates quantity owned as well as, risk level of stock
EB = [1,.5]
EO = [2,.5]
ES = [8,.05]
Exposure = {"BA":EB,"ORCL":EO,"SNE":ES}
print (Exposure)
#First function, allows for name to be added(key and name)
def addName():
    print()
    print("Function: addName")
    global a
    print("Please enter the Stock Symbol and Name you want added")
    a = input("Please enter Stock Symbol")
    b = input("Please enter Stock Name")
    Names[a] = b
    print (Names)
#Second function, allows for buy and sell price to be entered
def addPrices():
    global c
    global d
    print("Function: addPrices")
    c = input("please enter buy price")
    d = input("please enter current value")
    NewItemPrice = [c,d]
    Prices[a] = NewItemPrice
    print (Prices)
    print()
#Third function, allows for input of stocks owned and risk level
def addExposure():
    global e
    global f
    print ("Function addExposure")
    e = input("Please enter stocks owned")
    f = input("Please enter risk level")
    NewItemExposure = [e,f]
    Exposure[a]= NewItemExposure
    print(Exposure)
    print ()
#funtion that adds stock
def addStock():
    print ("Function addStock")
    addName()
    addPrices()
    addExposure()
    print ()
#main function, allows for two stock keys and names to be created, also, no parameters. Displays up to date Names, Prices and Exposure.
def main():
    print("Function main")
    print()
    print("Displaying updated stock names") 
    print(Names) 
    print()
    print("Displaying updated stock prices")
    print(Prices)
    print()
    print("Displaying updated stock exposure")
    print(Exposure)
    hi=True
    while hi:
        print("""
        1.Add Stock
        2.Recommend a Sale
        3.Exit
        """)
        hi=input("What would you like to do? ")
        if hi=="1":
          print("1.Add Stock")
          addStock()
        elif hi=="2":
          print("2.Recommend Sale")
          GetSale()
        elif hi=="3":
          print("3.Exit")
          hi = None
        else:
           print("\n Not Valid Choice Try again")
def GetSale():
    BoeingExpectedSaleValue =((131.51-131.54)- .5*131.51)*1
    print ("Boeing expected sale value",BoeingExpectedSaleValue)
    SonyExpectedSaleValue=((40.77-41.18)- .05*40.77)*8
    print ("Sony expected sale value",SonyExpectedSaleValue)
    OracleExpectedSaleValue=((25.53-17.42)- .5*25.53)*2
    print ("Oracle expected sale value",OracleExpectedSaleValue)
    if BoeingExpectedSaleValue < SonyExpectedSaleValue < OracleExpectedSaleValue:
        print("Highest value is Oracle:",OracleExpectedSaleValue)
    else:
        print ("Wrong order")
##    AddedstockExpectedSaleValue= ((c-d)-f*c)*e
##    print(AddedstockExpectedSaleValue)

    
#runs addstock and main

main()



