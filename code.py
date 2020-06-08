        
from tkinter import * 

         
root = Tk() 
root.title("CRYPTOGRAPHY") 
root.geometry("500x300") 

def encryptMessage():                       
    pt = e1.get() 
  
    
    a=pt
    n=0
    b=''
    d=''
    for l in a:
    
       if n<len(a):
         b+=(l.replace(l,chr(ord(l)+n)))
       n+=1 
    e2.insert(0, b) 
  
def decryptMessage():                      
    ct1 = e3.get() 
    p=''
   
    m=len(ct1)-1
    c=ct1[::-1]
    for s in c:
   
      if m>=0:
        #print(s)
         p+=(s.replace(s,chr(ord(s)-m)))
      m-=1
    pt1=p[::-1]
    e4.insert(0, pt1) 
    
# creating labels and positioning them on the grid 
label1 = Label(root, text ='plain text')                
label1.grid(row = 10, column = 1) 
label2 = Label(root, text ='encrypted text') 
label2.grid(row = 11, column = 1) 
l3 = Label(root, text ="cipher text") 
l3.grid(row = 10, column = 10) 
l4 = Label(root, text ="decrypted text") 
l4.grid(row = 11, column = 10) 
  
# creating entries and positioning them on the grid 
e1 = Entry(root) 
e1.grid(row = 10, column = 2) 
e2 = Entry(root) 
e2.grid(row = 11, column = 2) 
e3 = Entry(root) 
e3.grid(row = 10, column = 11) 
e4 = Entry(root) 
e4.grid(row = 11, column = 11) 
  
# creating encryption button to produce the output 
ent = Button(root, text = "encrypt",bg ="red", fg ="white", command = encryptMessage) 
ent.grid(row = 13, column = 2) 
 
# creating decryption button to produce the output 
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = decryptMessage) 
b2.grid(row = 13, column = 11) 
  
  
 

root.mainloop() 
