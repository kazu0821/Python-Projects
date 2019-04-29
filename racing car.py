from tkinter import * # Import tkinter

class AnimationDemo:
    def __init__(self):

        window = Tk() # Create a window
        window.title("Animation Demo") # Set a title
        width = 1250 # Width of the canvas
        self.canvas = Canvas(window, bg = "green", width = 1250, height = 1500)

        self.canvas.pack()
        # Starting x position
        x = 0
        self.canvas.create_rectangle(10,10,190,90,fill = "red",tags = "rect")

        x = 0
        self.canvas.create_oval(160,140,110,90,fill = "blue", tags = "oval")

        x = 0
        self.canvas.create_oval(90,140,40,90,fill = "blue", tags = "oval")

        
        # Bind canvas with mouse events
        self.canvas.bind("<Up>",self.speedUp)
        self.canvas.bind("<Down>",self.slowDown)
        self.canvas.focus_set()
        

        
        self.dx = 20
        
        self.AnimationDemo()

        window.mainloop()

    def slowDown(self,event):
        if self.dx > -200:
            self.dx -= 5
        


    def speedUp(self,event):
        if self.dx < 200:
            self.dx += 5
        
        

    def AnimationDemo(self):
        
        while True:
            
            self.canvas.move("rect",self.dx, 0)
            self.canvas.move("oval", self.dx,0)
            self.canvas.after(100) # Sleep for 100 milliseconds
            self.canvas.update() # Update canvas

            x = 0
            width = 1250
            if x < width:
                x += self.dx  # Get the current position for string


        else:

            x = 0 # Reset string position to the beginning
                
                # Redraw text at the beginning
                
            self.canvas.create_rectangle(10,10,190,90,fill = "red",tags = "rect")
            self.canvas.create_oval(160,140,110,90,fill = "blue", tags = "oval")
            self.canvas.create_oval(90,140,40,90,fill = "blue", tags = "oval")

            
        
                

            window.mainloop() # Create an event loop

 



AnimationDemo() # Create GUI
