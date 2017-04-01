run=0
from tkinter import *

from pygame import *
from tkinter.messagebox import *
from tkinter import filedialog as fi
from tkinter.filedialog import *
#from idletools import *
tk=Tk()
from tkinter.simpledialog import *
try:
    import pygame
except:
    showerror("error:install pygame","install pygame")
    sys.exit(1)

musicpath=None
run=1
pygame.init()


selection={"hello":"hello.mp3","hedwigs theme":"harry-potter.mp3"}
tk.title("embed media player")
mixer.init()
#try:
#
#    mixer.music.set_volume(float(askfloat("volume","enter volume")))
#except:
#    showwarning("error:volume set error","error")
mixer.music.set_volume(0.8)   
stop=False
def stop(zx=0):
    global stop
    
    if stop:
        mixer.music.pause()
    else:
        mixer.music.unpause()
class btn:
    def __init__(self,master,command,text):
        v=Button(master,command=command,text=text)
        v.pack()
    def getid(self):
        
        
        return v
#m=Entry(tk)
def adijust_volume(p=0):
    s=askstring("volume","volume")
    try:
        mixer.music.set_volume(float(s))
    except:
        mixer.music.set_volume(int(s))

run=2
def get(sss=0):
    global selection
    print("s")
    music=selection[Lb1.get(SEL)]
    pygame.mixer.load(music)
com=Text(tk,bg="black",fg="white")
com.insert(END,"Welcome to cmd media player though it is not a command line media player")
com.pack(fill=BOTH,expand=YES)
#m.pack()
#r=Entry(tk,textvarible=musicpath)
#r.pack()
#can=Canvas(tk, width=750, height=750)
#can.pack()
prev=None
#next=None
def new(p=0,g=1):
    pygame.mixer.music.rewind()

def loadmusic(p=2):
    global enter
    
    try:
        enter=filedialog.askopenfilename(initialdir = "c:/users",title = "choose your file",filetypes = (("music","*.mp3"),("all files","*.*")))
        
        mixer.music.load(enter)
    except:
        com.insert(0.0,"error loading mp3 file")



def play(s=0):
    mixer.music.play(int(askinteger('loop times','loop times')))
    com.insert(END,"now playing: "+str(enter))
def unpause(sss=0):
    mixer.music.unpause()

run=3
def hello(e=0):
    
    try:
        com.insert(0.0,"""Hello, it's me
I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya
But I ain't done much healing

Hello, can you hear me
I'm in California dreaming about who we used to be
When we were younger and free
I've forgotten how it felt before the world fell at our feet

There's such a difference between us
And a million miles

Hello from the other side
I must have called a thousand times
To tell you I'm sorry for everything that I've done
But when I call you never seem to be home

Hello from the outside
At least I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter it clearly doesn't tear you apart anymore

Hello, how are you?
It's so typical of me to talk about myself I'm sorry
I hope that you're well
Did you ever make it out of that town where nothing ever happened

It's no secret that the both of us
Are running out of time

So hello from the other side
I must have called a thousand times
To tell you I'm sorry for everything that I've done
But when I call you never seem to be home
Hello from the outside
At least I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter it clearly doesn't tear you apart anymore

Ooooohh, anymore
Ooooohh, anymore
Ooooohh, anymore
Anymore

Hello from the other side
I must have called a thousand times
To tell you I'm sorry for everything that I've done
But when I call you never seem to be home
Hello from the outside
At least I can say that I've tried
To tell you I'm sorry for breaking your heart
But it don't matter it clearly doesn't tear you apart anymore""")
        mixer.music.load("hello.mp3")
        mixer.music.play()
    except:
        com.insert("error loading hello.mp3")
        
    

def qmusic():
    global musicpath,r
    try:
        mixer.music.queue(askopenfilename(initialdir = "c:/Python 3.5/Lib/idlelib/moudles",title = "choose your file",filetypes = (("python files","*.py"),("all files","*.*"))))
    except:
        com.insert(0.0,"error loading mp3 file")

tk.bind_all("<Key-a>", new)
tk.bind_all("<Key-i>",loadmusic)
tk.bind_all("<space>",stop)
tk.bind_all("<Key-q>",qmusic)
tk.bind_all("<Return>",play)

#pygame.mixer.music.set_endevent() 

