##########################################################################
#Rico Cintron
#Intro to Programming
#3/21/2016
#Listomainia: Week 10 
##########################################################################
#function 1, numbers entered with duplicates will be ommited
def function1():
    print("Function 1, enter numbers, duplicate numbers will be ommited")
    a = int(input("please enter 1st number you want sorted"))
    b = int(input("please enter 2nd number you want sorted"))
    c = int(input("please enter 3rd number you want sorted"))
    d = int(input("please enter 4th number you want sorted"))
    numbers = [a,b,c,d]
    print ("Entered numbers:",numbers)
    numbers = sorted(set(numbers))
    print ("Sorted",numbers)
    print ()
#function 2, allows input for numbers, numbers entered in order will provide a true value, numbers out of order will result in a false
def function2():
    print()
    print("Function 2")
    print("Please enter 5 numbers you want sorted, numbers entered in order will return true, if not in order, false will be displayed")
    a = int(input("please enter 1st number you want sorted"))
    b = int(input("please enter 2nd number you want sorted"))
    c = int(input("please enter 3rd number you want sorted"))
    d = int(input("please enter 4th number you want sorted"))
    e = int(input("please enter 5th number you want sorted"))
    list_osort = [a,b,c,d,e]        
    print ("Numbers originally entered:", list_osort)
    list_osort.sort()
    print ("Your list sorted is:",list_osort)
    if a<b and b<c and c<d and d<e:
        print ("True")
    else:
        print ("False")
#function3, takes input and provides a sum of that list
def function3():
    print()
    print("Function 3")
    print("Numbers entered will be added together")
    a = int(input("please enter 1st number"))
    b = int(input("please enter 2nd number"))
    c = int(input("please enter 3rd number"))
    d = int(input("please enter 4th number"))
    number = range
    numbers = [a,b,c,d]
    SUM= sum(numbers)
    print (SUM)
#function 4, takes 3 words or numbers, displays original values entered, prints reverse order
def function4():
    print()
    print("Function 4")
    print("Enter 3 words or numbers, list will be reversed")
    a = input("Please enter 1st word or number")
    b = input("Please enter 2nd word or number")
    c = input("Please enter 3rd word or number")
    note = [a,b,c]
    print ("Original list",note)
    note.reverse()
    print("List in reverse order",note)
#function5, takes input (3 values) for 2 lists, lists will be combined, sorted and printed
def function5():
    print()
    print("Function5")
    print("Please enter 6 numbers, 1-3 (list1) 4-6 (list2) will be combined, sorted and, displayed")
    a = int(input("please enter 1st number (first list)"))
    b = int(input("please enter 2nd number(first list)"))
    c = int(input("please enter 3rd number(first list)"))
    print()
    d = int(input("please enter 4th number(second list)"))
    e = int(input("please enter 1st number(second list)"))
    f = int(input("please enter 2nd number(second list)"))
    list1 = [a,b,c]
    list2 = [d,e,f]
    ultimatelist = list1+list2
    ultimatelist.sort()
    print (ultimatelist)
#function6, runs functions 1-5
def function6():
    function1()
    function2()
    function3()
    function4()
    function5()
    
function6()

