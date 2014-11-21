from Tkinter import *
import time
import sqlite3 as lite
import random
root=Tk()
a4=[]
m1=0
m2=0
m3=0
a5=[]
a6=''
from tkMessageBox import *
def check1():
    h=en.get()
    if(h==a6):
        t2=time.time()
        t3=t2-t1
        print "t3 is: ",t3
        cur.execute("insert into pro_crypto values(?,?,?,?)",(m1,m2,m3,t3,))
        c.commit()
    else:
        showinfo('','you have entered wrong')
##        print "m1 is: ",m1
##    print "t3 is: ",t3
##    cur.execute("insert into pro_crypto values(?,?,?,?)",(m1,m2,m3,t3,))
##        print t3
    
##    en=Entry(root)
##    en.grid(row=1,column=1)
    check()
def check():

##    en=Entry(root)
##    en.grid(row=1,column=1)
    global m1,m2,m3,a6,t3,t2,t1,en
    en=Entry(root)
    en.grid(row=1,column=1)    

    
    a1=['a','q','w','s','d','z','x','c','e']
    a2=['r','t','y','f','g','h','v','b','n']
    a3=['u','i','o','p','j','k','l','m']
    for k in range(0,6):
        a4.append(random.choice(a1[random.randint(0,8)]+a2[random.randint(0,8)]+a3[random.randint(0,7)]))
    print a4
    m1=0
    m2=0
    m3=0
    for i in range(0,6):
        if(a4[i] in a1):
            m1=int(m1)+1
        elif(a4[i] in a2):
            m2=int(m2)+1
        elif(a4[i] in a3):
            m3=int(m3)+1
    a6=''
    for i in range(0,6):
        a6 +=str(a4[i])
    a4[:]=[]
    print 'm1 is',m1
    print 'm2 is',m2
    print 'm3 is',m3

    Label(root,text=a6).grid(row=1,column=0)
    t1=time.time()
    
    print 'a6 is',a6
    
##    t2=time.time()
##    if(h==a6):
##        
##        t3=t2-t1
##        print "m1 is: ",m1
##        print "t3 is: ",t3
##        cur.execute("insert into pro_crypto values(?,?)",(m1,m2,m3,t3,))
##        print t3
##        c.commit()
    
        
    
    
        
Label(root,text="Please enter the words in the box::").grid(row=0,column=0)

Button(root,text='Next',command=check1).grid(row=2,column=2)
c=lite.connect("project10.db")
cur=c.cursor()
cur.execute("create table pro_crypto(Category1 varchar(20),Category2 varchar(20),Category3 varchar(20),Time varchar(20))")
##cur.execute("insert into user values('raj','saha')")

check()
root.mainloop()
