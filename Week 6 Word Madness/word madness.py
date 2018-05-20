##############################################################
#Rico Cintron
#2/17/2016
#Introduction to Programming
##############################################################

#Vowel list
vowels= ['a','e','i','o','u']
#loop
while True:
#Funtions and default 0s
    cmdInput = "a"
    myWord = ""               
    vowelCount = 0
    consonantCount = 0
    wordCount = 0

    while cmdInput != "q":

        valid = False

        while valid == False:
            #Input/Selection display
            cmdInput = input("Hello and welcome. Please enter [V]owels, [C]onsonants, or [Q]uit: ")
            cmdInput = cmdInput.lower()
            cmdInput = cmdInput[0]
            if cmdInput != "v" and cmdInput != "c" and cmdInput != "q":
                print("Please enter V,C, or Q only!!!")
            else:
                print("You selected the",cmdInput,"mode.")
                valid = True
                  



#Vowel/Constant incrementation, display quit option
        if cmdInput != "q":
            myWord = input("Enter words to count, [q] for quit:")
            wordCount += 1
            myWord = myWord.lower()
            print ()
            for check in myWord:
                if check in vowels:
                    vowelCount += 1
                else:
                    consonantCount += 1

        else:
            cmdInput = "q"
          




# display vowel or constant count, perform division for average
        if cmdInput == "v":
            print ("The current vowel count = ", vowelCount)
            print ("The average vowels/word= ", vowelCount/wordCount)
        elif cmdInput == "c":
            print ("This is your constant count", consonantCount)
            print ("The average constants/word= ", consonantCount/wordCount)
        else:
            print ("Quitting the program, goodbye!!!")
            sys.exit(0);






































































