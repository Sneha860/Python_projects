 
from tkinter import *
import pymysql
from tkinter import messagebox
window=Tk()
window.geometry("1500x1500")
window .configure(bg="red")
window.title("STUDENT INFORMATION")
lb=Label(window,text="STUDENT INFORMATION MANAGEMENT SYSTEM",bg="white",font="bold",fg="blue")
lb.place(x=500,y=50)
lb1=Label(window,text="REGISTER NO",bg="light green",width=25)
lb1.place(x=200,y=150)
e1=Entry(window,width=80)
e1.place(x=450,y=150)
lb2=Label(window,text="NAME",bg="light green",width=25)
lb2.place(x=200,y=200)
e2=Entry(window,width=80)
e2.place(x=450,y=200)
lb3=Label(window,text="EMAIL ID",bg="light green",width=25)
lb3.place(x=200,y=250)
e3=Entry(window,width=80)
e3.place(x=450,y=250)
lb4=Label(window,text="PHONE NO",bg="light green",width=25)
lb4.place(x=200,y=300)
e4=Entry(window,width=80)
e4.place(x=450,y=300)
lb5=Label(window,text="GENDER",bg="light green",width=25)
lb5.place(x=200,y=350)
e5=Entry(window,width=80)
e5.place(x=450,y=350)
lb6=Label(window,text="ADDRESS",bg="light green",width=25)
lb6.place(x=200,y=400)
e6=Entry(window,width=80)
e6.place(x=450,y=400)
def insert_info():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    f=e6.get()
    dbc=pymysql.connect(host='localhost',user='root',password='',db='Student')
    g=dbc.cursor()
    try:
        sql="INSERT INTO info(RegNo,Name,Email,Phone,Gender,Address) VALUES (%s,%s,%s,%s,%s,%s)"
        val=(a,b,c,d,e,f)
        g.execute(sql,val)
        messagebox.showinfo("Information","Information is stored Successfully")
        dbc.commit()
    except Exception as e:
        print(e)
        dbc.rollback()
        dbc.close()
btn1=Button(window,text="INSERT",bg="blue",fg="white",font="bold",width=25,command=insert_info)
btn1.place(x=100,y=550)
def update_info():
    dbc=pymysql.connect(host='localhost',user='root',password='',db='Student')
    h=dbc.cursor()
    try:
        update_query="UPDATE info SET Name = 'Vishal' WHERE Name = 'Raghav'"
        h.execute(update_query)
        messagebox.showinfo("Information","Information is Updated Successfully")
        dbc.commit()
    except Exception as e:
        print(e)
        dbc.rollback()
        dbc.close()
btn2=Button(window,text="UPDATE",bg="blue",fg="white",font="bold",width=25,command=update_info)
btn2.place(x=500,y=550)
def delete_info():
    dbc=pymysql.connect(host='localhost',user='root',password='',db='Student')
    i=dbc.cursor()
    try:
        delete_query="DELETE FROM info WHERE RegNo = '2'"
        i.execute(delete_query)
        messagebox.showinfo("Information","Deleted Successfully")
        dbc.commit()
    except Exception as e:
        print(e)
        dbc.rollback()
        dbc.close()
btn3=Button(window,text="DELETE",bg="blue",fg="white",font="bold",width=25,command=delete_info)
btn3.place(x=900,y=550)
def select_info():
    dbc=pymysql.connect(host='localhost',user='root',password='',db='Student')
    j=dbc.cursor()
    try:
        select_query="SELECT * From info"
        j.execute(select_query)
        results = j.fetchall()
        for row in results:
            print(row)
        dbc.commit()
    except Exception as e:
        print(e)
        dbc.rollback()
        dbc.close()
btn4=Button(window,text="DISPLAY",bg="orange",fg="black",font="bold",width=25,command=select_info)
btn4.place(x=1050,y=200)
def close():
    window.destroy()
btn5=Button(window,text="EXIT",bg="orange",fg="black",font="bold",width=25,command=close)
btn5.place(x=1050,y=360)
window.mainloop()
