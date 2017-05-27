print('''
================================
Welcome to cmd pack
Provided by PIDLE
================================
type help for help
pack-pack files to an file
unpack-unpack files from packed file
exit-to exit
ENJOY





''')
try:
    from systools import *
    import os
    def isfile(file_path):
        if not file_path:
            return False
        elif not os.path.isfile(file_path):
            return False
        else:
            return True
except:
    print("unable to use pack or unpack")
while True:
    data=input(">>>").lower()
    if data=="pack":
        c=[]
        while True:
            t=input("File to pack  press enter if done")
            if t=="":
                break
            else:
                if isfile(t):
                    c.append(t)
                else:
                    raise Exception(t+" is not a file")
        
        pack(c,input("finish file: "))
    elif data=="unpack":
        try:
            unpack(input("File to unpack:\t"))
        except:
            raise Exception("Unable to unpack")
    elif data=="exit":
        break
    elif data=="help":
        print('''
================================
Welcome to cmd pack
Provided by PIDLE
================================
type help for help
pack-pack files to an file
unpack-unpack files from packed file
exit-to exit
ENJOY





''')


