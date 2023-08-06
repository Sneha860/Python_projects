 
from tkinter import*
from gtts import gTTS
import os
window=Tk()
window.geometry("800x800")
window.configure(bg="blue")
window.title("Text Converter")
lb1=Label(text="TEXT TO SPEECH CONVERTER",font="bold,100",bg="red",fg="white")
lb1.place(x=290,y=30)
txt1=Text(window,width=82,height=25)
txt1.place(x=50,y=150)
def play():
    language1 = "en"
    output = gTTS(text=txt1.get("1.0","end-1c"),lang=language1,slow=False)
    output.save("output.mp3")
    os.system("output.mp3")
bt1=Button(window,text="CONVERT TO SPEECH",font="bold,20",fg="black",bg="yellow",width=25,command=play)
bt1.place(x=100,y=600)
def clear():
    txt1.delete("1.0","end")
bt2=Button(window,text="CLEAR",font="bold,20",fg="black",bg="yellow",width=25,command=clear)
bt2.place(x=500,y=600)
 
    
 
                 
 
