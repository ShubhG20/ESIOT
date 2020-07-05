try:
    import Tkinter as tk
except:
    import tkinter as tk
    

import tkinter.messagebox
from pygame import mixer
import sqlite3
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
from datetime import date
import datetime
import dlib
import cv2
import os
import smtplib


uid=0
    
def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1. Shubhankar Gaikwad\n2. Shrut Shah \n3. Shruti Rawate \n4. Rasika Sonawane\n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Drowsiness Detection System version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
   

      
                                    
  
    
    
class SampleApp(tk.Tk):
    
    def __init__(self):
        
        #root.geometry('500x570')
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title("Driver Drowsiness Detection System")
        menu= tk.Menu(self)
        self.config(menu=menu)
        subm1= tk.Menu(menu)
        menu.add_cascade(label="Tools",menu=subm1)
        subm1.add_command(label="Open CV Docs",command=hel)
        subm2=tk.Menu(menu)
        menu.add_cascade(label="About",menu=subm2)
        subm2.add_command(label="DDDS",command=anotherWin)
        subm2.add_command(label="Contributors",command=Contri) 
        
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        #new_frame.config(self,relief="ridge",borderwidth=2)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=1)
        
            
      
     

class StartPage(tk.Frame):
   
    def __init__(self, master):
        
        def dbcheck():
   
                        password=Password.get()
                        uname=UserName.get()
                        conn = sqlite3.connect('Register.db')
                        global uid
                        cursor=conn.cursor()
                        cursor.execute('SELECT EXISTS(SELECT * FROM Users where UserName=? AND Password=?)',(uname,password))
                        row=cursor.fetchone()
                        #conn.commit()
                        if row[0]:
                            #row=cursor.fetchone()
                            uid=uname
                            
                            print("Welcome\n ID:"+ uid)
                            master.switch_frame(PageTwo)
                        else:
                            print("Login Failed")
                            tkinter.messagebox.showinfo("Login Error","Wrong username or password")
                                
                    
                    
                    
                    
                    
                    
                    
                    
        tk.Frame.__init__(self, master)
        filename= tk.PhotoImage(file="demo.png")
        
        
        tk.Frame.config(self, relief="ridge",borderwidth=2, background='light blue')
        
        
        tk.Label(self, text="DRIVER\n DROWSINESS\n DETECTION SYSTEM\n", font=('Times 35 bold'),background='light blue').pack(side="top")
        
        #filename= tk.PhotoImage(file="demo.png")
        l=tk.Label(self,image=filename)
        l.img=filename
       
        l.pack()
        UserName=tk.StringVar()
        Password=tk.StringVar()  
        
        label_1 = tk.Label(self, text="UserName",width=20,font=("bold", 10))
        label_1.place(x=80,y=280)
        entry_1 = tk.Entry(self,textvar=UserName)
        entry_1.place(x=240,y=280)
        label_2 = tk.Label(self, text="Password",width=20,font=("bold", 10))
        label_2.place(x=68,y=330)
        entry_2 = tk.Entry(self,textvar=Password, show="*")
        entry_2.place(x=240,y=330)
        
        tk.Button(self, text="Register",relief="groove",padx=5,pady=5,width=10,bg='white',fg='black',font=('helvetica 15 bold'),
                  command=lambda: master.switch_frame(PageOne)).place(x=100,y=400)
        tk.Button(self, text="Login",relief="groove", padx=5,pady=5,width=10,bg='white',fg='black',font=('helvetica 15 bold'),
                  command=dbcheck).place(x=300,y=400)
        #tk.Button(self, text="Login",relief="groove", padx=5,pady=5,width=10,bg='white',fg='black',font=('helvetica 15 bold'),
                  #command=lambda: master.switch_frame(PageTwo)).place(x=300,y=400)

class PageOne(tk.Frame):
   
           
    def __init__(self, master):
    
        def database():
                        name1=Fullname.get()
                        email=Email.get()
                        password=Password.get()
                        uname=UserName.get()
                        contact=Phone.get()
                        #country=c.get()
                        #prog=var1.get()
                        conn = sqlite3.connect('Register.db')
                        with conn:
                           cursor=conn.cursor()
                        cursor.execute('CREATE TABLE IF NOT EXISTS Users (Fullname TEXT,Email TEXT,UserName TEXT,Password TEXT,Contact TEXT)')
                        cursor.execute('INSERT INTO Users (FullName,Email,UserName,Password,Contact) VALUES(?,?,?,?,?)',(name1,email,uname,password,contact))
                        conn.commit()                  
          
        tk.Frame.__init__(self, master)
        
        filename=tk.PhotoImage(file="demo.png")
        
        var = tk.IntVar()
        c=tk.StringVar()
        var1= tk.IntVar()
        Fullname=tk.StringVar()
        Email=tk.StringVar()
        UserName=tk.StringVar()
        Phone=tk.IntVar()
        Password=tk.StringVar()  
        

                   
           
      
        tk.Frame.configure(self,bg='light blue')
        #tk.Label(self, text="User Registration", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        label_0 = tk.Label(self, text="Registration form",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)
        label_1 = tk.Label(self, text="FullName",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)
        entry_1 = tk.Entry(self,textvar=Fullname)
        entry_1.place(x=240,y=130)
        label_2 = tk.Label(self, text="UserName",width=20,font=("bold", 10))
        label_2.place(x=68,y=180)
        entry_2 = tk.Entry(self,textvar=UserName)
        entry_2.place(x=240,y=180)
        label_3 = tk.Label(self, text="Email",width=20,font=("bold", 10))
        label_3.place(x=70,y=230)
        entry_3= tk.Entry(self,textvar=Email)
        entry_3.place(x=240,y=230)
        label_4 = tk.Label(self, text="Phone",width=20,font=("bold", 10))
        label_4.place(x=70,y=280)
        entry_4=tk.Entry(self, textvar=Phone)
        entry_4.place(x=240,y=280)
        label_5 = tk.Label(self, text="Password",width=20,font=("bold", 10))
        label_5.place(x=70,y=330)
        entry_5=tk.Entry(self, textvar=Password,show="*")
        entry_5.place(x=240,y=330)
        
        
      
        tk.Button(self, text='Submit',width=20,bg='purple',fg='white',command=database).place(x=180,y=380)
        tk.Button(self, text="Go back to start page",bg='purple',fg='white',width='20',
                  command=lambda: master.switch_frame(StartPage)).place(x=180,y=430)
    
    

class PageTwo(tk.Frame):
    def __init__(self, master):
    
        def cam():
            print("Starting camera")
            print("UID:"+ uid)
            os.system('python3 drowsiness_yawn.py -uid '+uid+' -w 0')
            
            
        def report():
        
            print("Generating report")
            conn=sqlite3.connect('Register.db')
            c=conn.cursor()
            c.execute('SELECT DateTime FROM Analysis_Data WHERE AlertType=? AND UserId=?',('Drowsiness Alert',uid))
            
            res=c.fetchall();
            print(res)
            
            global drowsy;
            global yawn;
            drowsy=0;yawn=0;
          
            dvar=Date.get()
            
            
            #print(dvar)
            #print("..... ")
            
           
            
            for a in res:
                #global drowsy
                obj=datetime.datetime.strptime(a[0],'%Y-%m-%d %H:%M:%S')
                ovar=obj.date()
                #print('OVAR: '+str(ovar))
                #print('DVAR: '+dvar)
                #print(ovar==dvar)
                if str(ovar)==dvar :
                    drowsy+=1
                    #print(drowsy)
                else:
                    print("Fishy1")
                
            
            #drowsy=c.fetchall();
            #print(drowsy)
            
            c.execute('SELECT DateTime FROM Analysis_Data WHERE AlertType=? AND UserId=?',('Yawn Alert',uid))
            
            #yawn=c.fetchall();
            res2=c.fetchall();
            print(res2)
            
            for a in res2:
                
                #global yawn
                obj2=datetime.datetime.strptime(a[0],'%Y-%m-%d %H:%M:%S')
                ovar=obj2.date()
                #print('OVAR:'+str(ovar))
                #print('DVAR:'+dvar)
                if str(ovar)==dvar :
                    #print(yawn)
                    yawn+=1
                else:
                    print("Fishy2")
            
            tkinter.messagebox.showinfo("Analysis Report","Report:\n+UserId:"+uid+"\nDate:"+Date.get()+"\nDrowsiness Alerts Count:"+str(drowsy)+"\n Yawn Alerts Count:"+str(yawn))
            
            ms="Report:\n+UserId:"+uid+"\nDate:"+Date.get()+"\nDrowsiness Alerts Count:"+str(drowsy)+"\n Yawn Alerts Count:"+str(yawn)
            
            #mail to recipient
            print(type(uid))
            c.execute("SELECT Email FROM Users WHERE UserName='%s'" % uid);
            
            res3=c.fetchall();
            print(res3)
            
            
            rid=res3[0]
            s= smtplib.SMTP('smtp.gmail.com',587)
            sender="sih.codewarriors@gmail.com"
            to=rid
            subject="DDDS Report"
            headers="From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"% (sender,to,subject)
            message=headers+ms
            s.set_debuglevel(1)
            s.ehlo()
            
            s.starttls()
            s.ehlo()
            
            s.login("sih.codewarriors@gmail.com","sih2020cw")
            s.ehlo()
            
           
            print(message)
            print(rid)
            s.sendmail(sender,to,message)
            s.quit()
            
            
            
        
        
        
        tk.Frame.__init__(self, master)
        
        Date= tk.StringVar()
        tk.Frame.configure(self,bg='light pink')
        tk.Label(self, text="WELCOME TO DDDS", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        tk.Button(self, text='Start',height=5,width=30,bg='brown',fg='white',command=cam).place(x=130,y=100)
        
        
        label_5 = tk.Label(self, text="Enter Date(YYYY-MM-DD)",width=30,font=("bold", 10))
        label_5.place(x=130,y=250)
        entry_5=tk.Entry(self, width=30,textvar=Date)
    
        entry_5.place(x=130,y=275)
        tk.Button(self, text="View Report",bg='brown',fg='white',width=30,command=report).place(x=130,y=300)
        
        tk.Button(self, text="Go back to start page",width=30,
                  command=lambda: master.switch_frame(StartPage)).place(x=130,y=400)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
