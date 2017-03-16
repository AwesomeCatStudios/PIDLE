run=0
from tkinter import *

from pygame import *
from tkinter.messagebox import *
from tkinter import filedialog as fi
#from idletools import *

from tkinter.simpledialog import *
try:
    import pygame
except:
    showerror("error:install pygame","install pygame")
    sys.exit(1)

musicpath=None
run=1
pygame.init()
tk=Tk()

selection={"hello":"hello.mp3","hedwigs theme":"harry-potter.mp3"}
tk.title("embed media player")
mixer.init()
try:

    mixer.music.set_volume(float(askfloat("volume","enter volume")))
except:
    showwarning("error:volume set error","error")
    
Lb1 = Listbox(tk)
index=0
for x in selection:
    index=+1
    Lb1.insert(index,x)
Lb1.pack()
def stop():
    mixer.music.pause()
class btn:
    def __init__(self,master,command,text):
        v=Button(master,command=command,text=text)
        v.pack()
    def getid(self):
        
        
        return v
#m=Entry(tk)
def adijust_volume():
    s=askstring("volume","volume")
    try:
        mixer.music.set_volume(float(s))
    except:
        mixer.music.set_volume(int(s))
g=btn(tk,adijust_volume,'adjust')
run=2
def get():
    global selection
    print("s")
    music=selection[Lb1.get(SEL)]
    pygame.mixer.load(music)
d=btn(tk,stop,'pause')
#m.pack()
#r=Entry(tk,textvarible=musicpath)
#r.pack()
#can=Canvas(tk, width=750, height=750)
#can.pack()


def loadmusic():
    
    try:
        mixer.music.load(filedialog.askopenfilename(initialdir = "c:/users",title = "choose your file",filetypes = (("music","*.mp3"),("all files","*.*"))))
    except:
        com.insert(0.0,"error loading mp3 file")


s=btn(tk,loadmusic,'import')
def play():
    mixer.music.play(int(askint('loop times','loop times')))
def unpause():
    mixer.music.unpause()
a=Button(tk,command=unpause,text='resume')
o=Button(tk,command=play,text='play')
o.pack()
a.pack()            
Button(tk,text="import selection",command=get).pack()
com=Text(tk)
com.pack()
run=3
def hello():
    
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
        
    
mybutton=Button(tk,command=hello,text="hello")
mybutton.pack()
def qmusic():
    global musicpath,r
    try:mixer.music.queue(askopenfilename(initialdir = "c:/Python 3.5/Lib/idlelib/moudles",title = "choose your file",filetypes = (("python files","*.py"),("all files","*.*")))
)
    except:
        com.insert(0.0,"error loading mp3 file")
quick=btn(tk,qmusic,"play after finish")

