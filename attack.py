import time
import sqlite3 as lite
from Tkinter import *
from math import *
import random
a=[]
b=[]
a0=[]
a1=[]
a2=[]
a3=[]
a5=[]
a6=[]
a9=[]
abc=[]
efg=[]
def check3(flag,t):
    m1=m2=m3=0
    p0=['a','q','w','s','d','z','x','c','e']
    p1=['r','t','y','f','g','h','v','b','n']
    p2=['u','i','o','p','j','k','l','m']

    for i in range(0,6):
        if(ert[i] in p0):
            m1=int(m1)+1
        elif(ert[i] in p1):
            m2=int(m2)+1
        elif(ert[i] in p2):
            m3=int(m3)+1
    new_list=[]
    new_list.append(m1)
    new_list.append(m2)
    new_list.append(m3)
    print 'new list is',new_list
    c=lite.connect("project10.db")
    cur=c.cursor()
    res=cur.execute("select * from pro_crypto")
    for i in res:
        print i
        for j in range(0,3):
            a.append(eval(str(i[j])))
        print a
        b.append(eval(str(i[3])))
        print b
    for i in range(0,5):
        abc.append(floor(b[i]))
        efg.append(ceil(b[i]))
    print 'abc is',abc
    print 'efg is',efg

    if(len(a)!=0):
        for i in range(0,3):
            a1.append(a.pop(0))
    if(len(a)!=0):
        for i in range(0,3):
            a2.append(a.pop(0))
    if(len(a)!=0):
        for i in range(0,3):
            a3.append(a.pop(0))
    if(len(a)!=0):
        for i in range(0,3):
            a9.append(a.pop(0))
    if(len(a)!=0):
        for i in range(0,3):
            a5.append(a.pop(0))
    if(len(a)!=0):
        for i in range(0,3):
            a6.append(a.pop(0))
    print 'a1 is',a1
    print 'a2 is',a2
    print 'a3 is',a3
    print 'a9 is',a9
    print 'a5 is',a5
    print 'a6 is',a6
    if(new_list==a1):
        if(t>=abc[0] or t<=efg[0]):
            print "user authorised"
        else:
            print "acess denied"
    elif(new_list==a2):
        if(t>=abc[1] or t<=efg[1]):
            print "user authorised"
        else:
            print "acess denied"
    elif(new_list==a3):
        if(t>=abc[2] or t<=efg[2]):
            print "user authorised"
        else:
            print "acess denied"            
    elif(new_list==a9):
        if(t>=abc[3] or t<=efg[3]):
            print "user authorised"
        else:
            print "acess denied"
    elif(new_list==a5):
        if(t>=abc[4] or t<=efg[4]):
            print "user authorised"
        else:
            print "acess denied"
    elif(new_list==a6):
        if(t>=abc[5] or t<=efg[5]):
            print "user authorised"
        else:
            print "acess denied"
    else:
        print 'Word not in database'
def check2():
    global flag
    flag=0
    gh=en.get()
    if(gh==ert):
        flag=1
        check3(flag,t)
    else:
        flag=0
        print 'You have entered wrong'
def check1():
    global t
    t2=time.time()
    t=t2-t1
    check2()
def gen_random():
    temp=''
    var=''
    a4=[]
    p0=['a','q','w','s','d','z','x','c','e']
    p1=['r','t','y','f','g','h','v','b','n']
    p2=['u','i','o','p','j','k','l','m']
    for k in range(0,6):
        a4.append(random.choice(p0[random.randint(0,8)]+p1[random.randint(0,8)]+p2[random.randint(0,7)]))
    
    for i in range(0,6):
        var +=a4[i]
    return var


root=Tk()
ert=gen_random()
en=Entry(root)
en.grid(row=0,column=1)
Label(root,text='Enter thw word::'+ert).grid(row=0,column=0)
t1=time.time()
Button(root,text="Send",command=check1).grid(row=1,column=1)
root.mainloop()
