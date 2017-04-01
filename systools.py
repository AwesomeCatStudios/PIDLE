import pickle as p
class sysfile:
    def __init__(self,name="program.log",ftype="r+"):

        self.f=open(name,ftype)
        try:
            #self.rr=self.f.read()
            self.prop={"name":name,"opentype":ftype,"data":self.f.readlines(),"datastr":self.f.read()}
        except:
            print("error:fileerror")
            self.prop={"name":name,"opentype":ftype}
        print(self.prop)
        
        
        self.ft=ftype
        #try:
        #    self.byt=p.Pickler(open(name,"rb+"),p.DEFAULT_PROTOCOL)
        #except:
        #
        #   raise Exception("Pickle could not be created warning")
            
    def init(self,name="program.log",ftype="r+"):
        self.f.close()
        self.f=open(name,ftype)
        self.prop={"name":name,"opentype":ftype,"data":self.f.readlines(),"datastr":self.f.read()}
        self.ft=ftype
    def addlines(self,lines=[]):
        if not self.ftype=="r":
            self.f.writelines(lines)
    def add(self,word="",glitch=""):
        print("the glitch was",glitch)
        self.f.write(word)
    def close(self):
        self.f.close()
        self.f=None
    
def pack(files,filen):
    
    packf=[]
    for x in files:
        print("packing file:",x)
        s=sysfile(x)
        s.close()
        packf.append(s)
        
    p.dump(packf,open(filen,"wb"))
def unpack(filen):
    f=open(filen,"rb+")
    dat=p.load(f)
    for data in dat:
        cf=sysfile(data.prop["name"],"w")
        print("this is: ",data.prop["datastr"])
        
        cf.add(data.prop["datastr"])#prop["datastr"])
        cf.close()
def test():
    pack(["read.txt"],"r.ppf")
    
        
    
    
    
    

        

        
    
        
