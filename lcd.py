from tkinter import *
import sys
import time as t
def dog():
    root=Tk()
    root.title("Log")
    log=Text(root,fg="white",bg="black")
    log.pack(fill=BOTH,expand=YES)
    log.insert(END,"Log initalized\n")
    log.insert(END,"Launcher started")
    log.config(state=DISABLED)
    sys.stdout=output(log)
    sys.stderr=output(log)
    __import__("idlew")
    

class output:
    def __init__(self,z,parent=000):
        self.z=z
    def write(self,text,flush=False):
        self.z.insert(END,text+"\n")
    def writelines(self,text=[]):
        for x in text:
            self.z.insert(END,x+"\n")
class input:
    def __init__(self,z,parent=000):
        self.z=z
    def write(self,text,flush=False):
        self.z.insert(END,text+"\n")
    def writelines(self,text=[]):
        for x in text:
            self.z.insert(END,x+"\n")
    def read(self,prompt=""):
        write(prompt)
        simpledialog.askstring("The program is requesting input","type the input for the program")
        
if __name__=="__main__":
    dog()
print("testing =========="+t.asctime()+"=======")


        
        

