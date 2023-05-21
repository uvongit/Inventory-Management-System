#-------------------IMPORT SECTION--------------------------
import MenuScreen as msn
import Upack as u
from sys import *
from tkinter import*
from PIL import ImageTk, Image
import mysql.connector
#-------------------FUNCTION SECTION-------------------------
def mainscreen():
    def dbmanagement():
        Window.destroy()
        u.create_database()
    def login():
        if e1.get()=="root" and e2.get()=="1234":
            Window.destroy()
            msn.mainscrn()
            exit()
        mydb = mysql.connector.connect(host="localhost", user="root",\
                                password=u.password, database="stock")
        mycursor= mydb.cursor()
        sql = "SELECT uid,upwd from user"
        mycursor.execute(sql) 
        d=mycursor.fetchall()
        for a in d:
            if a[0]==e1.get() and a[1]==e2.get():
                Window.destroy()
                msn.mainscrn()
                exit()
        else:
            Window.destroy()
            u.message("Access Denied","INVALID DETAILS")    
        exit()    
    #---------------------Main Window--------------------

    Window = Tk()
    Window.title('Welcome to Inventory Manager')
    Window.geometry('1025x684+0+0')
    Window.config()

    #---------------------Importing Images------------------

    b = ImageTk.PhotoImage(Image.open("Images\background0.jpg"))
    Button1 = ImageTk.PhotoImage(Image.open("Images\Button0.jpg"))
    Button2 = ImageTk.PhotoImage(Image.open("Images\Button05.jpg"))
    label1 = ImageTk.PhotoImage(Image.open("Images\label77.jpg"))
    label2 = ImageTk.PhotoImage(Image.open("Images\label99.jpg"))
    
    #----------------------Window Labels----------------------------
    background = Label(Window, image=b)
    background.place(x=0, y=0)
    l1=Label(Window,image=label1).place(x=200,y=250)
    l2=Label(Window,image=label2).place(x=200,y=350)
    #------------------------Entries--------------------------------
    e1=ttk.Entry(Window, width=20,font=('calibre', 15, 'bold'))
    e1.place(x=520,y=265)
    e2=ttk.Entry(Window, width=20,font=('calibre', 15, 'bold'))
    e2.place(x=520,y=365)
    #----------------------Buttons-----------------------------------
    B1= Button(Window,bd=0,image=Button1,command=login)
    B1.place(x=350,y=420)
    B5= Button(Window,bd=0,image=Button2,command=dbmanagement)
    B5.place(x=350,y=580)
    Window.mainloop()
#*****************************************************************
                


