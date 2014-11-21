import time
from time1 import *
######new_var=time1.
def crack1(new_var):
    i1=i2=i3=0
    while(1:)
        if(len(new_var)!=0):
            t_new1=time.time()
            leng=len(new var)
            for i in range(0,6):
                if(new_var[i] in a0):
                    i1=i1+1
                elif(new_var[i] in a1):
                    i2=i2+1
                elif(new_var[i] in a2):
                    i3=i3+1
            new_list.append(i1)
            new_list.append(i2)
            new_list.append(i3)
            if(new_list==a1):
                t_new2=time.time()
                t_final=t_new2-t_new1
                time.sleep(int(b[0])-t_final)
########                return
            elif(new_list==a2):
                t_new2=time.time()
                t_final=t_new2-t_new1
                time.sleep(int(b[1])-t_final)
########                return
            elif(new_list==a3):
                t_new2=time.time()
                t_final=t_new2-t_new1
                time.sleep(int(b[2])-t_final)
########                return
            elif(new_list==a4):
                t_new2=time.time()
                t_final=t_new2-t_new1
                time.sleep(int(b[3])-t_final)
########                return
            elif(new_list==a5):
                t_new2=time.time()
                t_final=t_new2-t_new1
                time.sleep(int(b[4])-t_final)
########                return
            elif(new_list==a6):
                t_new2=time.time()
                t_final=t_new2-t_new1
                time.sleep(int(b[5])-t_final)
########                return
c=lite.connect("final_project1.db")
cur=c.cursor()
res=cur.execute("select * from pro_crypto")
a0=['a','q','w','s','d','z','x','c','e']
a1=['r','t','y','f','g','h','v','b','n']
a2=['u','i','o','p','j','k','l','m']
for i in res:
    print i
    for j in range(0,3):
        a.append(eval(str(i[j])))
    print a
    b.append(eval(str(i[3])))
    print b
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
        a4.append(a.pop(0))
if(len(a)!=0):
    for i in range(0,3):
        a5.append(a.pop(0))
if(len(a)!=0):
    for i in range(0,3):
        a6.append(a.pop(0))
