from tkinter import *
from time import strftime
from datetime import date
def gettime():
    timenow = strftime('%H : %M : %S')
    digital_clock.configure(text= timenow)
    digital_clock.after(80,gettime)
def getdate():
    today = date.today()
    now = today.strftime("%B %d,%Y")
    d.configure(text=now)
    d.after(60000, getdate)

root= Tk()
root.title('DIGITAL CLOCK')
root.configure(bg='black')
root.geometry('300x200')
a= Label(root,text= 'Digital Clock' ,font='Times 11 bold',bg='black', fg='white', borderwidth= 10, relief= SUNKEN)
a.place(x=85,y=20)
digital_clock=Label(root,bg='black',fg='red',font= 'Times 20 bold')
digital_clock.place(x=75, y=80)
gettime()
d=Label(root,font='Times 11 italic',fg='white',bg='black')
d.place(x=95,y=130)
getdate()
root.mainloop()


