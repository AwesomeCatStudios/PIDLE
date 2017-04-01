from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import time
root=Tk()
image=PhotoImage(file="test2.gif")
im=Label(root,image=image)
im.pack(side="bottom",fill=BOTH,expand=YES)
root.grab_set()
root.title("Image viewer")
def new_image(t=False,parms=0,e=0,p=2):
    fname = askopenfilename(filetypes=(("any", "*"),
                                           ("gif", "*.gif"),("All files", "*.*") ),title="view image")
    imgv=None
    try:
        imgv=PhotoImage(file=fname)
        im.configure(image=imgv)
        root.grab_set()
        root.title("Image viewer(new)")
        im.pack(side="bottom",fill=BOTH,expand=YES)
        root.grab_set()
        root.bell()
        #Tk()
        showinfo("see","due to bugs the image may only display during this window")
        
        
        
        
    
        
    except:
        showerror("Error:bad file","Error:bad file")
    
    
        
    
#root.grab_set()
#root.title("Image viewer("+fname+") at ")
Label(root,text="press a key to change current file").pack()

    
root.bind("<KeyPress>",new_image)
root.bind("<Button-3>",new_image)

'''
_tkinter.TclError: couldn't open "<_io.TextIOWrapper name='C:/Python 3.5/Lib/idlelib/moudles/pymaster/IDLEproject/Untitled.gif' mode='r' encoding='cp1252'>": no such file or directory
'''
root.mainloop()

