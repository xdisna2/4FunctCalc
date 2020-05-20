from tkinter import *
from tkinter import ttk

# Creates top level window
root = Tk()

# Creates a new button widget
button = ttk.Button(root, text='Click Me')

# Always pack the button
button.pack()

# Changing text
button['text'] = 'Hi There'
ttk.Label(root, text='Hello World!').pack()

# Always declare mainloop to keep it open
root.mainloop()



