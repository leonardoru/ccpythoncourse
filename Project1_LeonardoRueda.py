# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYTHON-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Project 1: Write a Calculator in Python:
# - It needs to be able to carry out addition, subtraction, division and multiplication.
# - It needs to be able to handle positive and negative numbers.
# - It needs to be able to accept integers and floating point numbers.
# - Clear button is to clear the screen during calculation or after the calculation.  When this button is pressed, windows needs to be cleaned as in the above picture.
# - For all buttons (numbers and functions), you will need to use Lambda functions.
# - All buttons need to be placed exactly same as above picture.
# - Entire Calculator size and button size should be larger than the picture since it was reduced to display without taking up too much space.
# - You will need to use several functions.
# - Make sure to provide proper comments for the program.
# - Windows color needs to be different than button or frame color.
# - Frame color and button color needs to be different.
# - Only use tkinter package.
# - Do not create a class for it. 
# - Only use functions for it.
# Student: Leonardo Rueda

# First import tkinter using * for all 
from tkinter import *

# 1. Calculator's Window
# Here we create a new window and set some settings for the window.
window = Tk() 
window.geometry("340x210")  # this is for the size of the window 

# Let's prevent windowdow resizing
window.resizable(0, 0)  

# Let's add a title to our window
window.title("Leonardo Ruedas Calculator")

# Let's add a background color to our window
window['bg']='white'

# 2. Function Definitions:                                    
# - 'main_buttons_action' function : 
# - This function appends a new character to the main string on the Calculators display ( Entry field)

def main_buttons_action(digit):
    global main_calculation_string
    if main_calculation_string == 0:
       input_text.set("") 
    main_calculation_string = main_calculation_string + str(digit)
    input_text.set(main_calculation_string)

# - 'clear_button_action' function :This is used to clear 
# - the input field

def clear_button_action():
    global main_calculation_string 
    main_calculation_string = "" 
    input_text.set("0")
 
# - 'equals_button_action':This method calculates the main_calculation_string 
# - currently present in input field
 
def equals_button_action( params = 0 ):
    global main_calculation_string
    if main_calculation_string != "":
        
        # - Note that the 'eval' function here is used to evaluate the main_calculation_string
        # - var directly instead of having functions for each operator ( + - / * )
        result = str(eval(main_calculation_string)) 
        input_text.set(result)

        # - The following allows to add the result to be used as part of the next operation
        main_calculation_string = result

# Add Global variable to hold the main Calculation string
main_calculation_string = ""

# - Note that the StringVar() function that follows here is used to get the instance of input field.
input_text = StringVar()

# Calculator Parts:
# 1 .Calculator Display:
# - Let's create a frame for the main Display of the calculator
display_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2) 
display_frame.pack(side=TOP)

# 2. Calculator's Display: 
# - Let's create the actual Display inside the frame using an 'Entry' class
# -- Note that the Entry for the display has the state=DISABLED property set... 
# -- This is so that users are not able to type directly into the field. 
# -- Instead they have to click the buttons or press the authorized maped keys.
main_display = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT, state=DISABLED, disabledforeground="#000000")
main_display.grid(row=0, column=0) 
main_display.pack(ipady=10) 
# -- Here we set the initial value to 0
input_text.set("0")

# 3. Calculator's Buttons
#  - Let's create another frame for the buttons
buttons_container = Frame(window, width=230, height=272.5, bg="white")
buttons_container.pack()
 
# - Finally we add all the buttons in a 4 x 5 row pattern and associate button actions accordingly
# -- Row 1
seven = Button(buttons_container, text = "7", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(7)).grid(row = 1, column = 0, padx = 0, pady = 0)
eight = Button(buttons_container, text = "8", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(8)).grid(row = 1, column = 1, padx = 0, pady = 0)
nine = Button(buttons_container, text = "9", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(9)).grid(row = 1, column = 2, padx = 0, pady = 0) 
plus = Button(buttons_container, text = "+", fg = "black", width = 7, height = 1, bd = 0, bg = "#eee",  command = lambda: main_buttons_action("+")).grid(row = 1, column = 3, padx = 0, pady = 0)
 
# -- Row 2
four = Button(buttons_container, text = "4", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(4)).grid(row = 2, column = 0, padx = 0, pady = 0)
five = Button(buttons_container, text = "5", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(5)).grid(row = 2, column = 1, padx = 0, pady = 0)
six = Button(buttons_container, text = "6", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(6)).grid(row = 2, column = 2, padx = 0, pady = 0) 
minus = Button(buttons_container, text = "-", fg = "black", width = 7, height = 1, bd = 0, bg = "#eee",  command = lambda: main_buttons_action("-")).grid(row = 2, column = 3, padx = 0, pady = 0)
 
# -- Row 3
one = Button(buttons_container, text = "1", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(1)).grid(row = 3, column = 0, padx = 0, pady = 0)
two = Button(buttons_container, text = "2", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(2)).grid(row = 3, column = 1, padx = 0, pady = 0)
three = Button(buttons_container, text = "3", fg = "black", width = 7, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(3)).grid(row = 3, column = 2, padx = 0, pady = 0)
multiplication = Button(buttons_container, text = "*", fg = "black", width = 7, height = 1, bd = 0, bg = "#eee",  command = lambda: main_buttons_action("*")).grid(row = 3, column = 3, padx = 0, pady = 0) 

# -- Row 4
zero = Button(buttons_container, text = "0", fg = "black", width = 17, height = 1, bd = 0, bg = "grey",  command = lambda: main_buttons_action(0)).grid(row = 4, column = 0, columnspan = 2, padx = 0, pady = 0)
point = Button(buttons_container, text = ".", fg = "black", width = 7, height = 1, bd = 0, bg = "#eee",  command = lambda: main_buttons_action(".")).grid(row = 4, column = 2, padx = 0, pady = 0) 
division = Button(buttons_container, text = "/", fg = "black", width = 7, height = 1, bd = 0, bg = "#eee",  command = lambda: main_buttons_action("/")).grid(row = 4, column = 3, padx = 0, pady = 0)

# -- Row 5
equals = Button(buttons_container, text = "=", fg = "black", width = 28, height = 1, bd = 0, bg = "#eee",  command = lambda: equals_button_action()).grid(row = 5, column = 0,columnspan = 3, padx = 0, pady = 0) 
clear = Button(buttons_container, text = "Clear", fg = "black", width = 7, height = 1, bd = 0, bg = "#eee",  command = lambda: clear_button_action()).grid(row = 5, column = 3, columnspan = 3, padx = 0, pady = 0)

# Button Mapping
# - Proffesor I have added this additional functionality to map the keys 
# - I thought it was cool and necessary.
window.bind ("<Return>", equals_button_action)
window.bind ("1", lambda i: main_buttons_action(1))
window.bind ("2", lambda i: main_buttons_action(2))
window.bind ("3", lambda i: main_buttons_action(3))
window.bind ("4", lambda i: main_buttons_action(4))
window.bind ("5", lambda i: main_buttons_action(5))
window.bind ("6", lambda i: main_buttons_action(6))
window.bind ("7", lambda i: main_buttons_action(7))
window.bind ("8", lambda i: main_buttons_action(8))
window.bind ("9", lambda i: main_buttons_action(9))
window.bind ("0", lambda i: main_buttons_action(0))
window.bind ("+", lambda i: main_buttons_action('+'))
window.bind ("-", lambda i: main_buttons_action('-'))
window.bind ("/", lambda i: main_buttons_action('/'))
window.bind ("*", lambda i: main_buttons_action('*'))
window.bind (".", lambda i: main_buttons_action('.'))

window.mainloop()

# By: Leonardo Rueda

