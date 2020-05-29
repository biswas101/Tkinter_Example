from tkinter import *
from tkinter.filedialog import askopenfilename

from tkinter import messagebox

root = Tk()
root.geometry( "=400x300" )
root.title( "File Opener" )
text = Text(root)

def open_file():
    file_name = askopenfilename(initialdir="C:/",
                           title="Choose a XPS text file.",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*"))

                           )
    print (file_name)
    try:
        with open(file_name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)


filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)



root.config(menu=menubar)
root.mainloop()