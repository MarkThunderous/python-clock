from tkinter import *   # Library that creates a window application for the program
import math    # Mathematical functions library
import datetime  # Time functions library

def x_coordinate(length, angle): # Function to find the x coordinate
    return width / 2 + length * math.cos(angle * math.pi / 180) # Formula

def y_coordinate(length, angle): # Function to find the y coordinate
    return height / 2 - length * math.sin(angle * math.pi / 180)  # Formula

width = 400     # Program width
height = 400    # Program height
radius = 150    # Radius of the oval inscribed in the square

root = Tk() # Window program
root.title("Clock")  # Program name

canvas = Canvas(root, width=width, height=height)    # Widget settings
canvas.pack()    # Widget packaging

canvas.create_oval(
width/2-radius, height/2-radius,
width/2+radius, height/2+radius) # Coordinates of the square in which the oval (circle) is inscribed

seconds = canvas.create_line(0, 0, 0, 0, fill="red") # Second hand
minutes = canvas.create_line(0, 0, 0, 0,) # Minute hand
hours =   canvas.create_line(0, 0, 0, 0,) # Hour hand

def change_hand(length, time, clock_hand, degree): # Setting the hands
    alpha = 90 - time * degree
    x1 = x_coordinate(0, alpha)
    y1 = x_coordinate(0, alpha)
    x2 = x_coordinate(length, alpha)
    y2 = y_coordinate(length, alpha)
    canvas.coords(clock_hand, x1, y1, x2, y2) # Setting each hand coordinate

def update(): # Function that updates the hands
    time = str(datetime.datetime.now())
    sec = int(time[17:19]) # seconds
    mmin = int(time[14:16]) # minutes
    hr =  int(time[11:13]) # hours

    change_hand(radius - 20, sec, seconds, 6)
    change_hand(radius - 40, mmin, minutes, 6)
    change_hand(radius / 2, hr, hours, 30)

    root.after(10, update) # Calls the function again every 10 ms

alpha = 60 # Angle
for i in range(1, 13): # Positioning of digits
    canvas.create_text(x_coordinate(radius+20, alpha), y_coordinate(radius+20, alpha), text=i,
                                        fill="blue", font="Times 10 italic bold") # Clock face parameters
    alpha -= 30 # Position each digit every 30 degrees

for i in range(60): # Graduation marks between minutes
    x1 = x_coordinate(radius, alpha)
    y1 = y_coordinate(radius, alpha)

    if alpha % 30 == 0: # Every 30 degrees (hour mark), make the mark longer
        x2 = x_coordinate(radius - 20, alpha)
        y2 = y_coordinate(radius - 20, alpha)
    else:
        x2 = x_coordinate(radius - 10, alpha)
        y2 = y_coordinate(radius - 10, alpha)
    canvas.create_line(x1, y1, x2, y2)
    alpha += 6

print(str(datetime.datetime.now())) # Display the real-time in the console
update() # Launch the main program function
root.mainloop() # Allows the user to close the program
