from tkinter import *

window=Tk()
window.title("launcher")
c=Canvas(window,width=700,height=500,bg="light blue",relief=RAISED)
c.create_text([350,250], text="Pidle launcher",fill="magenta")
c.create_text([350,50], text="press enter to start",fill="purple")
c.create_text([350,150], text="You also launch other programs using this launcher",fill="red")
def launch_program(key="ice"):
    __import__("idlelaunch")
def win(d=0,e=0,s=9):
    window.destroy()
def targetmedia(cmd="line",l="2",gs="35"):
    __import__("media")
def viewer(external=False):
    __import__("viewer")
def viewer2(external=False):
    __import__("cmdmedia")
   
window.bind("<Key-Return>",launch_program)
window.bind("<Key-Escape>",win)
window.bind("<Key-m>",targetmedia)
window.bind("<Key-i>",launch_program)
window.bind("<F1>",viewer)
window.bind("<F2>",viewer2)


c.pack()
window.mainloop()



