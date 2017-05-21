replacing='qwertyuiopasdfghjklzxcvbnm )([]\/{}!@#$%^&*'
a='\/abcdefghijklmnopqrstuvwxyz() }{][*%$&^#@!'
replacing=list(replacing)
a=list(a)

d={}
e={}
if len(replacing)==len(a):

    for x in range(len(a)):
            d[replacing[x]]=a[x]
            e[a[x]]=replacing[x] 
    

    
def encypt(dict,string):
    'code'
    code=[]
    for x in string:
            code.append(dict[x])
    return ''.join(code)
def decypt(dict,string):
    'uncode'
    decode=[]
    for x in string:
            decode.append(dict[x])
    return ''.join(decode)
if __name__=='__main__':
    
    
        
        
            
            
        c=input('code:')
        code=encypt(e,c)
        decode=decypt(d,c)
        
        print('encypts to',code)
        
        print('decypt to',decode)
        input()
