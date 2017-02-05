from tkinter import *
from sys import argv as args
import sys
import subprocess as sub
import shlex as sh
import time as t
#import pygame as py
from idleconfig import *
from tkinter import filedialog as fi

sys.stdout=open("program.log","r+")
#py.init()
#py.mixer.init()
#py.mixer.music.load("Charl.mp3")
#py.mixer.music.play(1)

def read(f):
    source=open(f,"r")
    print("read:"+f)
    
    return source.readlines()
def stre():
    filename=filedialog.askopenfilename(initialdir = "c:/Python 3.5/Lib/idlelib/moudles",title = "choose your file",filetypes = (("python files","*.py"),("all files","*.*")))
    txt.delete("0.0", 'end')
    r=0
    f=read(filename)
    for x in f:
        r=r+1
        txt.insert(END,x)
        print(x)
        sys.stderr.write("file line:"+str(r))
def save():
    filename =  filedialog.asksaveasfilename(initialdir = "c:/Python 3.5/Lib/idlelib/moudles",title = "Select file to save",filetypes = (("python 3.5 files","*.py"),("all files","*.*")))
    fi=open(filename,"w")
    fi.write(txt.get("1.0",END))
    fi.close()

screen=Tk()
screen.title("Idle")
menubar = Menu(screen)
#menubar.pack()
#
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=stre)
filemenu.add_command(label="Save", command=save)
screen.config(menu=filemenu)
txt=Text(screen)
txt.pack()
txt.config(width=160, height=30)
txt2=Text(screen)
txt2.pack()
txt2.config(width=60, height=15)
#http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2806369
enter=Entry(screen)
enter.pack()

def run():
    fi=open("runaction.py","w")
    fi.write(txt.get("1.0",END))
    fi.close()
    cmd=sh.split("python runaction.py")
    data=sub.Popen(cmd,stdout=sub.PIPE)
    txt2.insert(END,"run:"+t.asctime()+data.read())
    
    
    
f=read(startfile)
print("f:"+str(f))
for x in f:
    txt.insert(END,x)
    print(x)
btn=Button(screen,text="run",command=run)
btn.pack()

screen.mainloop()
