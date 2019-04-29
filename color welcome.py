from tkinter import* # Import all defeinitions from tkinter






class radio:
    




    def __init__(self):
        
        window = Tk() #create a window
        window.title("radio buttons and buttons")
    	#set a title






        #Add a check button
        frame1 = Frame(window)# Create and add a frame to window




        frame1.pack()




        self.v1 = StringVar()












# define color



        rbRed = Radiobutton(frame1,text = "Red", bg = "red",




                        	variable = self.v1, value = "r",




                        	command = self.processRadiobutton)


        rbYellow = Radiobutton(frame1,text = "Yellow", bg = "yellow",




                        	variable = self.v1, value = "y",




                        	command = self.processRadiobutton)








        rbWhite = Radiobutton(frame1,text = "White", bg = "white",




                        	variable = self.v1, value = "w",




                        	command = self.processRadiobutton)






        rbGray = Radiobutton(frame1,text = "Gray", bg = "gray",




                        	variable = self.v1, value = "g",




                        	command = self.processRadiobutton)








        rbGreen = Radiobutton(frame1,text = "Green", bg = "green",




                        	variable = self.v1, value = "gr",




                        	command = self.processRadiobutton)




        rbRed.grid(row = 1, column = 1)




        rbYellow.grid(row = 1, column = 2)




        rbWhite.grid(row = 1, column = 3)




        rbGray.grid(row = 1, column = 4)




        rbGreen.grid(row = 1, column = 5)




    	




   	#add A Label, an entry, a button, and a message to frame1
    	




        frame2 = Frame(window)# create and add a frame to window




        frame2.pack()

        


        self.label = Label(frame2, text = "Welcome",width = 50,height = 2,
                           bg = "white")
        
         
        
                    





        self.label.grid(row = 2,column =3 )

       
                        








    	# add a Label




        frame3 = Frame(window)#create and add a frame to window




        frame3.pack()




        Left = Button(frame3, text = "<=",command = self.displayLeft)




        Right = Button(frame3, text = "=>",command = self.displayRight)


        Left.grid(row = 3,column = 2)
        Right.grid(row = 3, column = 3)


        window.mainloop()# create an event loop


    
# paint a background color
    def processRadiobutton(self):
        if self.v1.get() == 'r':
            self.label["bg"] = "red"
        elif self.v1.get() == 'y':
            self.label["bg"] = "yellow"
        elif self.v1.get() == 'w':
            self.label["bg"] = "white"
        elif self.v1.get() == 'g':
            self.label["bg"] = "gray"
        elif self.v1.get() == 'gr':
            self.label["bg"] = "green"





    def displayLeft(self):
        Left.grid(frame2,row = 2,column = 1)

        
    def displayRight(self):
        Right.grid(frame2,row = 2, column = 5)





radio()#create GUI








