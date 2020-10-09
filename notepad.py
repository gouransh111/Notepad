from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
def Newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    #textaarea delete se 1.0 matlab 1 line ke 0 character se end tak hata do
    Textarea.delete(1.0,END)
def openfile():
    # *matlab sabhi tareh ki files
   file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
   if file == "":
       file = None
   else:
       root.title(os.path.basename(file) + " - Notepad")
       Textarea.delete(1.0,END)
       f = open(file,"r")
       # textarea .insert 1 line ke 0 character se f.read jha tak jayega va tak insert kar dega
       Textarea.insert(1.0,f.read())
       f.close()  
 
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
           file = None
        else:
          f = open(file,"w")
          f.write(Textarea.get(1.0,END))
          f.close()    
          root.title(os.path.basename(file) + "- Notepad")
    else:
          f = open(file,"w")
          f.write(Textarea.get(1.0,END))
          f.close()        
def quitApp():
    #it closes the window
    root.destroy()
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by gouransh")                  
root.title("Notepad by gouransh")
root.geometry("655x755")
#add text area 
Textarea = Text(root,font = "lucida 13")
#fill=Both fill x and y both and expand takes the width of the parent 
Textarea.pack(expand=True,fill=BOTH)
file = None
#lets create a menubar
Menubar = Menu(root)
#Filemenu starts
FileMenu = Menu(Menubar,tearoff=0)

#to open new file
FileMenu.add_command(label="New",command= Newfile)
FileMenu.add_command(label="Open",command= openfile)
# to save the file
FileMenu.add_command(label="Save",command = savefile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command = quitApp)
Menubar.add_cascade(label = "File",menu=FileMenu)

#Edit menu starts
EditMenu = Menu(Menubar,tearoff= 0)
#to give cut,copy,paste
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="paste",command=paste)
Menubar.add_cascade (label="Edit",menu=EditMenu)
#help menu starts
Helpmenu = Menu(Menubar,tearoff=0)
Helpmenu.add_command(label="About notepad",command=about)
Menubar.add_cascade(label="Help",menu=Helpmenu)
root.config(menu = Menubar)

#adding Scrollbar
Scroll = Scrollbar(Textarea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=Scroll.set)



root.mainloop()