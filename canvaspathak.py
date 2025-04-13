import tkinter
import datetime as datetime
from datetime import* 
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
recd=''


t=tkinter.Tk()
t.geometry('1300x700')
t.title("service call management")
#p3=Label(c3,text='service call management',font=('arial',20),bg='lightpink')
#p3.place(x=250,y=7)

def showbuttonSCenter():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='lightblue')
        c3.place(x=500,y=0)
       # p3=Label(c1,text='SCM Project',font=('arial',20,'bold'),bg='lightpink')
       # p3.place(x=20,y=20)
        f=Canvas(c3,height=500,width=600,bg='lightpink')
        f.place(x=80,y=60)
        l6 = Label(c3, text='service center details',bg='lightblue', font=('arial', 10,'bold'))
        l6.place(x=230, y=20)
        #f=Canvas(c3,height=500,width=600,bg='lightpink')
        #f.place(x=80,y=60)
        t.config(bg='lightpink')
        def dest():
            c3.destroy()
        
        
            
            
        
        
        
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select * from service_center where id='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchall()
            
            if data: 
                messagebox.showerror("Error","Data already exist")
            elif len(e1.get())==0 or  len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or len(e6.get())==0:
                
                messagebox.showerror('Invalid','Invalid details')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                xf=e6.get()
                
                sql="insert into service_center values('%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi','saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                db.close()
        
            
        # code for db connectivity button

       

        l6 = Label(c3, text='service center details',bg='lightblue', font=('arial', 30,'bold'))
        l6.place(x=250, y=20)
        l1 = Label(c3, text='Id',bg='lightblue',font=('arial',20,'bold'))
        l1.place(x=200, y=100)

        e1 = Entry(c3, width=30,font=('arial',15,'bold'),bg='lightblue')
        e1.place(x=400, y=100)

        l2 = Label(c3, text='C Name',bg='lightblue',font=('arial',20,'bold'))
        l2.place(x=200, y=150)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=400, y=150)

        l3 = Label(c3, text='Address',bg='lightblue',font=('arial',20,'bold'))
        l3.place(x=200, y=200)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=400, y=200)

        l4 = Label(c3, text='Email',bg='lightblue',font=('arial',20,'bold'))
        l4.place(x=200, y=250)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=400, y=250)

        l5 = Label(c3, text='Phone',bg='lightblue',font=('arial',20,'bold'))
        l5.place(x=200, y=300)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=400, y=300)

        l6 = Label(c3, text='Reg No',bg='lightblue',font=('arial',20,'bold'))
        l6.place(x=200, y=350)

        e6 = Entry(c3, width=30,font=('arial',15))
        e6.place(x=400, y=350)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=250, y=450)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=350, y=450)
        
        
            
            
        
        
        
        
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='lightblue')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
        l6.place(x=200, y=7)
        t.config(bg='lightblue')
        lt = []
        def dest():
            c3.destroy()

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select id from service_center"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = f1.get()
            xe = h1.get()
            xf = s1.get()
            if xa=='':
                messagebox.showerror('Invalid','Please fill valid details ')
            else:    
                sql = "update service_center set cname='%s',address='%s',email='%s',phone='%s',reg='%s' where id=%d" % (xb, xc, xd, xe, xf, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])
                s1.delete(0, data[4])

       # l6 = Label(c3, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
       # l6.place(x=200, y=7)
        a = Label(c3, text='Id',font=('arial',20,'bold'),bg='lightblue')
        a.place(x=100, y=60)
        a1 = ttk.Combobox(c3,width=28,font=('arial',15))
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=60)

        b = Label(c3, text='C Name',font=('arial',20,'bold'),bg='lightblue')
        b.place(x=100, y=100)
        b1 = Entry(c3, width=30,font=('arial',15))
        b1.place(x=300, y=100)
        d = Label(c3, text='Address',font=('arial',20,'bold'),bg='lightblue')
        d.place(x=100, y=140)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=140)
        f = Label(c3, text='Email',font=('arial',20,'bold'),bg='lightblue')
        f.place(x=100, y=180)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=180)
        h = Label(c3, text='Phone',font=('arial',20,'bold'),bg='lightblue')
        h.place(x=100, y=220)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=220)
        s = Label(c3, text='Reg No',font=('arial',20,'bold'),bg='lightblue')
        s.place(x=100, y=260)
        s1 = Entry(c3, width=30,font=('arial',15))
        s1.place(x=300, y=260)
        p = Button(c3, text='update',font=('arial',15), bg='blue', command=updatedata)
        p.place(x=400, y=310)
        p = Button(c3, text='close',font=('arial',15), bg='blue', command=dest)
        p.place(x=500, y=310)

        
       
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='lightblue')
        c3.place(x=500,y=0)
        l6 = Label(t, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
        l6.place(x=650, y=10)
        t.config(bg='lightblue')
        def dest():
            c3.destroy()
            
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select id from service_center"
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            
       

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Please fill valid details')
            else:    
                sql = "delete from service_center where id=%d" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        #l6 = Label(t, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=10)
        a = Label(c3, text='Id',font=('arial',15,'bold'),bg='lightblue')
        a.place(x=150, y=100)
        
        #a1 = Entry(t, width=20,font=('arial',10))
       # a1.place(x=300, y=100)
        a1 = ttk.Combobox(c3,width=20)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=100)
       
        b = Button(c3, text='Delete', bg='blue',font=('arial',15), command=deletedata)
        b.place(x=200, y=200)
        b1 = Button(c3, text='Close', bg='blue',font=('arial',15), command=dest)
        b1.place(x=400, y=200)
        
    def showfind():
        c3=Canvas(t,height=900,width=900,bg='lightblue')
        c3.place(x=500,y=0)
        l6 = Label(t, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
        l6.place(x=650, y=10)
        t.config(bg='lightblue')
        lt = []
        def dest():
            c3.destroy()

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "Select id from service_center"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        # find data using billno as primary key
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            e6.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','Fill data for find')
            else:
                sql = "Select cname,address,email,phone,regno from service_center where id=%d" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])
                e6.insert(0, data[4])
                db.close()
        #l6 = Label(c3, text='service center details',bg='lightblue', font=('arial',30,'bold'))
        #l6.place(x=200, y=7)

        l1 = Label(c3, text='Id',bg='lightblue',font=('arial',20,'bold'))
        l1.place(x=100, y=70)
        
        

        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=200, y=110)

        e1 = ttk.Combobox(c3,font=('arial',13),width=34)
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=70)

        l2 = Label(c3, text='C Name',bg='lightblue',font=('arial',20,'bold'))
        l2.place(x=100, y=150)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=150)

        l3 = Label(c3, text='Address',bg='lightblue',font=('arial',20,'bold'))
        l3.place(x=100, y=200)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=210)

        l4 = Label(c3, text='Email',font=('arial',20,'bold'),bg='lightblue')
        l4.place(x=100, y=250)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=260)

        l5 = Label(c3, text='Phone',font=('arial',20,'bold'))
        l5.place(x=100, y=300)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=310)

        l6 = Label(c3, text='Reg No',font=('arial',20,'bold'))
        l6.place(x=100, y=350)

        e6 = Entry(c3, width=30,font=('arial',15))
        e6.place(x=300, y=360)
        b3=Button(c3,text='close',bg='blue',command=dest,font=('arial',15))
        b3.place(x=150,y=420)

        
    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='lightblue')
        c3.place(x=500,y=0)
        l6 = Label(t, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
        l6.place(x=650, y=10)
        t.config(bg='lightblue')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from service_center"
            cur.execute(sql)
            l6 = Label(c3, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
            l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                
                recd = recd+'\t'+str(res[0])
                recd = recd+'\t'+(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+(res[3])
                recd = recd+'\t'+str(res[4])
                recd = recd+'\t'+str(res[5])
                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)
        
    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='lightblue')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service center details',bg='lightblue', font=('arial', 30,'bold'))
        l6.place(x=220, y=7)
        t.config(bg='lightblue')
        def dest():
            c3.destroy()
        xa = []
        xb = []
        xc = []
        xd = []
        xe = []
        xf = []
        i = 0

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select*from service_center"
            cur.execute(sql)
            #l6 = Label(t, text='service center details', font=('arial', 20,'bold'),bg='lightblue')
           # l6.place(x=150, y=3)
            data = cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
            db.close()

        def first():
            global i
            i = 0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])

        def next():
            global i
            i = i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])

        def previous():
            global i
            i = i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])
        def last():
            global i
            i = len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])

        l1 = Label(c3, text='Id',font=('arial',15,'bold'),bg='lightblue')
        l1.place(x=100, y=60)

        e1 = Label(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        l2 = Label(c3, text='C Name',font=('arial',15,'bold'),bg='lightblue')
        l2.place(x=100, y=100)

        e2 = Label(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='lightblue')
        l3.place(x=100, y=140)
        e3 = Label(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Email',font=('arial',15,'bold'),bg='lightblue')
        l4.place(x=100, y=180)

        e4 = Label(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='lightblue')
        l5.place(x=100, y=220)

        e5 = Label(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        l6 = Label(c3, text='Reg No',font=('arial',15,'bold'),bg='lightblue')
        l6.place(x=100, y=260)

        e6 = Label(c3, width=30,font=('arial',15))
        e6.place(x=300, y=260)

        b1 = Button(c3, text='First',font=('arial',15), bg='blue', command=first)
        b1.place(x=100, y=350)

        b2 = Button(c3, text='Next',font=('arial',15), bg='blue', command=next)
        b2.place(x=200, y=350)
        b3 = Button(c3, text='Previous',font=('arial',15), bg='blue', command=previous)
        b3.place(x=300, y=350)
        b4 = Button(c3, text='Last',font=('arial',15), bg='blue', command=last)
        b4.place(x=400, y=350)
        b4 = Button(c3, text='Close',font=('arial',15), bg='blue', command=dest)
        b4.place(x=500, y=350)
        filldata()
    bc=Label(c2,text='service center',font=('arial',20,'bold'),bg='peach puff')
    bc.place(x=13,y=20)
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='skyblue',command=showinsert)
    b1.place(x=35,y=75)
    b2=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='skyblue',command=showupdate)
    b2.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='skyblue',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='skyblue',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='skyblue',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='skyblue',command=shownevigate)
    b1.place(x=35,y=450)
def showproductcategory():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='lightpink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightpink')
        l6.place(x=200, y=7)
        t.config(bg='lightpink')
        recd=''
        def dest():
            c3.destroy()
            
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            sql="select*from product_category where prodcatid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchall()
            if data:
                messagebox.showerror("error","data already exist")
            elif  len(e1.get())==0 or  len(e2.get())==0 or len(e3.get())==0:
                messagebox.showerror('Invalid','invalid details')
            
           
                
            else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                    cur=db.cursor()
                    xa=e1.get()
                    xb=e2.get()
                    xc=e3.get()
                    
            
                    
                    sql="insert into product_category values('%s','%s','%s')"%(xa,xb,xc)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('hi','saved')
                    db.close()
                    e1.delete(0,100)
                    e2.delete(0,100)
                    e3.delete(0,100)
            
        
            #db.close()
        
       
            
           
        # code for db connectivity button

       

        #l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='lightpink')
        l1.place(x=100, y=60)

        e1 = Entry(c3, width=30,font=('arial',10)
                   )
        e1.place(x=300, y=60)
        
        l2 = Label(c3, text='Cat Name',font=('arial',15,'bold'),bg='lightpink')
        l2.place(x=100, y=100)

        e2 = Entry(c3, width=30,font=('arial',10))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Description',font=('arial',15,'bold'),bg='lightpink')
        l3.place(x=100, y=140)

        e3 = Entry(c3, width=30,font=('arial',10))
        e3.place(x=300, y=140)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=200)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=200, y=200)
        
        #b3 = Button(t, text='check',font=('arial',15,'bold'), bg='blue',command=checkdata)
        #b3.place(x=300, y=200)
        
        
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='lightpink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightpink')
        l6.place(x=200, y=7)
        t.config(bg='lightpink')
        def dest():
            c3.destroy()
        lt = []

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select prodcatid from product_category"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            if xa=='':
                messagebox.showerror('Invalid','Enter data for updates')
            else:    
                sql = "update product_category set catname='%s',description='%s' where prodcatid='%s'" % (xb, xc, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])

        #l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=7)
        a = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='lightpink')
        a.place(x=100, y=60)
        a1 = ttk.Combobox(c3,font=('arial',10),width=28)
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=60)

        b = Label(c3, text='Cat Name',font=('arial',15,'bold'),bg='lightpink')
        b.place(x=100, y=100)
        b1 = Entry(c3, width=30,font=('arial',10))
        b1.place(x=300, y=100)
        d = Label(c3, text='Description',font=('arial',15,'bold'),bg='lightpink')
        d.place(x=100, y=140)
        d1 = Entry(c3, width=30,font=('arial',10))
        d1.place(x=300, y=140)

        p = Button(c3, text='update',font=('arial',15), bg='blue', command=updatedata)
        p.place(x=150, y=200)
        
        p1 = Button(c3, text='close',font=('arial',15), bg='blue', command=dest)
        p1.place(x=250, y=200)

        
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='lightpink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightpink')
        l6.place(x=200, y=15)
        t.config(bg='lightpink')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select prodcatid from product_category"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
       

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Enter data for delete')
            else:
                sql = "delete from product_category where prodcatid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        #l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=15)
        a = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='lightpink')
        a.place(x=150, y=100)
        #a1 = Entry(t, width=20,font=('arial',10))
        #a1.place(x=300, y=100)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=100)
        b = Button(c3, text='Delete',font=('arial',15), bg='blue', command=deletedata)
        b.place(x=170, y=170)
        b1 = Button(c3, text='Close',font=('arial',15), bg='blue', command=dest)
        b1.place(x=300, y=170)

        
    def showfind():
        c3=Canvas(t,height=900,width=900,bg='lightpink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightpink')
        l6.place(x=200, y=7)
        t.config(bg='lightpink')
        def dest():
            c3.destroy()
        lt = []

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "Select prodcatid from product_category"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','Fill details')
            else:
                sql = "Select catname,description from product_category where prodcatid='%s'" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])

            db.close()
        #l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=7)

        l1 = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='lightpink')
        l1.place(x=100, y=60)

        b1 = Button(c3, text='Find',font=('arial',15,), bg='blue', command=finddata)
        b1.place(x=200, y=90)

        e1 = ttk.Combobox(c3,font=('arial',10),width=28)
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=60)

        l2 = Label(c3, text='Cat Name',font=('arial',15,'bold'),bg='lightpink')
        l2.place(x=100, y=140)

        e2 = Entry(c3, width=30,font=('arial',10))
        e2.place(x=300, y=140)

        l3 = Label(c3, text='Description',font=('arial',15,'bold'),bg='lightpink')
        l3.place(x=100, y=190)

        e3 = Entry(c3, width=30,font=('arial',10))
        e3.place(x=300, y=190)
        
        b6 = Button(c3, text='close',font=('arial',15,), bg='blue', command=dest)
        b6.place(x=200, y=230)
    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='lightpink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightpink')
        l6.place(x=200, y=7)
        t.config(bg='lightpink')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from product_category"
            cur.execute(sql)
            l6 = Label(c3, text='product category details', font=('arial', 20,'bold'),bg='lightpink')
            l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+(res[0])
                recd = recd+'\t'+(res[1])
                recd = recd+'\t'+(res[2])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)

    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='lightpink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='product category Details', font=('arial', 20,'bold'),bg='lightpink')
        l6.place(x=150, y=20)
        t.config(bg='lightpink')
        def dest():
            c3.destroy()
        xa = []
        xb = []
        xc = []
        i = 0

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select*from product_category"
            cur.execute(sql)
            #l6 = Label(c3, text='product category Details', font=('arial', 20,'bold'),bg='lightblue')
           # l6.place(x=150, y=20)
            data = cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])

            db.close()

        def first():
            global i
            i = 0
            e1.delete(0, 100)
            e2.delete(0, 100)
            e3.delete(0, 100)

            e1.insert(0, xa[i])
            e2.insert(0, xb[i])
            e3.insert(0, xc[i])

        def next():
            global i
            i = i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])

        def previous():
            global i
            i = i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])

        def last():
            global i
            i = len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])

        l1 = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='lightpink')
        l1.place(x=100, y=100)

        e1 = Label(c3, width=30,font=('arial',15))
        e1.place(x=300, y=100)

        l2 = Label(c3, text='Cat Name',font=('arial',15,'bold'),bg='lightpink')
        l2.place(x=100, y=150)

        e2 = Label(c3, width=30,font=('arial',15))
        e2.place(x=300, y=150)

        l3 = Label(c3, text='Description',font=('arial',15,'bold'),bg='lightpink')
        l3.place(x=100, y=200)

        e3 = Label(c3, width=30,font=('arial',15))
        e3.place(x=300, y=200)

        b1 = Button(c3, text='First',font=('arial',15), bg='blue', command=first)
        b1.place(x=100, y=300)

        b2 = Button(c3, text='Next',font=('arial',15), bg='blue', command=next)
        b2.place(x=200, y=300)
        b3 = Button(c3, text='Previous',font=('arial',15), bg='blue', command=previous)
        b3.place(x=300, y=300)
        b4 = Button(c3, text='Last',font=('arial',15), bg='blue', command=last)
        b4.place(x=450, y=300)
        b5 = Button(c3, text='Close',font=('arial',15), bg='blue', command=dest)
        b5.place(x=550, y=300)
        filldata()
    bd=Label(c2,text='product category',font=('arial',20,'bold'),bg='peach puff')
    bd.place(x=13,y=20)
    b2=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='pink',command=showinsert)
    b2.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='pink',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='pink',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='pink',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='pink',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='pink',command=shownevigate)
    b1.place(x=35,y=450)
def showservicetype():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='cyan')
        c3.place(x=500,y=0)
        
        l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='cyan')
        l6.place(x=200, y=7)
        t.config(bg='cyan')
        def dest():
            c3.destroy()
        
        cdi=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select * from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
            #messagebox.showinfo('hi','inserted')
            
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=int(e4.get())
            xe=e5.get()
            sql="select * from servicetypes where prodcatid='%s'"%(xb)
            cur.execute(sql)
            data=cur.fetchone()
            if data:
                messagebox.showerror('Invalid','Data Already Exist')
            
            else:
                if xa=='' or xb== ''or xc=='' or xe=='':
                    messagebox.showerror('Invalid','Fill Entries')
                
                else:
                    if xd<100:
                        messagebox.showerror("Invalid Entry","Charge can't less 100")
                    else:    
                        sql="insert into servicetype values('%s','%s','%s','%d','%s')" %(xa,xb,xc,xd,xe)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('save','Data successfully save')
                        e1.delete(0,100)
                        e2.delete(0,100)
                        e3.delete(0,100)
                        e4.delete(0,100)
                        e5.delete(0,100)
        #l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Service Id',font=('arial',15,'bold'),bg='cyan')
        l1.place(x=100, y=60)

        e1 = Entry(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        

        l2 = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='cyan')
        l2.place(x=100, y=100)
       

        #e2 = Entry(t, width=30,bg='lightgreen',font=('arial',15))
        #e2.place(x=300, y=100)
        e2=ttk.Combobox(c3,font=('arial',13),width=34)
        filldata()
        e2['values']=cdi
        e2.place(x=300,y=100)

        l3 = Label(c3, text='Service Name',font=('arial',15,'bold'),bg='cyan')
        l3.place(x=100, y=140)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Charges',font=('arial',15,'bold'),bg='cyan')
        l4.place(x=100, y=180)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Time to solve',font=('arial',15,'bold'),bg='cyan')
        l5.place(x=100, y=220)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=300)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=300, y=300)
        
       # b4 = Button(t, text='check',font=('arial',15,'bold'), bg='blue',command=checkdata)
       # b4.place(x=400, y=300)
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='cyan')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='cyan')
        l6.place(x=200, y=7)
        t.config(bg='cyan')
        def dest():
            c3.destroy()
        lt = []

        def filldata():
            db = pymysql.connect(host='localhost', user='root', password='root', database='scm')
            cur = db.cursor()
            sql = "select serviceid from servicetypes"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
           # db.close()
        lt1 = []

        def filldata1():
            db = pymysql.connect(host='localhost', user='root', password='root', database='scm')
            cur = db.cursor()
            sql = "select prodcatid from product_category"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt1.append(res[0])
            db.close()     

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = int(f1.get())
            xe = h1.get()
            if  xa=='':
                messagebox.showerror('Invalid','Fill serivce id for updaating data')
            
            else:
                sql = "update servicetypes set prodcatid='%s',sname='%s',charges=%d,timetosolve='%s' where serviceid='%s'" % (xb, xc, xd, xe, xa)

                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])

       # l6 = Label(c3, text='service type details', font=('arial', 20),bg='lightblue')
       # l6.place(x=200, y=7)
        a = Label(c3, text='Service Id',font=('arial',15,'bold'),bg='cyan')
        a.place(x=100, y=60)
        a1 = ttk.Combobox(c3,font=('arial',13),width=34)
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=60)

        b = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='cyan')
        b.place(x=100, y=100)
        b1 = ttk.Combobox(c3,font=('arial',13),width=34)
        filldata1()
        b1['values'] = lt1
        b1.place(x=300, y=100)
        #b1 = Entry(c3, width=30,font=('arial',15))
        #b1.place(x=300, y=100)
        d = Label(c3, text='Service Name',font=('arial',15,'bold'),bg='cyan')
        d.place(x=100, y=140)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=140)
        f = Label(c3, text='Charges',font=('arial',15,'bold'),bg='cyan')
        f.place(x=100, y=180)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=180)
        h = Label(c3, text='Time to solve',font=('arial',15,'bold'),bg='cyan')
        h.place(x=100, y=220)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=220)

        p = Button(c3, text='update',font=('arial',15,'bold'), bg='blue', command=updatedata)
        p.place(x=150, y=300)
        
        p1 = Button(c3, text='close',font=('arial',15,'bold'), bg='blue', command=dest)
        p1.place(x=250, y=300)

    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='cyan')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='cyan')
        l6.place(x=200, y=10)
        t.config(bg='cyan')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select serviceid from servicetypes"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
       

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill data fro details')
            else:
                sql = "delete from servicetypes where serviceid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        #l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=10)
        a = Label(c3, text='Service Id',font=('arial',15,'bold'),bg='cyan')
        a.place(x=150, y=60)
        #a1 = Entry(t, width=20,font=('arial',15))
        #a1.place(x=300, y=60)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=60)
        b = Button(c3, text='Delete',font=('arial',15,'bold'), bg='blue', command=deletedata)
        b.place(x=250, y=100)
        b1 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b1.place(x=350, y=100)

    def showfind():
        c3=Canvas(t,height=900,width=900,bg='cyan')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='cyan')
        l6.place(x=200, y=7)
        t.config(bg='cyan')
        def dest():
            c3.destroy()
        lt = []

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root', password='root', database='scm')
            cur = db.cursor()
            sql = "Select serviceid from servicetypes"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','Fill id for updating details')
            
            else:
                sql = "Select prodcatid,sname,charges,timetosolve from servicetypes where serviceid='%s'" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])

            db.close()
        #l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='lightblue')
       # l6.place(x=250, y=7)

        l1 = Label(c3, text='Service Id',font=('arial',15,'bold'),bg='cyan')
        l1.place(x=100, y=60)

        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=230, y=90)

        e1 = ttk.Combobox(c3,font=('arial',13),width=34)
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=60)

        l2 = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='cyan')
        l2.place(x=100, y=120)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=120)

        l3 = Label(c3, text='Service Name',font=('arial',15,'bold'),bg='cyan')
        l3.place(x=100, y=180)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=180)

        l4 = Label(c3, text='Charges',font=('arial',15,'bold'),bg='cyan')
        l4.place(x=100, y=240)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=240)

        l5 = Label(c3, text='Time to solve',font=('arial',15,'bold'),bg='cyan')
        l5.place(x=100, y=300)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=300)
        
        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b2.place(x=230, y=360)
    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='cyan')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='cyan')
        l6.place(x=200, y=10)
        t.config(bg='cyan')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from servicetypes"
            cur.execute(sql)
            #l6 = Label(t, text='service type details', font=('arial', 20,'bold'),bg='lightblue')
            #l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+(res[0])
                recd = recd+'\t'+(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+str(res[3])
                recd = recd+'\t'+(res[4])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)

    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='cyan')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='service type details', font=('arial', 20,'bold'),bg='cyan')
        l6.place(x=200, y=4)
        t.config(bg='cyan')
        def dest():
            c3.destroy()
        xa = []
        xb = []
        xc = []
        xd = []
        xe = []

        i = 0

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select*from servicetypes"
            cur.execute(sql)
            #l6 = Label(t, text='service type details', font=('arial', 20,'bold'),bg='lightblue')
            #l6.place(x=150, y=4)
            data = cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])

            db.close()

        def first():
            global i
            i = 0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=str(xd[i]))
            e5.config(text=xe[i])

        def next():
            global i
            i = i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=str(xd[i]))
            e5.config(text=xe[i])

        def previous():
            global i
            i = i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=str(xd[i]))
            e5.config(text=xe[i])

        def last():
            global i
            i = len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=xa[i])
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=str(xd[i]))
            e5.config(text=xe[i])

        l1 = Label(c3, text='Service Id',font=('arial',15,'bold'),bg='cyan')
        l1.place(x=100, y=60)

        e1 = Label(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        l2 = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='cyan')
        l2.place(x=100, y=100)

        e2 = Label(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Service Name',font=('arial',15,'bold'),bg='cyan')
        l3.place(x=100, y=140)
        e3 = Label(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Charges',font=('arial',15,'bold'),bg='cyan')
        l4.place(x=100, y=180)

        e4 = Label(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Time to solve',font=('arial',15,'bold'),bg='cyan')
        l5.place(x=100, y=220)

        e5 = Label(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        b1 = Button(c3, text='First',font=('arial',15,'bold'), bg='blue', command=first)
        b1.place(x=100, y=300)

        b2 = Button(c3, text='Next',font=('arial',15,'bold'), bg='blue', command=next)
        b2.place(x=200, y=300)
        b3 = Button(c3, text='Previous',font=('arial',15,'bold'), bg='blue', command=previous)
        b3.place(x=300, y=300)
        b4 = Button(c3, text='Last',font=('arial',15,'bold'), bg='blue', command=last)
        b4.place(x=450, y=300)
        b5 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b5.place(x=550, y=300)
        filldata()
        

    st=Label(c2,text='service type',font=('arial',20,'bold'),bg='peach puff')
    st.place(x=13,y=20)    
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='cyan',command=showinsert)
    b1.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='cyan',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='cyan',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='cyan',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='cyan',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='cyan',command=shownevigate)
    b1.place(x=35,y=450)
    
def showengineers():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='white')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='white')
        l6.place(x=200, y=7)
        t.config(bg='white')
        recd=''
        cdi=[] 
        def dest():
            cdi.clear()
            c3.destroy()
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                sql="select count(*)from engineers where engid='%s'"%(xa)
                cur.execute(sql)
                dta=cur.fetchall()
                if data[0]==0:
                    messagebox.showinfo('hii','ok go')
                else:
                
                 cdi.append(res[0])
            db.close()
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*) from engineers where engid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchall()
            if (e1.get())==0 or  (e2.get())==0 or (e3.get())==0 or (e4.get())==0 or (e5.get())==0  or (e7.get())==0:
                messagebox.showerror('Error','Invalid')
            elif data:
                    messagebox.showerror('Invalid','Invalid  details')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                xf=e6.get()
                xg=e7.get()
        
                
                sql="insert into engineers values('%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi','saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
        
        
       
        

        #l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Engineer id',font=('arial',15,'bold'),bg='white')
        l1.place(x=100, y=60)

        e1 = Entry(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        

        l2 = Label(c3, text='Engineer Name',font=('arial',15,'bold'),bg='white')
        l2.place(x=100, y=100)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='white')
        l3.place(x=100, y=140)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='white')
        l4.place(x=100, y=180)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Email',font=('arial',15,'bold'),bg='white')
        l5.place(x=100, y=220)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        l6 = Label(c3, text='Prodcat id',font=('arial',15,'bold'),bg='white')
        l6.place(x=100, y=260)

        #e6 = Entry(t, width=30,bg='lightgreen',font=('arial',15))
        #e6.place(x=300, y=260)
        e6=ttk.Combobox(c3,font=('arial',13),width=34)
        filldata()
        e6['values']=cdi
        e6.place(x=300,y=260)

        l7 = Label(c3, text='Status',font=('arial',15,'bold'),bg='white')
        l7.place(x=100, y=300)

        e7 = Entry(c3, width=30,font=('arial',15))
        e7.place(x=300, y=300)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=350)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=200, y=350)
        
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='white')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='white')
        l6.place(x=200, y=7)
        t.config(bg='gray')
        def dest():
            c3.destroy()
        lt = []

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select engid from engineers"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root', password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = f1.get()
            xe = h1.get()
            xf = g1.get()
            xg = s1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill id for updating data')
            else:
                sql = "update engineers set ename='%s',address='%s',phone='%s',email='%s',prodcatid='%s',status='%s' where engid='%s'" % (xb, xc, xd, xe, xf, xg, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])
                g1.delete(0, data[4])
                s1.delete(0, data[5])

       # l6 = Label(t, text='engineer details', font=('arial', 20,'bold'),bg='lightblue')
       # l6.place(x=200, y=7)
        a = Label(c3, text='Engineer id',font=('arial',15,'bold'),bg='white')
        a.place(x=100, y=60)
        a1 = ttk.Combobox(c3,width=34,font=('arial',13))
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=60)

        b = Label(c3, text='Engineer Name',font=('arial',15,'bold'),bg='white')
        b.place(x=100, y=100)
        b1 = Entry(c3, width=30,font=('arial',15))
        b1.place(x=300, y=100)
        d = Label(c3, text='Address',font=('arial',15,'bold'),bg='white')
        d.place(x=100, y=140)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=140)
        f = Label(c3, text='Phone',font=('arial',15,'bold'),bg='white')
        f.place(x=100, y=180)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=180)
        h = Label(c3, text='Email',font=('arial',15,'bold'),bg='white')
        h.place(x=100, y=220)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=220)
        g = Label(c3, text='Prodcat id',font=('arial',15,'bold'),bg='white')
        g.place(x=100, y=260)
        g1 = Entry(c3, width=30,font=('arial',15))
        g1.place(x=300, y=260)
        s = Label(c3, text='Status',font=('arial',15,'bold'),bg='white')
        s.place(x=100, y=300)
        s1 = Entry(c3, width=30,font=('arial',15))
        s1.place(x=300, y=300)
        b = Button(c3, text='update',font=('arial',15,'bold'), bg='blue', command=updatedata)
        b.place(x=350, y=350)
        bt = Button(c3, text='close',font=('arial',15,'bold'), bg='blue', command=dest)
        bt.place(x=450, y=350)
        
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='white')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='white')
        l6.place(x=200, y=10)
        t.config(bg='white')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select engid from engineers"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
       

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill id for delete data')
            else:    
                sql = "delete from engineers where engid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        #l6 = Label(c3, text='engineer details', font=('arial', 20,'bold'),bg='lightblue')
       # l6.place(x=200, y=10)
        a = Label(c3, text='Engineer id',font=('arial',15,'bold'),bg='white')
        a.place(x=150, y=60)
        #a1 = Entry(t, width=20,font=('arial',15))
        #a1.place(x=300, y=60)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=60)
        b = Button(c3, text='Delete',font=('arial',15,'bold'), bg='blue', command=deletedata)
        b.place(x=170, y=100)
        b1 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b1.place(x=300, y=100)
    def showfind():
        c3=Canvas(t,height=900,width=900,bg='white')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='white')
        l6.place(x=200, y=7)
        t.config(bg='white')
        def dest():
            c3.destroy()
        
        lt = []

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "Select engid from engineers"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            e6.delete(0, 100)
            e7.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','fill data fro find')
            else:
                sql = "Select ename,address,phone,email,prodcatid,status from engineers where engid='%s'" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])
                e6.insert(0, data[4])
                e7.insert(0, data[5])

            db.close()
        #l6 = Label(t, text='engineer details', font=('arial', 20,'bold'),bg='lightblue')
        #l6.place(x=200, y=7)

        l1 = Label(c3, text='Engineer id',font=('arial',15,'bold'),bg='white')
        l1.place(x=100, y=60)

        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=200, y=90)

        e1 = ttk.Combobox(c3,font=('arial',13),width=34)
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=60)

        l2 = Label(c3, text='Engineer Name',font=('arial',15,'bold'),bg='white')
        l2.place(x=100, y=140)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=140)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='white')
        l3.place(x=100, y=180)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=180)

        l4 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='white')
        l4.place(x=100, y=220)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=220)

        l5 = Label(c3, text='Email',font=('arial',15,'bold'),bg='white')
        l5.place(x=100, y=260)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=260)

        l6 = Label(c3, text='Prodcat id',font=('arial',15,'bold'),bg='white')
        l6.place(x=100, y=300)

        e6 = Entry(c3, width=30,font=('arial',15))
        e6.place(x=300, y=300)

        l7 = Label(c3, text='Status',font=('arial',15,'bold'),bg='white')
        l7.place(x=100, y=340)

        e7 = Entry(c3, width=30,font=('arial',15))
        e7.place(x=300, y=340)
        
        b3 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b3.place(x=200, y=380)
    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='white')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='white')
        l6.place(x=200, y=10)
        t.config(bg='white')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from engineers"
            cur.execute(sql)
           # l6 = Label(t, text='engineer details', font=('arial', 30,'bold'),bg='lightblue')
           # l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+(res[0])
                recd = recd+'\t'+(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+(res[3])
                recd = recd+'\t'+(res[4])
                recd = recd+'\t'+(res[5])
                recd = recd+'\t'+(res[6])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)
        
    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='white')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='engineer Details', font=('arial', 20,'bold'),bg='white')
        l6.place(x=200, y=4)
        t.config(bg='white')
        def dest():
            c3.destroy()
        xa = []
        xb = []
        xc = []
        xd = []
        xe = []
        xf = []
        xg = []
        i = 0

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select*from engineers"
            cur.execute(sql)
            #l6 = Label(t, text='engineer details', font=('arial', 20,'bold'),bg='lightblue')
            #l6.place(x=150, y=4)
            data = cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
                xg.append(res[6])
            db.close()

        def first():
            global i
            i = 0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e7.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])
            e7.config(text=xg[i])

        def next():
            global i
            i = i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e7.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])
            e7.config(text=xg[i])

        def previous():
            global i
            i = i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e7.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])
            e7.config(text=xg[i])
        def last():
            global i
            i = len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            e7.config(text='')
            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])
            e7.config(text=xg[i])

        l1 = Label(c3, text='Engineer id',font=('arial',15,'bold'),bg='white')
        l1.place(x=100, y=60)

        e1 = Label(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        l2 = Label(c3, text='Engineer Name',font=('arial',15,'bold'),bg='white')
        l2.place(x=100, y=100)

        e2 = Label(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='white')
        l3.place(x=100, y=140)
        e3 = Label(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='white')
        l4.place(x=100, y=180)

        e4 = Label(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Email',font=('arial',15,'bold'),bg='white')
        l5.place(x=100, y=220)

        e5 = Label(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        l6 = Label(c3, text='Prodcat id',font=('arial',15,'bold'),bg='white')
        l6.place(x=100, y=260)

        e6 = Label(c3, width=30,font=('arial',15))
        e6.place(x=300, y=260)

        l7 = Label(c3, text='Status',font=('arial',15,'bold'),bg='white')
        l7.place(x=100, y=300)

        e7 = Label(c3, width=30,font=('arial',15))
        e7.place(x=300, y=300)

        b1 = Button(c3, text='First',font=('arial',15,'bold'), bg='blue', command=first)
        b1.place(x=100, y=350)

        b2 = Button(c3, text='Next',font=('arial',15,'bold'), bg='blue', command=next)
        b2.place(x=200, y=350)
        b3 = Button(c3, text='Previous',font=('arial',15,'bold'), bg='blue', command=previous)
        b3.place(x=300, y=350)
        b4 = Button(c3, text='Last',font=('arial',15,'bold'), bg='blue', command=last)
        b4.place(x=450, y=350)
        b5 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b5.place(x=550, y=350)
        filldata()
    bf=Label(c2,text='engineers',font=('arial',25,'bold'),bg='peach puff')
    bf.place(x=20,y=20)     
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='white',command=showinsert)
    b1.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='white',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='white',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='white',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='white',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='white',command=shownevigate)
    b1.place(x=35,y=450)
def showcustomer():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='deep pink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='deep pink')
        l6.place(x=300, y=7)
        t.config(bg='deep pink')
        recd=''
        
        cdi=[]
        def dest():
            cdi.clear()
            c3.destroy()
       
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select prodcatid from product_category"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                sql="select count(*)from customers where custid='%s'"%(xa)
                cur.execute(sql)
                dta=cur.fetchall()
                if data[0]==0:
                    messagebox.showinfo('hii','ok go')
                else:
                
                 cdi.append(res[0])
            db.close()
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select * from customers where custid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchall()
            if data:
                messagebox.showerror("Error","Invalid details")
            elif (e1.get())==0 or  (e2.get())==0 or (e3.get())==0 or (e4.get())==0 or (e5.get())==0  or (e6.get())==0:
                messagebox.showerror('Invalid','Invalid details')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                cur=db.cursor()
                xa=e1.get()
                xb=e2.get()
                xc=e3.get()
                xd=e4.get()
                xe=e5.get()
                xf=e6.get()
                
        
                
                sql="insert into customers values('%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi','saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                
        
        
        

        #l6 = Label(t, text='customer details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='deep pink')
        l1.place(x=100, y=60)

        e1 = Entry(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        

        l2 = Label(c3, text='Customer Name',font=('arial',15,'bold'),bg='deep pink')
        l2.place(x=100, y=100)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='deep pink')
        l3.place(x=100, y=140)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Email',font=('arial',15,'bold'),bg='deep pink')
        l4.place(x=100, y=180)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='deep pink')
        l5.place(x=100, y=220)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        l6 = Label(c3, text='Prodcat id',font=('arial',15,'bold'),bg='deep pink')
        l6.place(x=100, y=260)

        #e6 = Entry(t, width=30,font=('arial',15))
        #e6.place(x=300, y=260)
        e6=ttk.Combobox(c3,font=('arial',13),width=34)
        filldata()
        e6['values']=cdi
        e6.place(x=300,y=260)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=350)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=200, y=350)
        
       # b3 = Button(t, text='Check',font=('arial',15,'bold'), bg='blue',command=checkdata)
        #b3.place(x=300, y=350)
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='deep pink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='deep pink')
        l6.place(x=300, y=7)
        t.config(bg='deep pink')
        lt = []
        def dest():
            c3.destroy()

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select custid from customers"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = f1.get()
            xe = h1.get()
            xf = g1.get()
            if xa=='':
                messagebox.showerror('Invalid','fill customer id')
            else:
                sql = "update customers set cname='%s',address='%s',email='%s',phone='%s',prodcatid where custid='%s'" % (xb, xc, xd, xe, xf, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])
                g1.delete(0, data[4])
                s1.delete(0, data[5])

        #l6 = Label(t, text='customer details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        a = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='deep pink')
        a.place(x=100, y=60)
        a1 = ttk.Combobox(c3,font=('arial',13),width=34)
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=60)

        b = Label(c3, text='Customer Name',font=('arial',15,'bold'),bg='deep pink')
        b.place(x=100, y=100)
        b1 = Entry(c3, width=30,font=('arial',15))
        b1.place(x=300, y=100)
        d = Label(c3, text='Address',font=('arial',15,'bold'),bg='deep pink')
        d.place(x=100, y=140)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=140)
        f = Label(c3, text='Email',font=('arial',15,'bold'),bg='deep pink')
        f.place(x=100, y=180)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=180)
        h = Label(c3, text='Phone',font=('arial',15,'bold'),bg='deep pink')
        h.place(x=100, y=220)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=220)
        g = Label(c3, text='Prodcat Id',font=('arial',15,'bold'),bg='deep pink')
        g.place(x=100, y=260)
        g1 = Entry(c3, width=30,font=('arial',15))
        g1.place(x=300, y=260)

        b = Button(c3, text='update',font=('arial',15,'bold'), bg='blue', command=updatedata)
        b.place(x=200, y=300)
        bt = Button(c3, text='close',font=('arial',15,'bold'), bg='blue', command=dest)
        bt.place(x=300, y=300)
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='deep pink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='deep pink')
        l6.place(x=300, y=7)
        t.config(bg='deep pink')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select custid from customers"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])
       

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill custmer id')
            else:
                sql = "delete from customers where custid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        l6 = Label(c3, text='customer details', font=('arial', 20),bg='deep pink')
        l6.place(x=200, y=10)
        a = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='deep pink')
        a.place(x=150, y=60)
        #a1 = Entry(t, width=20,font=('arial',15))
       # a1.place(x=300, y=60)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=60)
        b = Button(c3, text='Delete',font=('arial',15,'bold'), bg='blue', command=deletedata)
        b.place(x=170, y=100)
        b = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b.place(x=300, y=100)

    def showfind():
        c3=Canvas(t,height=900,width=900,bg='deep pink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='deep pink')
        l6.place(x=300, y=7)
        t.config(bg='deep pink')
        lt = []
        def dest():
            c3.destroy()

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "Select custid from customers"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            e6.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','Fill data for updates')
            else:
                sql = "Select cname,address,email,phone,prodcatid from customers where custid='%s'" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])
                e6.insert(0, data[4])

            db.close()
       # l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='yellow')
       # l6.place(x=200, y=7)

        l1 = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='deep pink')
        l1.place(x=100, y=80)
        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=220, y=100)

       

        e1 = ttk.Combobox(c3,font=('arial',13),width=34)
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=80)
        

        l2 = Label(c3, text='customer name',font=('arial',15,'bold'),bg='deep pink')
        l2.place(x=100, y=140)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=140)

        l3 = Label(c3, text='address',font=('arial',15,'bold'),bg='deep pink')
        l3.place(x=100, y=200)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=200)

        l4 = Label(c3, text='email',font=('arial',15,'bold'),bg='deep pink')
        l4.place(x=100, y=260)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=260)

        l5 = Label(c3, text='phone',font=('arial',15,'bold'),bg='deep pink')
        l5.place(x=100, y=320)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=320)

        l6 = Label(c3, text='prodcat id',font=('arial',15,'bold'),bg='deep pink')
        l6.place(x=100, y=380)

        e6 = Entry(c3, width=30,font=('arial',15))
        e6.place(x=300, y=380)
        
        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b2.place(x=150, y=440)
    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='deep pink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='deep pink')
        l6.place(x=300, y=10)
        t.config(bg='deep pink')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from customers"
            cur.execute(sql)
            #l6 = Label(t, text='customer details', font=('arial', 20,'bold'),bg='yellow')
           # l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+(res[0])
                recd = recd+'\t'+(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+(res[3])
                recd = recd+'\t'+(res[4])
                recd = recd+'\t'+(res[5])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)
        
    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='deep pink')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='customer details', font=('arial', 20,'bold'),bg='deep pink')
        l6.place(x=300, y=4)
        t.config(bg='deep pink')
        def dest():
            c3.destroy()
        xa = []
        xb = []
        xc = []
        xd = []
        xe = []
        xf = []
        i = 0

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select*from customers"
            cur.execute(sql)
            #l6 = Label(t, text='customer details', font=('arial', 20,'bold'),bg='yellow')
            #l6.place(x=200, y=4)
            data = cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
            db.close()

        def first():
            global i
            i = 0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])


        def next():
            global i
            i = i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])


        def previous():
            global i
            i = i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])


        def last():
            global i
            i = len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=xf[i])

        l1 = Label(c3, text='Id',font=('arial',15,'bold'),bg='deep pink')
        l1.place(x=100, y=60)

        e1 = Label(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        l2 = Label(c3, text='C Name',font=('arial',15,'bold'),bg='deep pink')
        l2.place(x=100, y=100)

        e2 = Label(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='deep pink')
        l3.place(x=100, y=140)
        e3 = Label(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Email',font=('arial',15,'bold'),bg='deep pink')
        l4.place(x=100, y=180)

        e4 = Label(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='deep pink')
        l5.place(x=100, y=220)

        e5 = Label(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        l6 = Label(c3, text='regno',font=('arial',15,'bold'),bg='deep pink')
        l6.place(x=100, y=260)

        e6 = Label(c3, width=30,font=('arial',15))
        e6.place(x=300, y=260)

        b1 = Button(c3, text='First',font=('arial',15,'bold'), bg='blue', command=first)
        b1.place(x=100, y=350)

        b2 = Button(c3, text='Next',font=('arial',15,'bold'), bg='blue', command=next)
        b2.place(x=200, y=350)
        b3 = Button(c3, text='Previous',font=('arial',15,'bold'), bg='blue', command=previous)
        b3.place(x=300, y=350)
        b4 = Button(c3, text='Last',font=('arial',15,'bold'), bg='blue', command=last)
        b4.place(x=450, y=350)
        b5 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b5.place(x=550, y=350)
        filldata()

    bg=Label(c2,text='customers',font=('arial',25,'bold'),bg='peach puff')
    bg.place(x=17,y=20)     
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='deeppink',command=showinsert)
    b1.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='deeppink',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='deeppink',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='deeppink',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='deeppink',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='deeppink',command=shownevigate)
    b1.place(x=35,y=450)
def showstaff():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='thistle')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='thistle')
        l6.place(x=200, y=7)
        t.config(bg='thistle')
        recd=''
        def dest():
            c3.destroy()
        def savedata():
            if len(e1.get())==0 or  len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
                    
                    
                    messagebox.showerror('hii','Mndatory to fil all details')
            else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
                    cur=db.cursor()
                    xa=e1.get()
                    xb=e2.get()
                    xc=e3.get()
                    xd=e4.get()
                    xe=e5.get()
                    
                    
            
                    
                    sql="insert into staff values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('hi','saved')
                    db.close()
                    e1.delete(0,100)
                    e2.delete(0,100)
                    e3.delete(0,100)
                    e4.delete(0,100)
                    e5.delete(0,100)
                    
                    
            
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select count(*)from staff where staffid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hii','ok go')
            else:
                messagebox.showinfo('hii','already exit')
            db.close()      
            
        

        

        #l6 = Label(t, text='staff details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='thistle')
        l1.place(x=100, y=60)
        

        e1 = Entry(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)

        l2 = Label(c3, text='Staff Name',font=('arial',15,'bold'),bg='thistle')
        l2.place(x=100, y=100)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='thistle')
        l3.place(x=100, y=140)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Email',font=('arial',15,'bold'),bg='thistle')
        l4.place(x=100, y=180)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='thistle')
        l5.place(x=100, y=220)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=300)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=200, y=300)
        b3 = Button(c3, text='Check',font=('arial',15,'bold'), bg='blue',command=checkdata)
        b3.place(x=300, y=300)

        
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='thistle')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='thistle')
        l6.place(x=200, y=7)
        t.config(bg='thistle')
        def dest():
            c3.destroy()
        lt = []

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select staffid from staff"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = f1.get()
            xe = h1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill staffid fro update details')
            else:    
                sql = "update staff set staffname='%s',address='%s',email='%s',phone='%s' where staffid=%d" % (xb, xc, xd, xe, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])

        #l6 = Label(t, text='staff details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        a = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='thistle')
        a.place(x=100, y=60)
        a1 = ttk.Combobox(c3,width=28,font=('arial',15))
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=60)

        b = Label(c3, text='Staff Name',font=('arial',15,'bold'),bg='thistle')
        b.place(x=100, y=100)
        b1 = Entry(c3, width=30,font=('arial',15))
        b1.place(x=300, y=100)
        d = Label(c3, text='Address',font=('arial',15,'bold'),bg='thistle')
        d.place(x=100, y=140)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=140)
        f = Label(c3, text='Email',font=('arial',15,'bold'),bg='thistle')
        f.place(x=100, y=180)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=180)
        h = Label(c3, text='Phone',font=('arial',15,'bold'),bg='thistle')
        h.place(x=100, y=220)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=220)

        p = Button(c3, text='update',font=('arial',15,'bold'), bg='blue', command=updatedata)
        p.place(x=150, y=300)
        p1 = Button(c3, text='close',font=('arial',15,'bold'), bg='blue', command=dest)
        p1.place(x=250, y=300)
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='thistle')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='thistle')
        l6.place(x=200, y=10)
        t.config(bg='thistle')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select staffid from staff"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill id for delete data')
            else:
                sql = "delete from staff where staffid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        #l6 = Label(t, text='staff details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=10)
        a = Label(c3, text='staff id',font=('arial',15,'bold'),bg='thistle')
        a.place(x=150, y=60)
        #a1 = Entry(t, width=20,font=('arial',15))
        #a1.place(x=300, y=60)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=60)
        b = Button(c3, text='Delete',font=('arial',15,'bold'), bg='blue', command=deletedata)
        b.place(x=170, y=100)
        b1 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b1.place(x=300, y=100)
    def showfind():
        c3=Canvas(t,height=900,width=900,bg='thistle')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='thistle')
        l6.place(x=200, y=7)
        t.config(bg='thistle')
        def dest():
            c3.destroy()
        lt = []
        

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "Select staffid from staff"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','fill id for finding data')
            
            else:
                sql = "Select staffname,address,email,phone from staff where staffid=%d" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])

            db.close()
        #l6 = Label(t, text='staff details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)

        l1 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='thistle')
        l1.place(x=100, y=80)
        
       
        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=200, y=90)
        
        e1 = ttk.Combobox(c3,width=34,font=('arial',13))
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=80)


        

        l2 = Label(c3, text='Staff Name',font=('arial',15,'bold'),bg='thistle')
        l2.place(x=100, y=140)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=140)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='thistle')
        l3.place(x=100, y=200)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=200)

        l4 = Label(c3, text='Email',font=('arial',15,'bold'),bg='thistle')
        l4.place(x=100, y=260)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=260)

        l5 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='thistle')
        l5.place(x=100, y=320)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=320)
        
        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b2.place(x=200, y=380)

    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='thistle')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='thistle')
        l6.place(x=200, y=10)
        t.config(bg='thistle')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from staff"
            cur.execute(sql)
            #l6 = Label(t, text='staff details', font=('arial', 20,'bold'),bg='yellow')
            #l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+str(res[0])
                recd = recd+'\t'+(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+(res[3])
                recd = recd+'\t'+(res[4])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)
        
    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='thistle')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='thistle')
        l6.place(x=200, y=7)
        t.config(bg='thistle')
        def dest():
            c3.destroy()
        xa = []
        xb = []
        xc = []
        xd = []
        xe = []

        i = 0

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select*from staff"
            cur.execute(sql)
            #l6 = Label(c3, text='staff details', font=('arial', 20,'bold'),bg='yellow')
            #l6.place(x=200, y=7)
            data = cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])

            db.close()

        def first():
            global i
            i = 0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])


        def next():
            global i
            i = i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])

        def previous():
            global i
            i = i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])

        def last():
            global i
            i = len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')

            e1.config(text=str(xa[i]))
            e2.config(text=xb[i])
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])

        l1 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='thistle')
        l1.place(x=100, y=60)

        e1 = Label(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)
        l2 = Label(c3, text='Staff Name',font=('arial',15,'bold'),bg='thistle')
        l2.place(x=100, y=100)

        e2 = Label(c3, width=30,font=('arial',15))
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Address',font=('arial',15,'bold'),bg='thistle')
        l3.place(x=100, y=140)
        e3 = Label(c3, width=30,font=('arial',15))
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Email',font=('arial',15,'bold'),bg='thistle')
        l4.place(x=100, y=180)

        e4 = Label(c3, width=30,font=('arial',15))
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Phone',font=('arial',15,'bold'),bg='thistle')
        l5.place(x=100, y=220)

        e5 = Label(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        b1 = Button(c3, text='First',font=('arial',15,'bold'), bg='blue', command=first)
        b1.place(x=100, y=300)

        b2 = Button(c3, text='Next',font=('arial',15,'bold'), bg='blue', command=next)
        b2.place(x=200, y=300)
        b3 = Button(c3, text='Previous',font=('arial',15,'bold'), bg='blue', command=previous)
        b3.place(x=300, y=300)
        b4 = Button(c3, text='Last',font=('arial',15,'bold'), bg='blue', command=last)
        b4.place(x=450, y=300)
        b5 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b5.place(x=550, y=300)
        filldata()
    bh=Label(c2,text='staff',font=('arial',25,'bold'),bg='peach puff')
    bh.place(x=60,y=20)     
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='thistle',command=showinsert)
    b1.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='thistle',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='thistle',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='thistle',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='thistle',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='thistle',command=shownevigate)
    b1.place(x=35,y=450)
def showcallassignment():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='lightyellow')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='lightyellow')
        l6.place(x=200, y=7)
        t.config(bg='lightyellow')
        recd=''
        cdi=[]
        def dest():
            cdi.clear()
            c3.destroy()
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from staff"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                
                cdi.append(res[0])
            db.close()
        cdi1=[]
        #def dest():
            #cdi1.clear()
            #c3.destroy()
        def filldata1():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                
                cdi1.append(res[0])
            db.close()    
        cdi2=[]
        #def dest():
            #cdi2.clear()
            #c3.destroy()
        def filldata2():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select engid from engineers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                 
                cdi2.append(res[0])
            db.close()
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=int(e6.get())
            sql="select * from callassignment where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data:
                messagebox.showerror('Invalid','Data Already Exist')
            
            else:
                if xa=='' or xb== ''or xc=='' or xd==''or xe=='':
                    messagebox.showerror('Invalid','Fill Entries')
                
                else:
                    if xf<100:
                        messagebox.showerror("Invalid Entry","Charge can't less 100")
                    else:    
                        sql="insert into callassignment values('%s','%s','%s','%s','%s','%d')" %(xa,xb,xc,xd,xe,xf)
                        cur.execute(sql)
                        db.commit()
                        db.close()
                        messagebox.showinfo('save','Data successfully save')
                        e1.delete(0,100)
                        e2.delete(0,100)
                        e3.delete(0,100)
                        e4.delete(0,100)
                        e5.delete(0,100)
                        e6.delete(0,100)
       

        #l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='lightyellow')
        l1.place(x=100, y=60)

        e1 = Entry(c3, width=30,font=('arial',15))
        e1.place(x=300, y=60)

        l2 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='lightyellow')
        l2.place(x=100, y=100)

        #e2 = Entry(t, width=30,font=('arial',15))
       # e2.place(x=300, y=100)
        e2=ttk.Combobox(c3,font=('arial',13),width=34)
        filldata()
        e2['values']=cdi
        e2.place(x=300,y=100)

        l3 = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='lightyellow')
        l3.place(x=100, y=140)

        #e3 = Entry(t, width=30,font=('arial',15))
        #e3.place(x=300, y=140)
        e3=ttk.Combobox(c3,font=('arial',13),width=34)
        filldata1()
        e3['values']=cdi1
        e3.place(x=300,y=140)

        l4 = Label(c3, text='Engineer Id',font=('arial',15,'bold'),bg='lightyellow')
        l4.place(x=100, y=180)

        #e4 = Entry(t, width=30,font=('arial',15))
        #e4.place(x=300, y=180)
        e4=ttk.Combobox(c3,font=('arial',13),width=34)
        filldata2()
        e4['values']=cdi2
        e4.place(x=300,y=180)

        l5 = Label(c3, text='Date of call',font=('arial',15,'bold'),bg='lightyellow')
        l5.place(x=100, y=220)
        date=datetime.today().strftime('%Y-%m-%d')
        e5=Entry(c3,width='30',font=('arial',15))
        e5.insert(0,date)

        #e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=220)

        l6 = Label(c3, text='Charge',font=('arial',15,'bold'),bg='lightyellow')
        l6.place(x=100, y=260)

        e6 = Entry(c3, width=30,font=('arial',15))
        e6.place(x=300, y=260)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=350)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=200, y=350)
       # b3 = Button(c3, text='Check',font=('arial',15,'bold'), bg='blue',command=checkdata)
       # b3.place(x=300, y=350)

    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='lightyellow')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='lightyellow')
        l6.place(x=200, y=7)
        t.config(bg='lightyellow')
        def dest():
            c3.destroy()
        lt = []

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select callid from callassignment"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = f1.get()
            xe = h1.get()
            xf = g1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill id for updates')
            else:           
                sql = "update callassignment set staffid=%d,custid='%s',engid='%s',dateofcall='%s',charges=%d where callid='%s'" % (xb, xc, xd, xe, xf, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])
                g1.delete(0, data[4])
                s1.delete(0, data[5])

        #l6 = Label(t, text='call assignment details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        a = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='lightyellow')
        a.place(x=100, y=80)
        a1 = ttk.Combobox(c3,width=34,font=('arial',13))
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=80)

        b = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='lightyellow')
        b.place(x=100, y=120)
        b1 = Entry(c3, width=30,font=('arial',15))
        b1.place(x=300, y=120)
        d = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='lightyellow')
        d.place(x=100, y=160)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=160)
        f = Label(c3, text='Engineer Id',font=('arial',15,'bold'),bg='lightyellow')
        f.place(x=100, y=200)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=200)
        h = Label(c3, text='Date of call',font=('arial',15,'bold'),bg='lightyellow')
        h.place(x=100, y=240)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=240)
        g = Label(c3, text='Charge',font=('arial',15,'bold'),bg='lightyellow')
        g.place(x=100, y=280)
        g1 = Entry(c3, width=30,font=('arial',15))
        g1.place(x=300, y=280)

        b = Button(c3, text='update',font=('arial',15,'bold'), bg='blue', command=updatedata)
        b.place(x=150, y=350)
        b1 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b1.place(x=250, y=350)
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='lightyellow')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='lightyellow')
        l6.place(x=200, y=10)
        t.config(bg='lightyellow')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select callid from callassignment"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','fill id for update')
            else:    
                sql = "delete from callassignment where callid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
        #l6 = Label(t, text='call assignment details', font=('arial', 20),bg='yellow')
        #l6.place(x=200, y=10)
        a = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='lightyellow')
        a.place(x=150, y=60)
        #a1 = Entry(t, width=20,font=('arial',15))
        #a1.place(x=300, y=60)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=60)
        b = Button(c3, text='Delete',font=('arial',15,'bold'), bg='blue', command=deletedata)
        b.place(x=170, y=100)
        b1 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b1.place(x=300, y=100)
    def showfind():
        c3=Canvas(t,height=900,width=900,bg='lightyellow')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='lightyellow')
        l6.place(x=200, y=7)
        t.config(bg='lightyellow')
        def dest():
            c3.destroy()
        lt = []
        

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root', password='root', database='scm')
            cur = db.cursor()
            sql = "Select callid from callassignment"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()


        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            e6.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','Fill id for finding data')
            else:    
                sql = "Select staffid,custid,engid,dateofcall,charges from callassignment where callid='%s'" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])
                e6.insert(0, data[4])

            db.close()
        #l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)

        l1 = Label(c3, text='call id',font=('arial',15,'bold'),bg='lightyellow')
        l1.place(x=100, y=80)

        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=200, y=90)

        e1 = ttk.Combobox(c3,width=34,font=('arial',13))
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=80)

        l2 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='lightyellow')
        l2.place(x=100, y=140)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=140)

        l3 = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='lightyellow')
        l3.place(x=100, y=200)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=200)

        l4 = Label(c3, text='Engineer Id',font=('arial',15,'bold'),bg='lightyellow')
        l4.place(x=100, y=260)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=260)

        l5 = Label(c3, text='Date of call',font=('arial',15,'bold'),bg='lightyellow')
        l5.place(x=100, y=320)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=320)

        l6 = Label(c3, text='Charge',font=('arial',15,'bold'),bg='lightyellow')
        l6.place(x=100, y=380)

        e6 = Entry(c3, width=30,font=('arial',15))
        e6.place(x=300, y=380)
        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b2.place(x=200, y=440)     
    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='lightyellow')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='lightyellow')
        l6.place(x=200, y=10)
        t.config(bg='lightyellow')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from callassignment"
            cur.execute(sql)
            #l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='yellow')
            #l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+(res[0])
                recd = recd+'\t'+str(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+(res[3])
                recd = recd+'\t'+(res[4])
                recd = recd+'\t'+str(res[5])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)
    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='lightyellow')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call assignment details', font=('arial', 20,'bold'),bg='lightyellow')
        l6.place(x=200, y=4)
        t.config(bg='lightyellow')
        def dest():
            c3.destroy()
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from callassignment"
            cur.execute(sql)
            #l6=Label(c3,text='call assignment Details',font=('arial',20,'bold'),bg='yellow')
            #l6.place(x=150,y=4)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
            db.close()
            
        def first():
            global i
            i=0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=str(xf[i]))
            
        def next():
            global i
            i=i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=str(xf[i]))
            
        def previous():
            global i
            i=i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=str(xf[i]))
            
        def last():
            global i
            i=len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            e6.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            e6.config(text=str(xf[i]))
           
        l1=Label(c3,text='Call Id',font=('arial',15,'bold'),bg='lightyellow')
        l1.place(x=100,y=60)

        e1=Label(c3,width=30,font=('arial',15))
        e1.place(x=300,y=60)
        l2=Label(c3,text='Staff Id',font=('arial',15,'bold'),bg='lightyellow')
        l2.place(x=100,y=100)

        e2=Label(c3,width=30,font=('arial',15))
        e2.place(x=300,y=100)

        l3=Label(c3,text='Customer Id',font=('arial',15,'bold'),bg='lightyellow')
        l3.place(x=100,y=140)
        e3=Label(c3,width=30,font=('arial',15))
        e3.place(x=300,y=140)

        l4=Label(c3,text='Engineer Id',font=('arial',15,'bold'),bg='lightyellow')
        l4.place(x=100,y=180)

        e4=Label(c3,width=30,font=('arial',15))
        e4.place(x=300,y=180)

        l5=Label(c3,text='Date Of Call',font=('arial',15,'bold'),bg='lightyellow')
        l5.place(x=100,y=220)

        e5=Label(c3,width=30,font=('arial',15))
        e5.place(x=300,y=220)
         
        l6=Label(c3,text='Charge',font=('arial',15,'bold'),bg='lightyellow')
        l6.place(x=100,y=260)

        e6=Label(c3,width=30,font=('arial',15))
        e6.place(x=300,y=260)

        b1=Button(c3,text='first',font=('arial',15,'bold'),bg='blue',command=first)
        b1.place(x=100,y=300)

        b2=Button(c3,text='next',font=('arial',15,'bold'),bg='blue',command=next)
        b2.place(x=200,y=300)
        b3=Button(c3,text='previous',font=('arial',15,'bold'),bg='blue',command=previous)
        b3.place(x=300,y=300)
        b4=Button(c3,text='last',font=('arial',15,'bold'),bg='blue',command=last)
        b4.place(x=450,y=300)
        b5=Button(c3,text='Close',font=('arial',15,'bold'),bg='blue',command=dest)
        b5.place(x=550,y=300)
        filldata()             
    bi=Label(c2,text='call assignment',font=('arial',25,'bold'),bg='peach puff')
    bi.place(x=2,y=20)     
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='lightyellow',command=showinsert)
    b1.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='lightyellow',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='lightyellow',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='lightyellow',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='lightyellow',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='lightyellow',command=shownevigate)
    b1.place(x=35,y=450)
def showcallclose():
    def showinsert():
        c3=Canvas(t,height=900,width=900,bg='steelblue4')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='steelblue4')
        l6.place(x=200, y=7)
        t.config(bg='steelblue4')
        recd=''
        cdi=[]
        def dest():
            cdi.clear()
            c3.destroy()
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select callid from callassignment"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                
                cdi.append(res[0])
            db.close()
        cdi1=[]
        #def dest():
           # cdi1.clear()
           # t.destroy()
        def filldata1():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select staffid from staff"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                
                cdi1.append(res[0])
            db.close()    
        cdi2=[]
       # def dest():
           # cdi2.clear()
           # t.destroy()
        def filldata2():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select custid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                 
                cdi2.append(res[0])
            db.close()       
        cdi3=[]
        #def dest():
          # cdi3.clear()
          # t.destroy()
        def filldata3():
           db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
           cur=db.cursor()
           sql="select engid from engineers"
           cur.execute(sql)
           data=cur.fetchall()
           for res in data:
                
               cdi3.append(res[0])
           db.close()       
            
        def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            
            sql="select * from callclose where callid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data:
                messagebox.showerror('Invalid','Data Already Exist')
            
           # else:
                #if xa=='' or xb== ''or xc=='' or xd==''or xe=='':
                   # messagebox.showerror('Invalid','Fill Entries')
                
                #else:
                    #if xf<100:
                        #messagebox.showerror("Invalid Entry","Charge can't less 100")
            else:    
                sql="insert into callclose values('%s','%s','%s','%s','%s')" %(xa,xb,xc,xd,xe)
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('save','Data successfully save')
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                
                        
                    
            
       # def checkdata():
           # db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
           # cur=db.cursor()
           # xa=e1.get()
           # sql="select count(*)from callclose where callid='%s'"%(xa)
           # cur.execute(sql)
            #data=cur.fetchone()
            #if data[0]==0:
               # messagebox.showinfo('hii','ok go')
           # else:
               # messagebox.showinfo('hii','already exit')
           # db.close()      
                 
       

        #l6 = Label(t, text='call close details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        l1 = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='steelblue4')
        l1.place(x=100, y=60)
        
        #e1 = Entry(t, width=30,font=('arial',15))
       # e1.place(x=300, y=60)
        e1 = ttk.Combobox(c3,width=34)
        # call function filldata below
        filldata()
        e1['values'] = cdi
        e1.place(x=300, y=60)
       

        l2 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='steelblue4')
        l2.place(x=100, y=100)

        #e2 = Entry(t, width=30,font=('arial',15))
        #e2.place(x=300, y=100)
        e2 = ttk.Combobox(c3,width=34)
        # call function filldata below
        filldata1()
        e2['values'] = cdi1
        e2.place(x=300, y=100)

        l3 = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='steelblue4')
        l3.place(x=100, y=140)

        #e3 = Entry(t, width=30,font=('arial',15))
        #e3.place(x=300, y=140)
        e3 = ttk.Combobox(c3,width=34)
        # call function filldata below
        filldata2()
        e3['values'] =cdi2
        e3.place(x=300, y=140)

        l4 = Label(c3, text='Engineer Id',font=('arial',15,'bold'),bg='steelblue4')
        l4.place(x=100, y=180)

        #e4 = Entry(t, width=30,font=('arial',15))
        #e4.place(x=300, y=180)
        e4 = ttk.Combobox(c3,width=34)
        # call function filldata below
        filldata3()
        e4['values'] =cdi3
        e4.place(x=300, y=180)

        l5 = Label(c3, text='Date of close',font=('arial',15,'bold'),bg='steelblue4')
        l5.place(x=100, y=220)
        date=datetime.today().strftime('%Y-%m-%d')
        e5=Entry(c3,width='25',font=('arial',13))
        e5.insert(0,date)

        #e5 = Entry(c3, width=34,font=('arial',10))
        e5.place(x=300, y=220)

        b1 = Button(c3, text='Save',font=('arial',15,'bold'), bg='blue', command=savedata)
        b1.place(x=100, y=300)

        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue',command=dest)
        b2.place(x=200, y=300)
       # b3 = Button(c3, text='Check',font=('arial',15,'bold'), bg='blue',command=checkdata)
       # b3.place(x=300, y=300)
        
    def showupdate():
        c3=Canvas(t,height=900,width=900,bg='steelblue4')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='steelblue4')
        l6.place(x=200, y=7)
        t.config(bg='steelblue4')
        def dest():
            c3.destroy()
        lt = []

        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select callid from callclose"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        def updatedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            xd = f1.get()
            xe = h1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill data for updates')
            else:
                
                sql = "update callclose set staffid='%s',custid='%s',engid='%s',dateofclose='%s' where callid='%s'" % ( xb, xc, xd, xe, xa)
    
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'update done')
                a1.delete(0, 100)
    
                b1.delete(0, data[0])
                d1.delete(0, data[1])
                f1.delete(0, data[2])
                h1.delete(0, data[3])

        #l6 = Label(t, text='call close details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)
        a = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='steelblue4')
        a.place(x=100, y=80)
        a1 = ttk.Combobox(c3,width=28,font=('arial',15))
        filldata()
        a1['values'] = lt
        a1.place(x=300, y=80)

        b = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='steelblue4')
        b.place(x=100, y=120)
        b1 = Entry(c3, width=30,font=('arial',15))
        b1.place(x=300, y=120)
        d = Label(c3, text='Customer Id',font=('arial',15,'bold'),bg='steelblue4')
        d.place(x=100, y=160)
        d1 = Entry(c3, width=30,font=('arial',15))
        d1.place(x=300, y=160)
        f = Label(c3, text='Engineer Id',font=('arial',15,'bold'),bg='steelblue4')
        f.place(x=100, y=200)
        f1 = Entry(c3, width=30,font=('arial',15))
        f1.place(x=300, y=200)
        h = Label(c3, text='Date of close',font=('arial',15,'bold'),bg='steelblue4')
        h.place(x=100, y=240)
        h1 = Entry(c3, width=30,font=('arial',15))
        h1.place(x=300, y=240)

        p = Button(c3, text='update',font=('arial',15,'bold'), bg='blue', command=updatedata)
        p.place(x=150, y=300)
        p1 = Button(c3, text='close',font=('arial',15,'bold'), bg='blue', command=dest)
        p1.place(x=250, y=300)
        
    def showdelete():
        c3=Canvas(t,height=900,width=900,bg='steelblue4')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='steelblue4')
        l6.place(x=200, y=10)
        t.config(bg='steelblue4')
        def dest():
            c3.destroy()
        cdi=[]
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select callid from callclose"
        
            
            cur.execute(sql)           
            data=cur.fetchall()
            for res in data:
                cdi.append(res[0])

        def deletedata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = a1.get()
            if xa=='':
                messagebox.showerror('Invalid','Fill data for delete')
            else:    
                sql = "delete from callclose where callid='%s'" % (xa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('hi', 'deleted')
                db.close()
                a1.delete(0, 100)
       # l6 = Label(t, text='call close details', font=('arial', 20,'bold'),bg='yellow')
       # l6.place(x=200, y=10)
        a = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='steelblue4')
        a.place(x=150, y=60)
        #a1 = Entry(t, width=20,font=('arial',15))
        #a1.place(x=250, y=60)
        a1 = ttk.Combobox(c3)
        filldata()
        a1['values'] = cdi
        a1.place(x=300, y=60)
        b = Button(c3, text='Delete',font=('arial',15,'bold'), bg='blue', command=deletedata)
        b.place(x=170, y=100)
        b1 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b1.place(x=300, y=100)
        
    def showfind():
        c3=Canvas(t,height=900,width=900,bg='steelblue4')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='steelblue4')
        l6.place(x=200, y=7)
        t.config(bg='steelblue4')
        def dest():
            c3.destroy()
        lt = []

        # combobox function
        def filldata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "Select callid from callassignment"
            cur.execute(sql)
            data = cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()

        
        def finddata():
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            xa = e1.get()
            # delete previous data find before
            e2.delete(0, 100)
            e3.delete(0, 100)
            e4.delete(0, 100)
            e5.delete(0, 100)
            if xa=='':
                messagebox.showerror('Invalid','Fill id for finding data')
            else:    
                sql = "Select staffid,custid,engid,dateofclose from callclose where callid='%s'" % (xa)
                cur.execute(sql)
                # fetchone to get data using index positions
                data = cur.fetchone()
                e2.insert(0, data[0])
                e3.insert(0, data[1])
                e4.insert(0, data[2])
                e5.insert(0, data[3])

            db.close()
        #l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='yellow')
        #l6.place(x=200, y=7)

        l1 = Label(c3, text='Call Id',font=('arial',15,'bold'),bg='steelblue4')
        l1.place(x=100, y=60)

        b1 = Button(c3, text='Find',font=('arial',15,'bold'), bg='blue', command=finddata)
        b1.place(x=200, y=90)

        e1 = ttk.Combobox(c3,font=('arial',13),width=34)
        # call function filldata below
        filldata()
        e1['values'] = lt
        e1.place(x=300, y=60)

        l2 = Label(c3, text='Staff Id',font=('arial',15,'bold'),bg='steelblue4')
        l2.place(x=100, y=120)

        e2 = Entry(c3, width=30,font=('arial',15))
        e2.place(x=300, y=120)

        l3 = Label(c3, text='customer Id',font=('arial',15,'bold'),bg='steelblue4')
        l3.place(x=100, y=180)

        e3 = Entry(c3, width=30,font=('arial',15))
        e3.place(x=300, y=180)

        l4 = Label(c3, text='Engineer Id',font=('arial',15,'bold'),bg='steelblue4')
        l4.place(x=100, y=240)

        e4 = Entry(c3, width=30,font=('arial',15))
        e4.place(x=300, y=240)

        l5 = Label(c3, text='Date of close',font=('arial',15,'bold'),bg='steelblue4')
        l5.place(x=100, y=300)

        e5 = Entry(c3, width=30,font=('arial',15))
        e5.place(x=300, y=300)
        b2 = Button(c3, text='Close',font=('arial',15,'bold'), bg='blue', command=dest)
        b2.place(x=200, y=360)

    def showdatashow():
        c3=Canvas(t,height=900,width=900,bg='steelblue4')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='steelblue4')
        l6.place(x=200, y=10)
        t.config(bg='steelblue4')
        def showdata():
            global recd
            db = pymysql.connect(host='localhost', user='root',password='root', database='scm')
            cur = db.cursor()
            sql = "select * from callclose"
            cur.execute(sql)
           # l6 = Label(t, text='call close details', font=('arial', 20,'bold'),bg='yellow')
           # l6.place(x=200, y=10)
            data = cur.fetchall()
            for res in data:
                recd = recd+'\t'+(res[0])
                recd = recd+'\t'+str(res[1])
                recd = recd+'\t'+(res[2])
                recd = recd+'\t'+(res[3])
                recd = recd+'\t'+(res[4])

                recd = recd+'\n'
            db.close()

        e = Text(c3, width=150, height=50,font=('arial',15))
        showdata()
        e.insert(tkinter.END, recd)
        e.place(x=10, y=70)
    def shownevigate():
        c3=Canvas(t,height=900,width=900,bg='steelblue4')
        c3.place(x=500,y=0)
        l6 = Label(c3, text='call close details', font=('arial', 20,'bold'),bg='steelblue4')
        l6.place(x=200, y=4)
        t.config(bg='steelblue4')
        def dest():
            c3.destroy()
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            sql="select*from callclose"
            cur.execute(sql)
           # l6=Label(t,text='Call Close Details',font=('arial',20,'bold'),bg='yellow')
           # l6.place(x=150,y=4)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                
            db.close()
            
        def first():
            global i
            i=0
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            
            
        def next():
            global i
            i=i+1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            
            
        def previous():
            global i
            i=i-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            
            
        def last():
            global i
            i=len(xa)-1
            e1.config(text='')
            e2.config(text='')
            e3.config(text='')
            e4.config(text='')
            e5.config(text='')
            
            e1.config(text=xa[i])
            e2.config(text=str(xb[i]))
            e3.config(text=xc[i])
            e4.config(text=xd[i])
            e5.config(text=xe[i])
            
           
        l1=Label(c3,text='Call Id',font=('arial',15,'bold'),bg='steelblue4')
        l1.place(x=100,y=60)

        e1=Label(c3,width=30,font=('arial',15))
        e1.place(x=300,y=60)
        l2=Label(c3,text='Staff Id',font=('arial',15,'bold'),bg='steelblue4')
        l2.place(x=100,y=100)

        e2=Label(c3,width=30,font=('arial',15))
        e2.place(x=300,y=100)

        l3=Label(c3,text='Customer Id',font=('arial',15,'bold'),bg='steelblue4')
        l3.place(x=100,y=140)
        e3=Label(c3,width=30,font=('arial',15))
        e3.place(x=300,y=140)

        l4=Label(c3,text='Engineer Id',font=('arial',15,'bold'),bg='steelblue4')
        l4.place(x=100,y=180)

        e4=Label(c3,width=30,font=('arial',15))
        e4.place(x=300,y=180)

        l5=Label(c3,text='Date Of Close',font=('arial',15,'bold'),bg='steelblue4')
        l5.place(x=100,y=220)

        e5=Label(c3,width=30,font=('arial',15))
        e5.place(x=300,y=220)
         
        

        b1=Button(c3,text='First',font=('arial',15,'bold'),bg='blue',command=first)
        b1.place(x=100,y=300)

        b2=Button(c3,text='Next',font=('arial',15,'bold'),bg='blue',command=next)
        b2.place(x=200,y=300)
        b3=Button(c3,text='Previous',font=('arial',15,'bold'),bg='blue',command=previous)
        b3.place(x=300,y=300)
        b4=Button(c3,text='Last',font=('arial',15,'bold'),bg='blue',command=last)
        b4.place(x=450,y=300)
        b5=Button(c3,text='Close',font=('arial',15,'bold'),bg='blue',command=dest)
        b5.place(x=550,y=300)
        filldata()                  
    bk=Label(c2,text='call close',font=('arial',25,'bold'),bg='peach puff')
    bk.place(x=25,y=20) 
    b1=Button(c2,text='Insert',font=('Arial',12,'bold'),width=14,bg='steelblue4',command=showinsert)
    b1.place(x=35,y=75)
    b1=Button(c2,text='Update',font=('Arial',12,'bold'),width=14,bg='steelblue4',command=showupdate)
    b1.place(x=35,y=150)
    b1=Button(c2,text='Delete',font=('Arial',12,'bold'),width=14,bg='steelblue4',command=showdelete)
    b1.place(x=35,y=225)
    b1=Button(c2,text='Find',font=('Arial',12,'bold'),width=14,bg='steelblue4',command=showfind)
    b1.place(x=35,y=300)
    b1=Button(c2,text='Show',font=('Arial',12,'bold'),width=14,bg='steelblue4',command=showdatashow)
    b1.place(x=35,y=375)
    b1=Button(c2,text='Navigate',font=('Arial',12,'bold'),width=14,bg='steelblue4',command=shownevigate)
    b1.place(x=35,y=450)

    
    
        
c1=Canvas(t,height=900,width=250,bg='bisque')
c1.place(x=0,y=0)
c2=Canvas(t,height=900,width=250,bg='peach puff')
c2.place(x=250,y=0)
c3=Canvas(t,height=900,width=900,bg='navajo white')
c3.place(x=500,y=0)
p3=Label(c1,text='SCM Project',font=('arial',20,'bold'),bg='bisque')
p3.place(x=25,y=20)
b=Button(c1,text='Service centre',width=14,font=('arial',12,'bold'),bg='sky blue',command=showbuttonSCenter)
b.place(x=35,y=75)
c=Button(c1,text='Product Category',width=14,font=('arial',12,'bold'),bg='light pink',command=showproductcategory)
c.place(x=35,y=150)
d=Button(c1,text='Service Type',width=14,font=('arial',12,'bold'),bg='cyan',command=showservicetype)
d.place(x=35,y=225)
e=Button(c1,text='Engineers',width=14,font=('arial',12,'bold'),bg='white',command=showengineers)
e.place(x=35,y=300)
f=Button(c1,text='Customers',width=14,font=('arial',12,'bold'),bg='deep pink',command=showcustomer)
f.place(x=35,y=375)
g=Button(c1,text='Staff',width=14,font=('arial',12,'bold'),bg='thistle',command=showstaff)
g.place(x=35,y=450)
h=Button(c1,text='Call Assignment',width=14,font=('arial',12,'bold'),bg='light yellow',command=showcallassignment)
h.place(x=35,y=525)
j=Button(c1,text='Call Close',width=14,font=('arial',12,'bold'),bg='steel blue4',command=showcallclose)
j.place(x=35,y=600)
t.mainloop()
