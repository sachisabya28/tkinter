from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
root = Tk(  )
def OpenFile():
    name = askopenfilename(initialdir="C:\\Users\\sabya\\Desktop",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "selct fiel to read"
                           )
    print (name)

    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No fileeets")


Title = root.title( "File Opener")
label = ttk.Label(root, text ="I'm BATMAN!!!",foreground="red",font=("Helvetica", 16))
label.pack()


menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
menu.add_cascade(label = 'File', menu = file)
root.mainloop()
