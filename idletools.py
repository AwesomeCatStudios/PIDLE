from tkinter import *
from tkinter.messagebox import *
from subprocess import Popen
from shlex import split as make
import webbrowser
import os
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

