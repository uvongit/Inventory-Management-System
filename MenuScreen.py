#-------------------IMPORT SECTION--------------------------
from sys import *
from tkinter import*
from PIL import ImageTk, Image
import Upack as u
def mainscrn():
    def productmanagement():
        Window.destroy()
        u.product_mgmt()
    def purchasemanagement():
        Window.destroy()
        u.purchase_mgmt()
    def salesmanagement():
        Window.destroy()
        u.sales_mgmt()
    def usermanagement():
        Window.destroy()
        u.user_mgmt()
    def dbmanagement():
        Window.destroy()
        u.db_mgmt()
    def destroy():
        Window.destroy()
        exit()

    #---------------------Main Window--------------------

    Window = Tk()
    Window.title('Welcome to Inventory Manager')
    Window.geometry('1025x684+0+0')
    Window.config()

    #---------------------Importing Images------------------

    b = ImageTk.PhotoImage(Image.open("Images\background.jpg"))
    Button1 = ImageTk.PhotoImage(Image.open("Images\Button1.png"))
    Button2 = ImageTk.PhotoImage(Image.open("Images\Button2.jpg"))
    Button3 = ImageTk.PhotoImage(Image.open("Images\Button3.jpg"))
    Button4 = ImageTk.PhotoImage(Image.open("Images\Button4.jpg"))
    Button5 = ImageTk.PhotoImage(Image.open("Images\Button5.jpg"))
    Button6 = ImageTk.PhotoImage(Image.open("Images\Button6.png"))
    #----------------------Window Labels----------------------------
    background = Label(Window, image=b)
    background.place(x=0, y=0)

    #----------------------Buttons-----------------------------------
    B1= Button(Window,bd=0,image=Button1,command=productmanagement)
    B1.place(x=225,y=280)
    B2= Button(Window,bd=0,image=Button2,command=purchasemanagement)
    B2.place(x=555,y=280)
    B3= Button(Window,bd=0,image=Button3,command=salesmanagement)
    B3.place(x=225,y=380)
    B4= Button(Window,bd=0,image=Button4,command=usermanagement)
    B4.place(x=555,y=380)
    B5= Button(Window,bd=0,image=Button5,command=dbmanagement)
    B5.place(x=225,y=480)
    B6 = Button(Window,image=Button6,bd=0,command=destroy)
    B6.place(x=555, y=480)
    Window.mainloop()
#*****************************************************************


