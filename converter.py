from tkinter import *
window=Tk()
root=window
main=Menu(root)
basic=Menu(root)
main.add_cascade(label="basic",menu=basic)
window.config(menu=main)
window.title("Rconvert 2.0")
import sys
def exitp(r=0):
    window.quit()
    sys.exit(1)
basic.add_command(label="exit",command=exitp)
convi=Entry(root,bg="green")
convi.pack(anchor=W)
convo=Entry(root,bg="red")
convo.pack(anchor=E)
info=Label(text="info",anchor=CENTER)
info.pack()
