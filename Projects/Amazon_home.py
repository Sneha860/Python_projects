
 
from tkinter import *
 
from tkinter.ttk import*
 
import tkinter as tk
 
from PIL import ImageTk,Image
 
import pymysql
 
from tkinter import messagebox
 
window=Tk()
 
window.title('amazon.in')
 
window.geometry('1500x1500')
 
img1=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image.JPG"))
 
logo1=Label(window,text='',image=img1)
 
logo1.place(x=5,y=1)
 
img2=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image1.JPG"))
 
logo2=Label(window,text='',image=img2)
 
logo2.place(x=200,y=150)
 
n1=Label(window,text='Enter your mobile number')
 
n1.place(x=200,y=200)
 
e1=Entry(window,width=30)
 
e1.place(x=400,y=200)
 
img3=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image2.JPG"))
 
logo3=Label(window,text='',image=img3)
 
logo3.place(x=220,y=300)
 
img4=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image3.JPG"))
 
logo4=Label(window,text='',image=img4)
 
logo4.place(x=650,y=395)
 
img5=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image4.JPG"))
 
logo5=Label(window,text='',image=img5)
 
logo5.place(x=620,y=100)
 
def create_account():
 
    window=Tk()
 
    window.title('create new account')
 
    window.geometry('500x500')
 
    window.configure(bg="light green")
 
    n2=Label(window,text='Create Your Account',font="calibri,20")
 
    n2.place(x=150,y=25)
 
    name=Label(window,text='user name',font="calibri,10")
 
    name.place(x=150,y=70)
 
    e2=Entry(window,width=30)
 
    e2.place(x=150,y=100)
 
    mobile=Label(window,text='Mobile no',font="calibri,10")
 
    mobile.place(x=150,y=130)
 
    country_code=['+91','+65','+1','+44']
 
    combo=Combobox(window,value=country_code,width=3)
 
    combo.place(x=150,y=165)
 
    e3=Entry(window,width=22)
 
    e3.place(x=200,y=165)
 
    mail=Label(window,text='Email(optional)',font="calibri,10")
 
    mail.place(x=150,y=200)
 
    e4=Entry(window,width=30)
 
    e4.place(x=150,y=230)
 
    pswd=Label(window,text='password',font="calibri,10")
 
    pswd.place(x=150,y=265)
 
    e5=Entry(window,width=30)
 
    e5.place(x=150,y=300)
 
    def sign_up(): 
 
        n=e2.get()
 
        m=e3.get()
 
        e=e4.get()
 
        p=e5.get()
 
        dbc=pymysql.connect(host='localhost',user='root',password='',db='amazon1')
 
        c=dbc.cursor()
 
        try:
 
            sql="INSERT INTO login1(Name,mobileno,email,password) VALUES (%s,%s,%s,%s)"
 
            val=(n,m,e,p)
 
            c.execute(sql,val)
 
            messagebox.showinfo("Information","Your account is created successfully")
 
            window=tk.Toplevel()
 
            window.geometry('1500x1500')
 
            img7=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image5.JPG"))
 
            logo7=tk.Label(window,text='',image=img7)
 
            logo7.image=img7
 
            logo7.grid(row=0,column=0)
 
            dbc.commit()   
 
        except Exception as e:
 
            print(e)
 
            dbc.rollback()
 
            dbc.close()
 
    bt3=Button(window,text='signup',width=30,command=sign_up)
 
    bt3.place(x=150,y=400)
 
def login():
    mobilenumber=e1.get()
    dbc=pymysql.connect(host='localhost',user='root',password='',db='amazon1')
    d=dbc.cursor()
    try:
        sql1='SELECT * from login1 where mobileno=%s'
        d.execute(sql1,mobilenumber)
        result=d.fetchone()
        res=result[1]
        if res==mobilenumber:
            messagebox.showinfo("Information","login successfully")
            window=tk.Toplevel()
            window.geometry('1500x1500')
            img7=ImageTk.PhotoImage(Image.open("c:\\Users\\Sneha\\Desktop\\images\\image5.JPG"))
            logo7=tk.Label(window,text='',image=img7)
            logo7.image=img7
            logo7.grid(row=0,column=0)
            dbc.commit()
    except Exception as e:
        print(e)
        messagebox.showerror("Error","please enter the valid mobile number")
        dbc.rollback()
        dbc.close()
bt1=Button(window,text='continue',width=30,command=login)
bt1.place(x=400,y=250)
 
bt2=Button(window,text='create your Amazon account',width=30,command=create_account)
bt2.place(x=320,y=500)
window.mainloop()   
 
 
 
