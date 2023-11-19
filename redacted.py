from tkinter import *

window = Tk() # start of window code, pops up window
window.geometry("480x480+0+0") # dimensions of window and location of the window
window.title("Khloe") # title of window

icon = PhotoImage(file="redacted.png") # defines icon as photoimage file
window.iconphoto(True, icon) # makes icon the iconphoto of window 'window'

window.config(background="black")

window.mainloop() # end of window code
