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
