#####################################################
#Rico Cintron
#Intro to Programming
#3/16/2015
#10 Functions!
#####################################################



#function 1, Request Name and Major
def printmajor():
    global name
    print("Welcome to Function 1, Enter your name and major")
    name = input("Please enter your name")
    major = input("Please enter your major")
    print ("Your name is:",name)
    print ("Your major is:",major)
    print()
#function 2,Request age, displays input.
def getAge():
    print("We have arrived at Function 2, Age input")
    age = int(input("Please enter your age"))
    return age
#function 3, works with input from function one to give a warm welcome
def argumentgrab():
    print ("Function 3")
    print ("Hello",name)
    print()

#function 4, allows number entered to be inverted
def inverseNumber():
    print ("Now at function 4, Inverse number time!")
    inumber = int(input("Please enter the number you want inverted"))
    print("Your inverted number is",inumber*-1)
    print()


#function 5, takes input for word and multiplies it by input of a number
def intargcount():
    print ("Function five!!!,Word multiplcation!")
    x = input("please enter the word you want multiplied ")
    y = int(input("please enter the number of times you want the word displayed"))
    print("Now displaying argument, will display",y,"times")
    print (x)
    print (x*y)
    print ()

#function 6, takes input integers, displays higher value or equal value
def getBiggest():
    print("We are now at Function 6!, please enter 2 numbers you want compaired")
    x = int(input("Enter first number you want compaired"))
    y = int(input("Enter second number you want compaired"))
    if x > y:
        print(x,"is bigger or same")
    else:
        print(y,"is bigger or same")
        print()
#function 7, counts upper case letters and returns that value
def strargucount():
    print ("Function 7...")
    myString = input("Please enter the word, or words, you want counted for upper case letters")
    x = sum(1 for c in myString if c.isupper())
    print (x)
    print ()
#function 8, compairs values and displays middle or most common
def middlevaluecompair():
    print ("Funtion 8 :),Please enter 3 values.Middle value or most common will be displayed after selection.")
    a = int(input("please enter the first value"))
    b = int(input("please enter the second value"))
    c = int(input("please enter the third and final value"))
    my_list = [a, b, c]
    print ('Numbers originally entered:', my_list)
    my_list.sort()
    print ('Middle or most common:', my_list[1])
    print()
#funtion 9, takes input for two words, and prints characters that are the same in both words
def matchingchar():
    x = input("Please enter first word")
    y = input("Please enter second word")
    set1 = set(x)
    set2 = set(y)
    set3 = set1.intersection(set2)
    print (set3)
    print ()
#function 11, a little bit of GUI....
def functioneleven():
    import tkinter

    class MyGUI:
        def __init__(self):
            #Create the main window widget.
            self.main_window = tkinter.Tk()

            #Create a label widget containing the text 'Thanks for using this program'!'
            self.label = tkinter.Label(self.main_window, \
                                   text='Thanks for using this program!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #Call the Label widget's pack method.
            self.label.pack()

            #Enter the tkinter main loop.
            tkinter.mainloop()

    #Create an instance of the MyGUI class
    my_gui = MyGUI()


#funtion 10
def runAll():
    #function 1
    printmajor()
    #function 2
    age = getAge()
    print("Your age is: ",age)
    print()
    #function 3
    argumentgrab()
    #function 4
    inverseNumber()
    #function 5
    intargcount()
    #function 6
    getBiggest()
    #function 7
    strargucount()
    #function 8
    middlevaluecompair()
    #function 9
    matchingchar()
    #function 11
    functioneleven()


runAll()
