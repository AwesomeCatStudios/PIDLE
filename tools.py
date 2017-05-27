if __name__=="__main__":
    import sys
import urllib.request as url
from tkinter import *
from tkinter import simpledialog
import warnings as warn
import warnings

#warn.simplefilter("ignore")
def msg(s,f):
    warn.warnings(s, f)
msg("warningsing:this uses internet\n I am not responsible for random downloads",warning)


class pkginstaller:
    
    def dwn(self,arg=0):
        
        
        com=self.install+self.e.get()+".py"
        print(com,file=sys.stderr)
        download=url.urlopen(com).read()
        print(dir(download),file=sys.stderr)
        print(type(download),file=sys.stderr)
        new=open(com[64:]+".py","wb")
        new.write(download)
        new.close()
        self.txt.insert(END,"\n install of "+com[64:]+" was sucessful\n")
              
                        
			
			
    
    def build(self,title="Install extensions"):
        #load cache
        self.install="https://raw.githubusercontent.com/javaarchive/extensions/master/"
        try:
            cache=url.urlopen("https://raw.githubusercontent.com/javaarchive/extensions/master/cache.txt")
            cache=cache.read()
        except:
            print("unable to read cache",file=sys.stderr)
            cache="unable to load available \nextensions for download\n note already installed extensions are included \n"
        self.win=Tk()
        self.win.title(title)
        
        self.txt=Text(self.win,bg="#8dfc98")
        self.txt.pack()
        self.txt.insert(END,cache)
        self.e=Entry(self.win,bg="lightgreen",width=30)
        self.e.pack()
        self.submit=Button(self.win,text="download \nNote:restart required",anchor=E,command=self.dwn,bg="lightblue",fg="gray")
        self.submit.pack()
        
        
    def __init__(self):
        self.install="https://raw.githubusercontent.com/javaarchive/extensions/master/"
        self.build()
 
        
        

s=pkginstaller()       
            
        
