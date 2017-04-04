from tkinter import *
import os
#from thread import start_new_thread
import threading
import ccode
from ccode import *
#this file must exisit for idlelaunch to run properly
#idleconfig.py idle configruation
startfile="idleconfig.py"
from tkinter.messagebox import *
'''sets
hieght = text h
width = textw
'''
import extension as e
webconfig=8080
openpswd=False
start=False
textw=8000
texth=40
title="Idle(python) 2.5.0"#title
passkey=""
bgcolor="#e3cdeb"
idlecodecolor="#93d1cd"
import webbrowser

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



from systools import *
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
   tkmessagebox.showinfo("info","PIDLE is an idle for creating programs \n It is still in devlopment \nyour version: \t "+title[-5:]+"""
\n
I strongly recomendusing the .bat launcher for windows and the script launcher
\n
for linux. There is no mac launcher \n
right now so you 
just have to launch it through idlelaunch.py


Also this idle is open source and free for all.
please feel free to make any edits,comments,suggestions or improvements.






PIDLE 2.5.0 downloaded from github ©
"""
)
args=sys.argv
   
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
def estre():
    global cfile
    filename=filedialog.askopenfilename(initialdir = "c:/users",title = "choose your file",filetypes = (("python files","*.py"),("all files","*.*")))
    txt.delete("0.0", 'end')
    r=0
    f=read(filename)
    
    for x in f:
        r=r+1
        x=ccdoe.decypt(e,x)
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
def esave2(c=0):
    try:
        global cfile
        filename=fi.asksaveasfilename(initialdir = "c:/users",title = "Select file to save",filetypes = (("python 3.5 files","*.py"),("all files","*.*")))
        fi=open(filename,"w")
        fi.write(ccdoe.encypt(e,txt.get("1.0",END)))
        fi.close()
    except:
        print("error bad file")

def save2(c=0):
    try:
        global cfile
        filename=cfile
        fi=open(filename,"w")
        fi.write(txt.get("1.0",END))
        fi.close()
    except:
        print("error bad file")
def ssave2(c=0):
    global asave
    if asave:
        
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
def idle(keyboard=False):
    import idlelib.PyShell
    idlelib.PyShell.main()
def rrs(key=False):
    chrome("https://github.com/javaarchive/idle/archive/master.zip")
def yahoo(z=1):
    try:
        chrome("https://search.yahoo.com/search;_ylc=X3oDMTFiN25laTRvBF9TAzIwMjM1MzgwNzUEaXRjAzEEc2VjA3NyY2hfcWEEc2xrA3NyY2h3ZWI-?p="+askstring("Search yahoo","search keywords").replace(" ","+")+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8")
    except:
        
        showerror("Something went wrong","search error")

    
    
def compress(r=0,w=9):
    rty=(("python packed files","*.ppf"),("all files","*.*"),("pyzip file","*.pzip"),("*.py","python files"),("*.py;*.docx;*.doc;*.gif;*.jpg;*.dll;*.pyw;*.exe;*.bat;*.zip;*.ppf;*.pzip;*.zip;*.tar.gz;*.7z","work files"))
    filez = filedialog.askopenfilenames(parent=screen,title='Choose files to compress',filetypes = rty)
    s=screen.tk.splitlist(filez)
    #try:
        #try:
    pack(s,filedialog.asksaveasfilename(parent=screen,title='Save compresed files',filetypes = (("python packed files","*.ppf"),("all files","*.*"),"pyzip file","*.pzip")))
        
    showinfo("Done","files compressed sucessufully")
    #except:
        #showerror("invaid","invaid")
def findr(s=0):
    what=askstring("find and replace","find what")
    replace=askstring("find and replace","replace with")
    text=txt.get("1.0",END)
    text=text.replace(what,replace)
    txt.delete(END)
    txt.insert(END,text)
def getargs(pants=19854):
    global args
    showinfo("arguments for the program",str(args))
    
def coe(r=0,w=9):
    filez = filedialog.askopenfilenames(parent=screen,title='Choose file to extract',filetypes = (("python packed files","*.ppf"),("all files","*.*")))
    
    try:
        unpack(filez)
        showinfo("Done","files extracted sucessufully")
    except:
        showerror("invaid","invaid")
def webserver(key=0):
    import http.server
    import socketserver
    trust=True
    while trust:
        #try:
        PORT = webconfig
        PORT=askinteger("web server","port number please")
            
            
        Handler = http.server.SimpleHTTPRequestHandler

        httpd = socketserver.TCPServer(("localhost", PORT), Handler)

        print("serving at port", PORT)
        trust=False
        httpd.serve_forever()
            
        #except:
        trust=False
        showerror("Not a valid port number try again","error")
            
            
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print(self.threadID,"\t executing server")
        webserver(2)
                    
def handleweb(key=2):
    thread=myThread(0,"webthread",100)
    thread.start()

    
    
screen=Tk()
screen.title(title)
screen.bind("<F4>",hello)
if openpswd:
    s=askstring("Password", "Enter password:", show='*')
    if s!=passkey:
        tkmessagebox.showerror("Exiting",'wrong password')
        sys.exit(1)

menubar = Menu(screen)
def opendcs(s=2):
    chrome("https://javaarchive.github.io/idle/error.htm")
from urllib.request import *
def url():
    try:
        urlo=urlopen(simpledialog.askstring("Open url","open url")).read()
        txt.delete("0.0",END)
        txt.insert(END,urlo)
    except:
        showerror("Bad url","Bad url")
'''def tell():
    showinfo(
'''     
    
    
#menubar.pack()
#
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=stre)
filemenu.add_command(label="Save", command=save2)
filemenu.add_command(label="Save as", command=save)
filemenu.add_command(label="quit", command=(lambda:quitgui("event")))
filemenu.add_command(label="open python IDLE", command=(lambda:idle("event")))
filemenu.add_command(label="extract", command=coe)
filemenu.add_command(label="compress", command=compress)

filemenu.add_separator()
# create more pulldown menus
edit=Menu(menubar)
def google(x=0):
    search=askstring("google","what should I google for you").replace(" ","+")
    chrome("https://www.google.com/#safe=active&q="+search)
    
def toggle(c=1):
    global asave
    asave=not asave
    
    
editmenu = Menu(menubar)
editmenu.add_command(label="open IDLE docs",command=opendcs)
editmenu.add_command(label="find/replace", command=findr)
editmenu.add_command(label="get arguments", command=getargs)
editmenu.add_command(label="redownload", command=rrs)
editmenu.add_command(label="web server", command=handleweb)
editmenu.add_command(label="encypted save", command=esave2)
editmenu.add_command(label="decypted open", command=estre)
editmenu.add_command(label="open an url", command=url)
#editmenu.add_command(label="Check for autosave", command=getsave)
editmenu.add_command(label="Change autosave setting(on/off)", command=toggle)
s=Menu(menubar)
s.add_command(label="google", command=google)
s.add_command(label="yahoo", command=yahoo)

def copy(x=2):
    screen.clipboard_clear()
    screen.clipboard_append(txt.selection_get())
    print("copy:",txt.selection_get())
def paste(x=2):
    txt.inset(txt.index(INSERT),screen.clipboard_get())
    print("paste:",screen.clipboard_get())
edit.add_command(label="copy", command=copy)
edit.add_command(label="paste", command=paste)

filemenu.add_cascade(label="Search",menu=s)    

    
def p(string):
    sys.stderr.write(string+"\n")
    
filemenu.add_cascade(label="More", menu=editmenu)
filemenu.add_cascade(label="edit", menu=edit)

screen.bind("<Key-Escape>",quitgui)
screen.bind("<Button-2>",save4)
screen.bind("<F1>",docs)

screen.bind("<F2>",docx)
screen.bind("<KeyPress>",ssave2)

asave=True
def toggle(c=1):
    global asave
    asave=not asave

screen.bind("<F3>",save3)
screen.bind("<F4>",hello)
screen.bind("<F11>",handleweb)
screen.bind("<F12>",toggle)

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
#status.iconbitmap("favicon.ico")
txt2=Text(status,bg="#f4f8ff")
txt2.pack()
txt2.config(width=75)
entry=Entry(status,font = "Helvetica 16 bold")
entry.pack()

def getrsave():
    global asave
    showinfo("it is","Autosave:"+str(asave))
    
def runcmd(parms="hi"):
    try:
        s=sh.split(entry.get())
        scmd=sub.Popen(s,stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
        txt2.insert(END,std(scmd))
    except:
        txt2.insert(END,"error with command line command")


class xmyThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print(self.threadID,"\t executing command")
        processplugin()
      
def go(true=True):
    processplugin()
    #th= myThread(1, "cmd", 1)
    #th.start()
entry.bind("<Return>",runcmd)
editmenu.add_command(label="Check for autosave", command=getrsave)
btn=Button(status,bg="magenta",text="run in cmdline",command=runcmd)
btn.pack()
def processplugin():
    o=e.Plugin([screen,txt,txt2,entry,btn3,btn])
    value=entry.get()
    try:
        eval("o."+value+"()")
    except:
        showerror("no plugin","no plugin installed: "+value+"\t")
btn3=Button(status,bg="magenta",text="plugin launch",command=go)
btn3.pack()    

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

