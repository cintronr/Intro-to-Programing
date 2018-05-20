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
    elif hi=="2":
      print("2.Recommend Sale")
    elif hi=="3":
      print("3.Exit")
      hi = None
    else:
       print("\n Not Valid Choice Try again")
