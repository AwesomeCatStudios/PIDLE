from tkinter import *
import os
#from thread import start_new_thread
#import threading
#this file must exisit for idlelaunch to run properly
#idleconfig.py idle configruation
startfile="idleconfig.py"
from tkinter.messagebox import *
'''sets
hieght = text h
width = textw
'''
openpswd=True
start=False
textw=80
texth=40
title="Idle(python) 1.9 "#title
passkey=""
bgcolor="#e3cdeb"
idlecodecolor="#93d1cd"


def fit(obj):
    obj.config(expand=YES)
up=TOP
right=RIGHT
left=LEFT
def quitask(screen):
    if askokcancel("Quit", "Do you really wish to quit?"):
        screen.destroy()
def launch(program):
    Popen(make("launch "+program))

def chrome(url):
    webbrowser.open_new(url)
def view(filename):
    

    webbrowser.open("file:///"+os.path.realpath(filename))




from sys import argv as args
import sys
import subprocess as sub
import shlex as sh
import time as t
#import pygame as py
#from idleconfig import *
from tkinter import filedialog as fi
#from idletools import *
from tkinter.simpledialog import *
import tkinter.messagebox as tkmessagebox
sys.stdout=open("program.log","r+")
if start:
    chrome("https://docs.python.org/3.5/")
def hello(event):
   tkmessagebox.showinfo("info","PIDLE is an idle for creating programs \n It is still in devlopment your version: \t "+title[-5:]+"""
\n
I strongly recomendusing the .bat launcher for windows and the script launcher
\n
for linux. There is no mac launcher \n
right now so you 
just have to launch it through idlelaunch.py


Also this idle is open source and free for all.
please feel free to make any edits,comments,suggestions or improvements.






PIDLE ©
"""
)
def std(args):
    '''
    tool finds string of errors and stdout from cmdline
    '''
    return str(args.stdout.read().decode())+str(args.stderr.read().decode())
#py.init()
#py.mixer.init()
#py.mixer.music.load("Charl.mp3")
#py.mixer.music.play(1)
cfile=startfile
def docs(key):
    chrome('https://docs.python.org/3.5/')
def docx(event):
    chrome("https://docs.python.org/3/")
def read(f):
    try:
        source=open(f,"r")
        print("read:"+f)
    
        return source.read()
    except:print("bad read file")
def stre():
    global cfile
    filename=filedialog.askopenfilename(initialdir = "c:/users",title = "choose your file",filetypes = (("python files","*.py"),("all files","*.*")))
    txt.delete("0.0", 'end')
    r=0
    f=read(filename)
    
    for x in f:
        r=r+1
        txt.insert(END,x)
        print(x)
        #sys.stderr.write("file line:"+str(r))
    cfile=filename
def save():
    filename =  fi.asksaveasfilename(initialdir = "c:/users",title = "Select file to save",filetypes = (("python 3.5 files","*.py"),("all files","*.*")))
    fil=open(filename,"w")
    fil.write(txt.get("1.0",END))
    fil.close()
def save3(i):
    filename =  fi.asksaveasfilename(initialdir = "c:/users",title = "Select file to save",filetypes = (("python 3.5 files","*.py"),("all files","*.*")))
    fil=open(filename,"w")
    fil.write(txt.get("1.0",END))
    fil.close()
def save2():
    try:
        global cfile
        filename=cfile
        fi=open(filename,"w")
        fi.write(txt.get("1.0",END))
        fi.close()
    except:
        print("error bad file")
def save4(isop):
    try:
        global cfile
        filename=cfile
        fil=open(filename,"w")
        fil.write(txt.get("1.0",END))
        fil.close()
    except:
        print("error bad file")
def quitgui(event):
    quitask(screen)
    status.destroy()
    sys.exit()
screen=Tk()
screen.title(title)
screen.bind("<F4>",hello)
if openpswd:
    s=askstring("Password", "Enter password:", show='*')
    if s!=passkey:
        tkmessagebox.showerror("Exiting",'wrong password')
        sys.exit(1)

menubar = Menu(screen)

#menubar.pack()
#
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=stre)
filemenu.add_command(label="Save", command=save2)
filemenu.add_command(label="Save as", command=save)
filemenu.add_command(label="quit", command=(lambda:quitgui("event")))
screen.bind("<Key-Escape>",quitgui)
screen.bind("<Button-2>",save4)
screen.bind("<F1>",docs)

screen.bind("<F2>",docx)

screen.bind("<F3>",save3)
screen.bind("<F4>",hello)
screen.config(menu=filemenu)
screen.config(bg=bgcolor)
txt=Text(screen)
txt.pack(fill=BOTH,anchor=CENTER,expand=YES)
scrollbar = Scrollbar(screen)
scrollbar.pack(side=RIGHT,fill=Y,expand=YES)
txt.config(yscrollcommand=scrollbar)
txt.pack()
scrollbar.config(command=txt.yview)
#note BUUGGs

'''


note the bugs



'''
txt.config(width=textw, height=texth,bg=idlecodecolor)
#Escape
#txt2=Text(screen)
#txt2.pack()
#txt2.config(width=60, height=15)
enter=Entry(screen)
enter.pack()
status=Tk()
status.iconbitmap("favicon.ico")
txt2=Text(status,bg="#f4f8ff")
txt2.pack()
txt2.config(width=75)
entry=Entry(status,font = "Helvetica 22 bold")
entry.pack()


def runcmd(parms="hi"):
    try:
        s=sh.split(entry.get())
        scmd=sub.Popen(s,stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
        txt2.insert(END,std(scmd))
    except:
        txt2.insert(END,"error with command line command")


'''class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print(self.threadID,"\t executing command")
        runcmd()
'''        
def go(true=True):
    th= myThread(1, "cmd", 1)
    th.start()
entry.bind("<Return>",runcmd)
btn=Button(status,bg="magenta",text="run in cmdline",command=runcmd)
btn.pack()
def run():
    
    fi=open("runaction.py","w")
    fi.write(txt.get("1.0",END))
    fi.close()
    r=open("runaction.py","r")
    exec(r.read())
    
    txt2.insert(END,"run:"+t.asctime()+r.name)
    r.close()
    
    
f=read(startfile)
print("f:"+str(f))

txt.insert(END,f)
print(f)
btn=Button(screen,text="run",command=run)
btn.pack()

screen.mainloop()
