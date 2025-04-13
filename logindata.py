import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from canvaslabel1 import *
 
from mailutil import*
t=tkinter.Tk()
t.geometry('840x480')
t.title('login1db')
t.config(bg='pink')
def dest():
    t.destroy()
    

    
def check():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=b.get()
    xb=e.get()
    sql="select count(*)from logindata where userid='%s' and password='%s'"%(xa,xb)
    cur.execute(sql)
    data=cur.fetchone()
    if data[0]==0:
        messagebox.showinfo('hii','failed')
    else:
        showcanvaslabel()
       
    db.close()

def checkemail():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=b.get()
    sql="select email,password from logindata where userid='%s'"%(xa)
    cur.execute(sql)
    
    data=cur.fetchone()
    r=data[0]
    s=data[1]
    messagebox.showinfo('hii',r+'..'+s)
    sendingmail(r,s)
    db.close()

     
        
       
a=Label(t,text='Username',font=('arial',20,'bold'),bg='pink')
a.place(x=50,y=60)

b=Entry(t,width=20,font=('arial',15))
b.place(x=250,y=70)


d=Label(t,text='Password',font=('arial',20,'bold'),bg='pink')
d.place(x=50,y=140)

e=Entry(t,width=20,show='*',font=('arial',15))
e.place(x=250,y=140)

#bt=Button(t,text='ok',font=('arial',20),bg='lightgreen')
#bt.place(x=200,y=230)
bt=Button(t,text='cancel',font=('arial',20),bg='lightblue',command=dest)
bt.place(x=50,y=230)
bt=Button(t,text='forget password',font=('arial',20),bg='blue',command=checkemail)
bt.place(x=200,y=230)
bt=Button(t,text='login',font=('arial',20),bg='blue',command=check)
bt.place(x=450,y=230)

t.mainloop()