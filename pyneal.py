# import the required module 
from tkinter import *
import tkinter.ttk as tkk 
 
# create the root window 
root = Tk() 
root.title('Resizable Window') 

# define constants for conversion from pixels to cm and inches
cm_factor = 1/37.79
inch_factor = 1/96

# this function updates the dimensions labels for resize
def updateDimensions(): 

    # get the current size in pixels
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()

    # calculate size in cm/inches
    screen_width_cm = screen_width*cm_factor
    screen_height_cm = screen_height*cm_factor
    screen_width_inch = screen_width*inch_factor
    screen_height_inch = screen_height*inch_factor

    # display size in app window
    current_dim.config(text='Currently: ' + str(screen_width) + 'x' + str(screen_height))
    displaySize_cm.config(text="Size in cm: " + str(round(screen_width_cm)) + "cm x " + str(round(screen_height_cm)) + " cm")
    displaySize_inch.config(text="Size in Inches: " + str(round(screen_width_inch)) + "in x " + str(round(screen_height_inch)) + " in")

# resize window on resize
def onResize(e): 
    updateDimensions() 

# set the initial size of the window 
root.geometry("400x300") 
 
# bind the root window and onResize()
root.bind("<Configure>", onResize)  
 
# display the dimensions 
current_dim = Label(root, text='Currently: 400x300')
current_dim.pack() 

# display size in cm
displaySize_cm = Label(root, text="Size in cm: 20cm x 10 cm ")
displaySize_cm.pack()

# display size in inches
displaySize_inch = Label(root, text="Size in Inches: 8in x 4in")
displaySize_inch.pack()

# this line should be last
root.mainloop() 
