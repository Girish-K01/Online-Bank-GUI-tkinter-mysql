#...................................................................................IMPORTS....................................................................................................
#change account details
#customer id not appearing one day skip
global dp
global utdu
import random
from tkinter import *
import tkinter.font as font
import mysql.connector as x
c=x.connect(host="localhost",user="root",password="g46902105k",database="girish")
k=c.cursor()
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
from datetime import date
utdu=datetime.date.today()
#..........................................................................................................................................................................
 
#............................................PRE-TEST OR TEMPORARY FUNCTIONS.................................................................................................................
def c1():
    return
def coexit():
    root.destroy()
def pin():
    global dsss
    b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dsss=""
    for i in range(4):
        a=str(random.randint(0,9))
        c=random.choice(b)
        dsss=dsss+a+c
    return
pin()
#................................................................ ONLY MAIN PROGRAM - REST OF THE PROGRAMS ARE FUNCTIONS ............................................................................................    
root=Tk()
root.title("OBGUI-ONLINE BANK MANAGEMENT SYSTEM")
root.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
root.geometry("2500x2500+0+0")
myfont=font.Font(size=30)
myfont1=font.Font(size=20)
myfont2=font.Font(size=30)
img1=ImageTk.PhotoImage(Image.open("bank1.jpg"))
pimg=Label(image=img1)
pimg.pack()
lbl=Label(root,text="OBGUI-Online Bank Graphical user interface",font=myfont,fg="chocolate1",bg="LightGoldenrod",relief="raised").place(x=400,y=5)
lbl1=Label(root,text="Welcome user,please login into your account or create a account",font=myfont1,fg="chocolate1",bg="LightGoldenrod",relief="raised").place(x=400,y=70)
lbl2=Label(root,text="By (Girish K)",font=myfont1,fg="chocolate1",bg="LightGoldenrod",relief="raised").place(x=400,y=650)
#THE EXIT BUTTONS...............................................................AND OTHER FUNCTIONS..........................................................................
def ww():
    d.destroy()
    root.deiconify()
#.......................................................................................................................
def www():
    cp.destroy()
    root.deiconify()
#.......................................................................................................................
def ew():
    bp.destroy()
    d.deiconify()
#.......................................................................................................................
def eww():
    sv.destroy()
    bp.deiconify()
#.......................................................................................................................
def lcp():
    ccp.destroy()
    bp.deiconify()
#.......................................................................................................................
def lp():
    llp.destroy()
    bp.deiconify()
#..........................................................................................................................
def uu():
    dep.destroy()
    sv.deiconify()
#........................................................................................................................
def ur():
    wtd.destroy()
    sv.deiconify()
#.........................................................................................................................
def ut():
    re.destroy()
    bp.deiconify()
#..........................................................................................................................
def uw():
    bor.destroy()
    bp.deiconify()
#...........................................................................................................................
def uq():
    ror.destroy()
    bp.deiconify()
#...............................................................................................................................................
    
#.......................................................................................................................

#..............................................CONDITIONS FOR SOME PROCESSES.......... MOST IMPORTANT FUNCTION IN THE PROGRAM..............................................................
def conj():
    global we1
    
    global state
    global estate

    global tab3
    global tab2
    global tab1

    global yu
    global uy
    global uyu

    global oda
    global oca
    global sabl
    global toi
    global nsno

    global xoy
    global cca
    global odz
    global ccaa
    global klg
    
    global taz
    global dpb
    global kyz
    global sate
    global ytaz

    global dss

    #...............
    k.execute("select * from customdet where Name=%s;",(we1,))
    yuy=k.fetchall()
    dss=yuy[0][6]
    #................................................................
    state=""
    k.execute("select * from %s order by sno desc limit 1"%(tab1,))
    uyu=k.fetchall()
    osno=uyu[0][0]
    oda=uyu[0][2]
    oca=uyu[0][3]
    sabl=uyu[0][5]
    toi=uyu[0][6]
    
    nsno=int(osno)+1
    #..................................................................

    estate=""
    k.execute("select * from %s order by sno desc limit 1"%(tab2,))
    uy=k.fetchall()
    xoc=uy[0][0]
    cca=uy[0][2]
    estate=uy[0][3]
    odz=uy[0][4]
    xoy=int(xoc)+1
    
    inha=int(cca)*0.35
    ccaa=int(cca)+inha
    
    #.............................................

    k.execute("select * from %s order by sno desc limit 1"%(tab3,))
    yu=k.fetchall()
    kwz=yu[0][0]
    dpb=yu[0][2]
    kyz=yu[0][3]
    sate=yu[0][4]
    ytaz=yu[0][5]

    taz=int(kwz)+1
    if dpb==0:
        state="free"
    else:
        state="taken"
#........................................................................................................................................................................................
#................................................................................................................................................................................    
def lgn():
    global q1
    global we1
    global we2
    import mysql.connector as x
    global tab1
    global tab2
    global tab3
    global yu
    global uy
    c=x.connect(host="localhost",user="root",password="g46902105k",database="girish")
    k=c.cursor()
    k.execute("select Name,password from customdet;")
    g=k.fetchall()
    s={}
    for i in g:
        s[i[0]]=i[1]
    we1=t1.get()
    we2=t2.get()
    t1.delete(0,END)
    t2.delete(0,END)
    for j in s:
        if j==we1 and s[we1]==we2:
            obp()
            tab1=we1+"ss"
            tab2=we1+"cc"
            tab3=we1+"ll"
            conj()
            break
    else:
        messagebox.showerror("re-enter","Username or Password is inncorrect")   
            
#...............................................................................................................................................................................
#LOGIN PAGE
def log():
    root.withdraw()
    global img2
    global d
    global t1
    global t2
    global we1
    global we2
    tf=font.Font(size=30)
    d=Toplevel(bg="black")
    d.geometry("2500x2500+0+0")
    d.title("LOGIN PAGE")
    d.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img2=ImageTk.PhotoImage(Image.open("loginp.jpg"))
    pimg2=Label(d,image=img2).pack()
    lbl1=Label(d,text="Username",font=myfont,relief="raised")
    lbl2=Label(d,text="Password",font=myfont,relief="raised")
    t1=Entry(d,borderwidth=6,font=myfont)
    t2=Entry(d,borderwidth=6,show="*",font=myfont)
    lbl1.place(x=450,y=350)
    lbl2.place(x=450,y=450)
    t1.place(x=700,y=350)
    t2.place(x=700,y=450)
    tu=Button(d,text="login",font=myfont,command=lgn).place(x=450,y=550)
    bb=Button(d,text="<<",font=myfont,command=ww).place(x=20,y=20)
#.................................................................................................... ........................... ........................... ...........................
#LOGIN
b1=Button(root,text="LOGIN",command=log,font=myfont2,bg="cyan2",fg="purple1",width=20).place(x=550,y=300)
#.........................................................................................................................................
def gv():
    global cp
    global z11
    global z12
    global z13
    global tab1
    global tab2
    global tab3
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    import mysql.connector as x
    utd=datetime.date.today()
    c=x.connect(host="localhost",user="root",password="g46902105k",database="girish")
    k=c.cursor()
    k.execute("select Name,password from customdet;")
    v=k.fetchall()
    u={}
    for i in v:
        u[i[0]]=i[1]
    q1=e1.get()
    for dq in u:
        if dq==q1:
            messagebox.showinfo("ERROR","Username typed aldready exists(it is unavailable-type another username to proceed)")
            e1.delete(0,END)
            break
    else:
        qz="paid"
        gy="free"
        gyw=gy.strip("")
        qzw=qz.strip("")
        cp.withdraw()
        log()
        q2=e2.get()
        q3=e3.get()
        q4=e4.get()
        q5=e5.get()
        q6=e6.get()
        q7=e7.get()
        messagebox.showinfo("Account sucesfully created",dsss + " -Please note down CUSTOMERID for future reference ")
        z11=q1+"ss"
        z12=q1+"cc"
        z13=q1+"ll"
        tab1=z11.strip("")
        tab2=z12.strip("")
        tab3=z13.strip("")
        k.execute("insert into customdet values(%s,%s,%s,%s,%s,%s,%s);",(q1,q2,q3,q4,q5,q6,q7))
        k.execute("create table %s(sno int,customer_id varchar(50),debit float,credit float,interest_percent float,balance float,date date);"%(tab1,))
        k.execute("insert into %s"%(tab1,)+" values(1,%s,0,0,3,10000,%s);",(dsss,utdu))
        k.execute("create table %s(sno int,customer_id varchar(50),cc_amount float,process varchar(50),date date);"%(tab2,))
        k.execute("insert into %s"%(tab2,)+" values(1,%s,0,%s,%s);",(dsss,qzw,utd))
        k.execute("create table %s(sno int,customer_id varchar(50),loan_left float,date date,state varchar(50),years int);"%(tab3,))
        k.execute("insert into %s"%(tab3,)+" values(1,%s,0,%s,%s,0);",(dsss,utd,gyw))
        c.commit()
    
    
   
    
#........................................................CREATE FUNCTION.................................................... .................................................................................

def cret():
    root.withdraw()
    global img3
    global cp
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    tff=font.Font(size=30)
    cp=Toplevel(bg="black")
    cp.geometry("2250x2250+0+0")
    cp.title("CREATE ACCOUNT PAGE")
    cp.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img3=ImageTk.PhotoImage(Image.open("piggy.jpg"))
    pimg3=Label(cp,image=img3).pack()
    lb1=Label(cp,text="username",font=myfont,relief="raised").place(x=450,y=150)
    lb2=Label(cp,text="Age",font=myfont,relief="raised").place(x=450,y=230)
    lb3=Label(cp,text="Gender",font=myfont,relief="raised").place(x=450,y=310)
    lb4=Label(cp,text="Date of Birth(yyyy-mm-dd format)",font=myfont,relief="raised").place(x=50,y=390)
    lb5=Label(cp,text="email",font=myfont,relief="raised").place(x=450,y=470)
    lb6=Label(cp,text="password",font=myfont,relief="raised").place(x=450,y=550)
    lb7=Label(cp,text="Customer_ID",font=myfont,relief="raised").place(x=450,y=630)
    e1=Entry(cp,selectborderwidth=6,font=myfont)
    e2=Entry(cp,selectborderwidth=6,font=myfont)
    e3=Entry(cp,selectborderwidth=6,font=myfont)
    e4=Entry(cp,selectborderwidth=6,font=myfont)
    e5=Entry(cp,selectborderwidth=6,font=myfont)
    e6=Entry(cp,selectborderwidth=6,font=myfont)
    e7=Entry(cp,selectborderwidth=6,font=myfont)
    e7.insert(0,dsss)
    bc=Button(cp,text="<<",font=myfont,command=www)
    tu=Button(cp,text="create",font=myfont,command=gv)
    e1.place(x=700,y=150)
    e2.place(x=700,y=230)
    e3.place(x=700,y=310)
    e4.place(x=700,y=390)
    e5.place(x=700,y=470)
    e6.place(x=700,y=550)
    e7.place(x=700,y=630)
    tu.place(x=450,y=710)
    bc.place(x=20,y=20)
#........................................................................................................................................................................................
#CREATE
b2=Button(root,text="CREATE ACCOUNT",command=cret,font=myfont2,bg="cyan2",fg="purple1").place(x=575,y=480)

#................................................................................................................................................



#..................................................................................................................................................................................    
#.............................REGISTER SHOW FUNCTION....................................................................................................................................
import tkinter as tk
from tkinter import ttk
import mysql.connector as x
c=x.connect(host="localhost",user="root",password="g46902105k",database="girish")
k=c.cursor()

def show():
    global we1
    k.execute("select * from customdet where Name=%s;",(we1,))
    uu=k.fetchall()
    eu= Toplevel(bg="black")
    eu.geometry("525x50")
    eu.title("ACCOUNT DETAILS")
    eu.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico') 
    i=1
    i1= Label(eu, width=10,text="Name",fg='black',relief="raised")
    i2= Label(eu, width=10,text="Age", fg='black',relief="raised")
    i3= Label(eu, width=10,text="Gender" ,fg='black',relief="raised")
    i4= Label(eu, width=10,text="DOB" ,fg='black',relief="raised")
    i5= Label(eu, width=10,text="Email" ,fg='black',relief="raised")
    i6= Label(eu, width=10,text="Password" ,fg='black',relief="raised")
    i7= Label(eu, width=10,text="CustomerID" ,fg='black',relief="raised")
    i1.grid(row=0,column=1)
    i2.grid(row=0,column=2)
    i3.grid(row=0,column=3)
    i4.grid(row=0,column=4)
    i5.grid(row=0,column=5)
    i6.grid(row=0,column=6)
    i7.grid(row=0,column=7)
    for cu in uu: 
        for j in range(len(cu)):
            e = Entry(eu, width=12, fg='black') 
            e.grid(row=i, column=j+1) 
            e.insert(END, cu[j])
        i=i+1

#...............................................................................................................................................


def show1():
    global we1
    global tab1
    global tab2
    global tab3
    import tkinter  as tk
    tab1=we1+"ss"
    tab2=we1+"cc"
    tab3=we1+"ll"

    k.execute("select * from %s"%(tab1,))
    eu1= Toplevel(bg="black")
    eu1.geometry("475x1000")
    eu1.title("SAVINGS ACCOUNT CUSTOMER REGISTER")
    eu1.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    i=1
    i1= Label(eu1, width=8,text="Sno.",fg='black',relief="raised")
    i2= Label(eu1, width=8,text="CustomerID", fg='black',relief="raised")
    i3= Label(eu1, width=8,text="Debit" ,fg='black',relief="raised")
    i4= Label(eu1, width=8,text="Credit" ,fg='black',relief="raised")
    i5= Label(eu1, width=8,text="Interest" ,fg='black',relief="raised")
    i6= Label(eu1, width=8,text="Balance" ,fg='black',relief="raised")
    i7= Label(eu1, width=8,text="Date" ,fg='black',relief="raised")
    i1.grid(row=0,column=1)
    i2.grid(row=0,column=2)
    i3.grid(row=0,column=3)
    i4.grid(row=0,column=4)
    i5.grid(row=0,column=5)
    i6.grid(row=0,column=6)
    i7.grid(row=0,column=7)
    for cu1 in k: 
        for j in range(len(cu1)):
            e = Entry(eu1, width=10, fg='black') 
            e.grid(row=i, column=j+1) 
            e.insert(END, cu1[j])
        i=i+1

#...............................................................................................................................................
def show2():
    global we1
    global tab1
    global tab2
    global tab3
    
    tab1=we1+"ss"
    tab2=we1+"cc"
    tab3=we1+"ll"
    k.execute("select * from %s"%(tab2,))
    eu2= Toplevel(bg="black")
    eu2.geometry("315x1000")
    eu2.title("CREDIT CARD ACCOUNT CUSTOMER REGISTER")
    eu2.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    i=1
    i1= Label(eu2, width=8,text="Sno.",fg='black',relief="raised")
    i2= Label(eu2, width=8,text="CustomerID", fg='black',relief="raised")
    i3= Label(eu2, width=8,text="CCAmount" ,fg='black',relief="raised")
    i4= Label(eu2, width=8,text="Process" ,fg='black',relief="raised")
    i5= Label(eu2, width=8,text="Date" ,fg='black',relief="raised")
    i1.grid(row=0,column=1)
    i2.grid(row=0,column=2)
    i3.grid(row=0,column=3)
    i4.grid(row=0,column=4)
    i5.grid(row=0,column=5)
    for cu2 in k: 
        for j in range(len(cu2)):
            e = Entry(eu2, width=10, fg='black') 
            e.grid(row=i, column=j+1) 
            e.insert(END, cu2[j])
        i=i+1
    

#...............................................................................................................................................
def show3():
    global we1
    global tab1
    global tab2
    global tab3
    
    tab1=we1+"ss"
    tab2=we1+"cc"
    tab3=we1+"ll"

    k.execute("select * from %s"%(tab3,))
    eu3= Toplevel(bg="black")
    eu3.geometry("400x1000")
    eu3.title("LOAN ACCOUNT CUSTOMER REGISTER")
    eu3.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    i=1
    i1= Label(eu3, width=8,text="Sno.",fg='black',relief="raised")
    i2= Label(eu3, width=8,text="CustomerID", fg='black',relief="raised")
    i3= Label(eu3, width=8,text="Loan" ,fg='black',relief="raised")
    i4= Label(eu3, width=8,text="Date" ,fg='black',relief="raised")
    i5= Label(eu3, width=8,text="State" ,fg='black',relief="raised")
    i6= Label(eu3, width=8,text="NoOfYears" ,fg='black',relief="raised")
    i1.grid(row=0,column=1)
    i2.grid(row=0,column=2)
    i3.grid(row=0,column=3)
    i4.grid(row=0,column=4)
    i5.grid(row=0,column=5)
    i6.grid(row=0,column=6)
    for cu3 in k: 
        for j in range(len(cu3)):
            e = Entry(eu3, width=10, fg='black') 
            e.grid(row=i, column=j+1) 
            e.insert(END, cu3[j])
        i=i+1
#..........................................................................................................................................................................................
#AFTER LOGIN -------- THE BANK PAGE FUNCTION................................................................................................................................................

def obp():
    global img4
    global bp
    global we1
    
    po="welcome "+ we1
    bp=Toplevel(bg="black")
    d.withdraw()
    bp.geometry("2250x2250+0+0")
    bp.title("BANK")
    bp.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img4=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg4=Label(bp,image=img4).pack()
    nb1=Label(bp,text=po,font=myfont,relief="raised").place(x=550,y=5)
    nb2=Label(bp,text="ACCESS MENU",font=myfont,relief="raised").place(x=595,y=150)
    nb3=Label(bp,text="SAVINGS",font=myfont,relief="raised").place(x=20,y=300)
    nb3=Label(bp,text="CREDIT",font=myfont,relief="raised").place(x=650,y=300)
    nb3=Label(bp,text="LOAN",font=myfont,relief="raised").place(x=1350,y=300)
    bbp=Button(bp,text="<<",font=myfont,command=ew,relief="raised").place(x=20,y=20)
    sv=Button(bp,text="GO(SV)",font=myfont,command=savp).place(x=20,y=400)
    cc=Button(bp,text="GO(CC)",font=myfont,command=ccp).place(x=650,y=400)
    ln=Button(bp,text="GO(LN)",font=myfont,command=lnp).place(x=1350,y=400)
    ad=Button(bp,text="Account Details",font=myfont,command=show).place(x=595,y=700)
    
#....................................EACH PAGE FROM BANKPAGE.............................................................................................................................
#SAVINGS PAGE
def savp():
    global img5
    global sv
    conj()
    sv=Toplevel(bg="black")
    bp.withdraw()
    sv.geometry("2250x2250+0+0")
    sv.title("SAVINGS ACCOUNT")
    sv.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img5=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg5=Label(sv,image=img5).pack()
    nb1=Label(sv,text="SAVINGS ACCOUNT",font=myfont,relief="raised").place(x=550,y=5)
    nb2=Label(sv,text="ACCESS MENU",font=myfont,relief="raised").place(x=595,y=150)
    nb3=Button(sv,text="DEPOSIT",font=myfont,command=depo).place(x=20,y=300)
    nb3=Button(sv,text="ACCOUNT REGISTER",font=myfont,command=show1).place(x=525,y=300)
    nb3=Button(sv,text="WITHDRAW",font=myfont,command=witt).place(x=1150,y=300)
    bbv=Button(sv,text="<<",font=myfont,command=eww).place(x=20,y=20)
    ty()
#..................................................................................................................
#CREDIT CARDS PAGE
def ccp():
    global img6
    global ccp
    global listBox
    global estate
    conj()
    ccp=Toplevel(bg="black")
    bp.withdraw()
    ccp.geometry("2250x2250+0+0")
    ccp.title("CREDIT CARD")
    ccp.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img6=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg6=Label(ccp,image=img6).pack()
    nb0=Label(ccp,text="Credit Card Amount must be  paid back in full and grace period is 30 days(interest if taken is 3% monthly)",font=myfont1,relief="raised").place(x=10,y=95)
    nb1=Label(ccp,text="CREDIT CARD",font=myfont,relief="raised").place(x=590,y=5)
    nb2=Label(ccp,text="ACCESS MENU",font=myfont,relief="raised").place(x=595,y=150)
    nb3=Button(ccp,text="REPAY",font=myfont,command=repay)
    nb3.place(x=20,y=300)
    nb4=Button(ccp,text="ACCOUNT REGISTER",font=myfont,command=show2).place(x=525,y=300)
    nb5=Button(ccp,text="WITHDRAW",font=myfont,command=ccw)
    nb5.place(x=1150,y=300)
    bbv=Button(ccp,text="<<",font=myfont,command=lcp).place(x=20,y=20)
    if estate=="paid":
        nb3.place_forget()
#..................................................................................................................
#LOANS PAGE
def lnp():
    global img7
    global llp
    global listBox
    global llp
    global state
    conj()
    llp=Toplevel(bg="black")
    bp.withdraw()
    llp.geometry("2250x2250+0+0")
    llp.title("LOAN ACCOUNT")
    llp.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img7=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg7=Label(llp,image=img7).pack()
    nb0=Label(llp,text="Loan is offered for time period of 1 year with 12 % interest",font=myfont,relief="raised").place(x=50,y=95)
    nb1=Label(llp,text="LOAN",font=myfont,relief="raised").place(x=700,y=5)
    nb2=Label(llp,text="ACCESS MENU",font=myfont,relief="raised").place(x=595,y=150)
    nb3=Button(llp,text="TAKE LOAN",font=myfont,command=borrow)
    nb3.place(x=20,y=300)
    nb4=Button(llp,text="ACCOUNT REGISTER",font=myfont,command=show3).place(x=525,y=300)
    nb5=Button(llp,text="PAYBACK",font=myfont,command=register)
    nb5.place(x=1150,y=300)
    bbv=Button(llp,text="<<",font=myfont,command=lp).place(x=20,y=20)
    if state=="taken":
        nb3.place_forget()
    else:
        nb5.place_forget()
        
#...................................................................................WINDOWS ARE ABOVE...................................................................................... 
#................................................................................WORKING OF EACH ACCOUNT............................................................................................

#................SAVINGS ACCOUNT...........................................................................................................................................................................

global tab1
global tab2
global tab3
global dss
import mysql.connector as x
c=x.connect(host="localhost",user="root",password="g46902105k",database="girish")
k=c.cursor()
import datetime
def ty():
    global onsn
    global an
    global ao
    global ai
    global ti
    global tr
    global nsno
    global na
    global oa
    global ia
    global tab1
    global tab2
    global tab3
    global ua
    global day
    global nj
    global toi
    global sabl
    global dss
    conj()
    ia=int(sabl)*0.00008219
    nj=datetime.date.today()
    dek=nj-toi
    asw=dek.days
    ua=int(sabl) +ia
    if int(asw)!=0:
        k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,0,0,3,%s,%s);",(dss,ua,nj))
        c.commit()
    return
#....................................................................................................................................    
def hgj():
    global onsn
    global an
    global ao
    global ai
    global ti
    global tr
    global nsno
    global na
    global oa
    global ia
    global ua
    global tab1
    global tab2
    global tab3
    global day
    global nj
    global dss
    conj()
    tr=po1.get()
    na=int(sabl)+int(tr)
    k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,%s,0,3,%s,%s);",(dss,tr,na,nj))
    messagebox.showinfo("Transaction","Amount succesfully deposited")
    c.commit()
#......................................................................................................................................
    
def depo():
    global tr
    global nsno
    global na
    global oa
    global ia
    global nj
    global po1
    global ua
    global tab1
    global tab2
    global tab3
    global img8
    global dep
    global dss
    dep=Toplevel(bg="black")
    sv.withdraw()
    dep.geometry("2250x2250+0+0")
    dep.title("DEPOSIT")
    dep.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img8=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg8=Label(dep,image=img8).pack()
    qo1=Label(dep,text="Enter deposit Amount",font=myfont,relief="raised").place(x=400,y=150)
    po1=Entry(dep,selectborderwidth=6,font=myfont)
    po1.place(x=950,y=150)
    nj=datetime.date.today()
    debb=Button(dep,text="DEPOSIT",font=myfont,command=hgj).place(x=700,y=250)
    bbv=Button(dep,text="<<",font=myfont,command=uu).place(x=20,y=20)

#.......................................................................................................................................
def hjg():
    global tr
    global nsno
    global na
    global oa
    global ia
    global rh
    global onsn
    global an
    global ao
    global ai
    global ti
    global ua
    global tab1
    global tab2
    global tab3
    global pq1
    global osno
    global nj
    global dss
    conj()
    rh=pq1.get()
    an=int(sabl)-int(rh)
    k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,0,%s,3,%s,%s);",(dss,rh,an,nj))
    messagebox.showinfo("Transaction","Amount succesfully withdrawn")
    c.commit()

#......................................................................................................................................    
def witt():
    global tr
    global nsno
    global na
    global oa
    global ia
    global nj
    global pq1
    global ua
    global onsn
    global an
    global ao
    global ai
    global ti
    global tab1
    global tab2
    global tab3
    global img54
    global wtd
    global dss
    wtd=Toplevel(bg="black")
    sv.withdraw()
    wtd.geometry("2250x2250+0+0")
    wtd.title("WITHDRAW")
    wtd.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img54=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg54=Label(wtd,image=img54).pack()
    qo1=Label(wtd,text="Enter withdraw Amount",font=myfont,relief="raised").place(x=400,y=150)
    pq1=Entry(wtd,selectborderwidth=6,font=myfont)
    pq1.place(x=950,y=150)
    nj=datetime.date.today()
    debb=Button(wtd,text="Withdraw",font=myfont,command=hjg).place(x=700,y=250)
    bbv=Button(wtd,text="<<",font=myfont,command=ur).place(x=20,y=20)


#CREDIT CARD................................................................................................................................................................................
global tab1
global tab2
global tab3
global estate
global te1
global dss
import datetime
import mysql.connector as x
c=x.connect(host="localhost",user="root",password="g46902105k",database="girish")
k=c.cursor()

def ccb():
    vf="taken"
    vff="taken".strip()
    global tab1
    global tab2
    global tab3
    global estate
    global te1
    global po1
    global xoy
    global nj
    global we1
    global sabl
    global dss
    conj()
    nj=datetime.date.today()
    te1=po1.get()
    iza=int(cca)+int(te1)
    izaa=int(sabl)+int(te1)
    if int(te1)>15000 or iza>15000:
        messagebox.showinfo("Transaction","Exceeding withdraw amount limit")
    else:
        if estate=="paid":
            k.execute("insert into %s"%(tab2,)+" values(%s,%s,%s,%s,%s);",(xoy,dss,te1,vff,nj))
            c.commit()
            messagebox.showinfo("Transaction","Amount taken succesfully")
            k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,%s,0,3,%s,%s);",(dss,te1,izaa,nj))
            c.commit()
        else:
            k.execute("update %s set cc_amount=cc_amount+%s"%(tab2,te1)+" order by sno desc limit 1;")
            messagebox.showinfo("Transaction"," Additional Amount taken succesfully")
            c.commit()
            k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,%s,0,3,%s,%s);",(dss,te1,izaa,nj))
            c.commit()

#......................................................................................................................................     
def ccw():
    global tab1
    global tab2
    global tab3
    global po1
    global estate
    global tab1
    global tab2
    global tab3
    global re
    global img12
    global dss
    re=Toplevel(bg="black")
    re.geometry("2250x2250+0+0")
    re.title("Withdraw")
    re.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img12=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg12=Label(re,image=img12).pack()
    qq1=Label(re,text="Enter withdraw Amount",font=myfont,relief="raised").place(x=500,y=150)
    po1=Entry(re,selectborderwidth=6,font=myfont)
    po1.place(x=950,y=150)
    nj=datetime.date.today()
    debb=Button(re,text="Withdraw",font=myfont,command=ccb).place(x=500,y=250)
    bbv=Button(re,text="<<",font=myfont,command=ut).place(x=20,y=20)
    c.commit()
    return
#...................................................................................................................................... 
def repay():
    xq="paid"
    xqq=xq.strip("")
    global tab1
    global tab2
    global tab3
    global estate
    global ccaa
    global cca
    global we1
    global xoy
    global sabl
    global nsno
    global klg
    global odz
    global dss
    conj()
    iqw=int(sabl)-int(cca)
    iqww=int(sabl)-int(ccaa)
    pl=datetime.date.today()
    dui=pl-odz
    klg=dui.days
    zaq=messagebox.askquestion("Confirmation","Would you like to repay ?")
    if zaq=="yes":
        if klg>30:
            if iqww<=0:
                messagebox.askquestion("Failed to process","Not enough balance in savings")
            else:
                k.execute("insert into %s"%(tab2)+ " values(%s,%s,0,%s,%s);",(xoy,dss,xqq,pl))
                c.commit()
                k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,%s,0,3,%s,%s);",(dss,ccaa,iqww,pl))
                c.commit()
                messagebox.showinfo("Transaction","Amount succesfully repayed(with interest)")
        elif klg<30:
            if iqw<=0:
                messagebox.askquestion("Failed to process","Not enough balance in savings")
            else:
                k.execute("insert into %s"%(tab2)+ " values(%s,%s,0,%s,%s);",(xoy,dss,xqq,pl))
                c.commit()
                k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,0,%s,3,%s,%s);",(dss,cca,iqw,pl))
                c.commit()
                messagebox.showinfo("Transaction","Amount succesfully repayed")
                
#LOAN........................................................................................................................................................................................
global tab1
global tab2
global tab3
import mysql.connector as x
global dss
c=x.connect(host="localhost", user="root", password="g46902105k", database="girish")
k=c.cursor()
from datetime import date
global loan_taken

#BORROW BUTTON FUNCTION....................................................................
 
def bff():
    global tab1
    global tab2
    global tab3
    global apd
    global interest
    global ro1
    global wo1
    global date_borrowed
    global loan_taken
    global taz
    global yers
    global nsno
    global taz
    global wo2
    global state
    global taa
    global dss
    conj()
    ran="taken"
    ranst=ran.strip("")
    loan_taken=wo1.get()
    yers=wo2.get()
    rqw=int(loan_taken)+int(sabl)
    date_borrowed=date.today()
    interest =int(loan_taken)*((1.12)**int(yers)-1)
    taa=int(loan_taken)+interest
    k.execute("insert into %s"%(tab3,)+" values(%s,"%(taz,)+"%s,%s,%s,%s,%s);",(dss,taa,date_borrowed,ranst,yers))
    c.commit()
    k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,%s,0,3,%s,%s);",(dss,loan_taken,rqw,date_borrowed))
    messagebox.showinfo("process","LOAN SUCCESFULLY BORROWED")
    c.commit()
    #add borrow limits

#BORROW....................................................................................................................................................................................
def borrow():
    global apd
    global interest
    global ro1
    global wo1
    global tab1
    global tab2
    global tab3
    global img9
    global state
    global date_borrowed
    global loan_taken
    global bor
    global wo2
    global dss
    bor=Toplevel(bg="black")
    bor.geometry("2250x2250+0+0")
    bor.title("BORROW")
    bor.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img9=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg9=Label(bor,image=img9).pack()
    ro1=Label(bor,text="Enter borrow Amount",font=myfont,relief="raised").place(x=550,y=150)
    ro2=Label(bor,text="Enter number of years",font=myfont,relief="raised").place(x=550,y=350)
    wo1=Entry(bor,borderwidth=6,font=myfont)
    wo2=Entry(bor,borderwidth=6,font=myfont)
    wo1.place(x=950,y=150)
    wo2.place(x=950,y=350)
    bt=Button(bor,text="Withdraw",font=myfont,command=bff).place(x=700,y=550)
    bbv=Button(bor,text="<<",font=myfont,command=uw).place(x=20,y=20)
    date_borrowed=date.today()
#......................................................................................................................................
#today's installment
def paie():
    kl="free"
    kl1=kl.strip("")
    lk="taken"
    lk1=lk.strip("")
    global ro1
    global wo1
    global apd
    global interest
    global tab1
    global tab2
    global tab3
    global state
    global date_borrowed
    global loan_taken
    global ao1
    global dpb
    global yers
    global nsno
    global sabl
    global sate
    global taz
    global ytaz
    global taa
    global ytaz
    global dss
    conj()
    kzs=ao1.get()
    dp=date.today()
    atbp=int(dpb)-int(kzs)
    exz=int(sabl)-int(kzs)
    exzz=int(sabl)-int(dpb)
    if atbp==0 or atbp<0:
        if exzz<=0:
            messagebox.showinfo("Failed to process","Not enough balance in savings")
        else:
            k.execute("insert into %s"%(tab3,)+" values(%s,"%(taz,)+"%s,0,%s,%s,%s);",(dss,dp,kl1,ytaz))
            c.commit()
            k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,0,%s,3,%s,%s);",(dss,kzs,exzz,dp))
            c.commit()
            messagebox.showinfo("Transaction","Your Loan has been repayed)")
    else:
        if exz<=0:
             messagebox.showinfo("Failed to process","Not enough balance in savings")
        else:
            k.execute("insert into %s"%(tab3,)+" values(%s,"%(taz,)+"%s,%s,%s,%s,%s);",(dss,atbp,dp,lk1,ytaz))
            c.commit()
            k.execute("insert into %s"%(tab1,)+" values(%s,"%(nsno,)+"%s,0,%s,3,%s,%s);",(dss,kzs,exz,dp))
            c.commit()
#......................................................................................................................................    
def register():
    global ro1
    global wo1
    global apd
    global interest
    global tab1
    global tab2
    global tab3
    global img10
    global state
    global date_borrowed
    global loan_taken
    global ror
    global ao1
    global dss
    ror=Toplevel(bg="black")
    ror.geometry("2250x2250+0+0")
    ror.title("Payback")
    ror.iconbitmap('C:/Users/giris/OneDrive/Desktop/G files/gg/CS PROJECT/bank icon.ico')
    img10=ImageTk.PhotoImage(Image.open("mney.jpg"))
    pimg10=Label(ror,image=img10).pack()
    uo1=Label(ror,text="Amount",font=myfont,relief="raised").place(x=550,y=150)
    ao1=Entry(ror,borderwidth=6,font=myfont)
    ao1.place(x=700,y=150)
    bts=Button(ror,text="Pay",font=myfont,command=paie).place(x=550,y=250)
    bbv=Button(ror,text="<<",font=myfont,command=uq).place(x=20,y=20)
    date_borrowed=date.today()

exb=Button(root,text="Exit",command=coexit,font=myfont2,fg="white",bg="red").place(x=720,y=700)
root.mainloop()
#..................................................................... THE END.................................................................................
