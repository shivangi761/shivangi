import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
recd=''
def showinsert():
    t=tkinter.Tk()
    t.geometry('640x480')
    t.title('page1db')
    #code for db connectivity button
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=int(e2.get())
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=int(e6.get())
        
        
        sql="insert into callassignment values('%s',%d,'%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Saved')
        db.close()
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        

    l6=Label(t,text='call assignment details',font=('arial',20))
    l6.place(x=200,y=7)
    l1=Label(t,text='call id')
    l1.place(x=100,y=60)

    e1=Entry(t,width=40)
    e1.place(x=200,y=60)

    l2=Label(t,text='staff id')
    l2.place(x=100,y=100)

    e2=Entry(t,width=40)
    e2.place(x=200,y=100)

    l3=Label(t,text='customer id')
    l3.place(x=100,y=140)

    e3=Entry(t,width=40)
    e3.place(x=200,y=140)

    l4=Label(t,text='engineer id')
    l4.place(x=100,y=180)

    e4=Entry(t,width=40)
    e4.place(x=200,y=180)

    l5=Label(t,text='date of call')
    l5.place(x=100,y=220)

    e5=Entry(t,width=40)
    e5.place(x=200,y=220)
    
    l6=Label(t,text='charge')
    l6.place(x=100,y=260)

    e6=Entry(t,width=40)
    e6.place(x=200,y=260)
    
    
    

    b1=Button(t,text='Save',command=savedata)
    b1.place(x=100,y=350)

    b2=Button(t,text='Close')
    b2.place(x=200,y=350)
    t.mainloop()
def showfind():
    t=tkinter.Tk()
    t.geometry('640x480')
    t.title('page2db')
    lt=[]

    #combobox function
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="Select callid from callassignment"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()

    #find data using billno as primary key
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        #delete previous data find before
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        
        sql="Select staffid,custid,engid,dateofcall,charges from callassignment where callid='%s'"%(xa)
        cur.execute(sql)
        #fetchone to get data using index positions
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        
        
        db.close()
    l6=Label(t,text='call assignment details',font=('arial',20))
    l6.place(x=200,y=7)  

    l1=Label(t,text='call id')
    l1.place(x=100,y=60)

    b1=Button(t,text='Find',command=finddata)
    b1.place(x=100,y=90)

    e1=ttk.Combobox(t)
    #call function filldata below
    filldata()
    e1['values']=lt
    e1.place(x=200,y=60)

    l2=Label(t,text='staff id')
    l2.place(x=100,y=120)

    e2=Entry(t,width=40)
    e2.place(x=200,y=120)

    l3=Label(t,text='customer id')
    l3.place(x=100,y=180)

    e3=Entry(t,width=40)
    e3.place(x=200,y=180)

    l4=Label(t,text='engineer id')
    l4.place(x=100,y=240)

    e4=Entry(t,width=40)
    e4.place(x=200,y=240)

    l5=Label(t,text='date of call')
    l5.place(x=100,y=300)

    e5=Entry(t,width=40)
    e5.place(x=200,y=300)
    
    l6=Label(t,text='charge')
    l6.place(x=100,y=360)

    e6=Entry(t,width=40)
    e6.place(x=200,y=360)
    
    
    
    
    
def showdelete():
    t=tkinter.Tk()
    t.geometry('640x480')
    t.title('page3db')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=a1.get()
        
        sql="delete from callassignment where callid='%s'"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','deleted')
        db.close()
        a1.delete(0,100)
    l6=Label(t,text='call assignment details',font=('arial',20))
    l6.place(x=200,y=10)    
    a=Label(t,text='call id')
    a.place(x=150,y=60)
    a1=Entry(t,width=20)
    a1.place(x=250,y=60)
    b=Button(t,text='Delete',command=deletedata)
    b.place(x=170,y=100)
def showupdate():
    t=tkinter.Tk()
    t.geometry('640x480')
    t.title('page4db')
    lt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select callid from callassignment"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()


    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=a1.get()
        xb=b1.get()
        xc=d1.get()
        xd=f1.get()
        xe=h1.get()
        xf=g1.get()
        
        
        sql="update callassignment set staffid=%d,custid='%s',engid='%s',dateofcall='%s',charges=%d where callid='%s'"%(xb,xc,xd,xe,xf,xa)
         
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('hi','update done')
        a1.delete(0,100)
         
        b1.delete(0,data[0])
        d1.delete(0,data[1])
        f1.delete(0,data[2])
        h1.delete(0,data[3])
        g1.delete(0,data[4])
        s1.delete(0,data[5])
        
        
    l6=Label(t,text='call assignment details',font=('arial',20))
    l6.place(x=200,y=7)           
    a=Label(t,text='call id')
    a.place(x=100,y=60)
    a1=ttk.Combobox(t)
    filldata()
    a1['values']=lt
    a1.place(x=200,y=60)
    
    b=Label(t,text='staff id')
    b.place(x=100,y=100)
    b1=Entry(t,width=40)
    b1.place(x=200,y=100)
    d=Label(t,text='customer id')
    d.place(x=100,y=140)
    d1=Entry(t,width=40)
    d1.place(x=200,y=140)
    f=Label(t,text='engineer id')
    f.place(x=100,y=180)
    f1=Entry(t,width=40)
    f1.place(x=200,y=180)
    h=Label(t,text='date of call')
    h.place(x=100,y=220)
    h1=Entry(t,width=40)
    h1.place(x=200,y=220)
    g=Label(t,text='charge')
    g.place(x=100,y=260)
    g1=Entry(t,width=40)
    g1.place(x=200,y=260)
    
    b=Button(t,text='update',command=updatedata)
    b.place(x=150,y=350)
    t.mainloop()
def showdatashow():
    t=tkinter.Tk()
    t.geometry('640x480')
    t.title('page5db')
    def showdata():
        global recd
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from callassignment"
        cur.execute(sql)
        l6=Label(t,text='call assignment details',font=('arial',20))
        l6.place(x=200,y=10)
        data=cur.fetchall()
        for res in data:
            recd=recd+'\t'+(res[0])
            recd=recd+'\t'+str(res[1])
            recd=recd+'\t'+(res[2])
            recd=recd+'\t'+(res[3])
            recd=recd+'\t'+(res[4])
            recd=recd+'\t'+str(res[5])
            
            
            recd=recd+'\n'
        db.close()
    
    
    e=Text(t,width=150,height=50)
    showdata()
    e.insert(tkinter.END,recd)
    e.place(x=10,y=70)
    t.mainloop()
    



t=tkinter.Tk()
t.geometry('640x480')
t.title('database tkinter')
b1=Button(t,text='Insert',command=showinsert)
b1.place(x=50,y=50)
b2=Button(t,text='Find',command=showfind)
b2.place(x=100,y=50)
b3=Button(t,text='Delete',command=showdelete)
b3.place(x=150,y=50)
b4=Button(t,text='Update',command=showupdate)
b4.place(x=200,y=50)
b5=Button(t,text='Show',command=showdatashow)
b5.place(x=260,y=50)
t.mainloop()