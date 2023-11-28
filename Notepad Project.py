from tkinter import *

root=Tk()

root.geometry("644x344")

root.title("Notepad By Abhijit Das")


# Define all function..

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass





# ADD SCROLLBAR

scroll=Scrollbar(root)
scroll.pack(side=RIGHT , fill=Y)

# ADD textArea
textArea=Text(root , font="lucida 13")
textArea.pack()

file=None


scroll.config(command=textArea.yview)     # scrollbar.config(command=widget.yview)

textArea.config(yscrollcommand=scroll.set)       # Widget.config(yscrollcommand = scrollbar.set)



# ADD DROP-DOWN MENU

mainmenu=Menu(root)
m1=Menu(mainmenu , tearoff=0)

m1.add_command(label="New" , command=new_file)

m1.add_command(label="Open" , command=open_file)

m1.add_command(label="Save" , command=save_file)

m1.add_separator()

m1.add_command(label="Exit" , command=quit)

# to pack the menu..
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File" , )



root.mainloop()