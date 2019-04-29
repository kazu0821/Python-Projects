from tkinter import * # Import tkinter

class AnimationDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Animation Demo") # Set a title
        width = 1250 # Width of the canvas
        self.canvas = Canvas(window, bg
                             = "green", width = 1250, height = 150)

        self.canvas.pack()
        # Starting x position
        x = 0
        self.canvas.create_rectangle(10,10,190,90,fill = "red",tags = "rect")

        x = 0
        self.canvas.create_oval(160,140,110,90,fill = "blue", tags = "oval")

        x = 0
        self.canvas.create_oval(90,140,40,90,fill = "blue", tags = "oval")
    	


        
        dx = 150


        while True:
            
            self.canvas.move("rect", dx, 0)
            self.canvas.move("oval", dx,0)
            self.canvas.after(100) # Sleep for 100 milliseconds
            self.canvas.update() # Update canvas


            if x < width:
                x += dx  # Get the current position for string


            else:
                x = 0 # Reset string position to the beginning

                # Redraw text at the beginning
                x = 0
                self.canvas.create_rectangle(10,10,190,90,fill = "red",tags = "rect")
                self.canvas.create_oval(160,140,110,90,fill = "blue", tags = "oval")
                self.canvas.create_oval(90,140,40,90,fill = "blue", tags = "oval")

            
        # Bind canvas with mouse events
                self.canvas.bind("<Button-1>", self.increaseSpeed)
                self.canvas.bind("<Button-3>", self.decreaseSpeed)

        window.mainloop() # Create an event loop

    def increaseSpeed(self):
        if dx < 100:
            dx += 2
        


    def decreaseSpeed(self):
        if dx > 2:
            dx -= 2



AnimationDemo() # Create GUI
