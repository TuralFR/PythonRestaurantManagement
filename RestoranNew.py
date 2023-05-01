from tkinter import *
import tkinter.messagebox
import random
from datetime import datetime

root = Tk()
root.geometry("1600x800+0+0")
space = " "
root.title(190*space + "Restoran Hesap Yonetim")

coverFrame = Frame(root, bd=10, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame, bd=10, pady=2, bg='cadet blue', relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame(root, bd=5, pady=2, width=1350, height=700, relief=RIDGE)
MainFrame.grid()

Tops = Frame(MainFrame, width=1600, height=50, bg='cadet blue', bd=10, relief=SUNKEN)
Tops.grid(row=0, column=0)

Tops2 = Frame(MainFrame, width=1600, height=700, bg='cadet blue', bd=10, relief=SUNKEN)
Tops2.grid(row=1, column=0)

f1 = Frame(Tops2, width=900, height=600, bd=10, relief=SUNKEN)
f1.grid(row=0, column=0)

f1a = Frame(f1, width=900, height=600, bd=10, relief=SUNKEN)
f1a.grid(row=0, column=0)

f1b = Frame(f1, width=900, height=100, relief=SUNKEN)
f1b.grid(row=1, column=0)

lblTitle = Label(Tops, font=('arial',16, 'bold'), text="Restoran Hesap Yonetimi", fg='white', bg='cadet blue', bd=10)
lblTitle.grid(row=0, column=0, padx=270)

rand = StringVar()
Iskender = StringVar()
Manti = StringVar()
Burger = StringVar()
Fajita = StringVar()
Nachos = StringVar()
AraToplam = StringVar()
Toplam = StringVar()
Servis_Ucreti = StringVar()
Icecekler = StringVar()
Vergi = StringVar()
Hesap = StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

Iskender.set("0")
Manti.set("0")
Burger.set("0")
Fajita.set("0")
Nachos.set("0")

def Reset():
    Iskender.set("0")
    Manti.set("0")
    Burger.set("0")
    Fajita.set("0")
    Nachos.set("0")
    AraToplam.set("")
    Toplam.set("")
    Servis_Ucreti.set("")
    Vergi.set("")
    Hesap.set("")

    txtIskender.configure(state=DISABLED)
    txtManti.configure(state=DISABLED)
    txtBurger.configure(state=DISABLED)
    txtFajita.configure(state=DISABLED)
    txtNachos.configure(state=DISABLED)
    txtIcecekler.configure(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)

def iCikis():
    iCikis = tkinter.messagebox.askyesno("Restoran Hesap Yonetimi", "Cikis Yapmak mi Istiyorsunuz?")
    if iCikis>= 1:
        root.destroy()
        return


def ToplamHesap():
    x = random.randint(9023, 490857)
    randomRef = str(x)
    rand.set(randomRef)

    HeIskender = float(Iskender.get())
    HeManti = float(Manti.get())
    HeBurger = float(Burger.get())
    HeFajita = float(Fajita.get())
    HeNachos = float(Nachos.get())
    HeIcecekler = float(Icecekler.get())

    IskenderHesabi = HeIskender*50
    MantiHesabi = HeManti * 30
    BurgerHesabi = HeBurger * 35
    FajitaHesabi = HeFajita * 65
    NachosHesabi = HeNachos * 45
    IceceklerHesabi = HeIcecekler * 5

    YemekHesabi = str('₺%.2f' % (IskenderHesabi + MantiHesabi + BurgerHesabi + FajitaHesabi + NachosHesabi + IceceklerHesabi))
    VergiUcreti = ((IskenderHesabi + MantiHesabi + BurgerHesabi + FajitaHesabi + NachosHesabi + IceceklerHesabi) * 0.1)
    ServisUcreti = str('₺%.2f' % ((IskenderHesabi + MantiHesabi + BurgerHesabi + FajitaHesabi + NachosHesabi + IceceklerHesabi) / 99))
    AToplam = str('₺%.2f' % (IskenderHesabi + MantiHesabi + BurgerHesabi + FajitaHesabi + NachosHesabi + IceceklerHesabi))
    ToplamVeri = (IskenderHesabi + MantiHesabi + BurgerHesabi + FajitaHesabi + NachosHesabi + IceceklerHesabi)
    Servis_Ucreti.set(ServisUcreti)
    Hesap.set(YemekHesabi)
    AraToplam.set(AToplam)
    Vergi.set(str('₺%.2f' %(VergiUcreti)))
    ToplamHesap = str('₺%.2f' %(VergiUcreti + ToplamVeri))
    Toplam.set(ToplamHesap)

def hesapIskender():
    if(var1.get() == 1):
        txtIskender.configure(state=NORMAL)
        txtIskender.focus()
        txtIskender.delete('0', END)
        Iskender.set("")
    elif(var1.get() == 1):
        txtIskender.configure(state=DISABLED)
        Iskender.set("0")

def hesapManti():
    if(var2.get() == 1):
        txtManti.configure(state=NORMAL)
        txtManti.focus()
        txtManti.delete('0', END)
        Manti.set("")
    elif(var2.get() == 1):
        txtManti.configure(state=DISABLED)
        Manti.set("0")

def hesapBurger():
    if(var3.get() == 1):
        txtBurger.configure(state=NORMAL)
        txtBurger.focus()
        txtBurger.delete('0', END)
        Burger.set("")
    elif(var3.get() == 1):
        txtBurger.configure(state=DISABLED)
        Burger.set("0")

def hesapFajita():
    if(var4.get() == 1):
        txtFajita.configure(state=NORMAL)
        txtFajita.focus()
        txtFajita.delete('0', END)
        Fajita.set("")
    elif(var4.get() == 1):
        txtFajita.configure(state=DISABLED)
        Fajita.set("0")

def hesapNachos():
    if(var5.get() == 1):
        txtNachos.configure(state=NORMAL)
        txtNachos.focus()
        txtNachos.delete('0', END)
        Nachos.set("")
    elif(var5.get() == 1):
        txtNachos.configure(state=DISABLED)
        Nachos.set("0")

def hesapIcecekler():
    if(var6.get() == 1):
        txtIcecekler.configure(state=NORMAL)
        txtIcecekler.focus()
        txtIcecekler.delete('0', END)
        Icecekler.set("")
    elif(var6.get() == 1):
        txtIcecekler.configure(state=DISABLED)
        Icecekler.set("0")

lblRef = Label(f1a, font=('arial',16, 'bold'), text="Referans", fg='black', bd=10)
lblRef.grid(row=0, column=0, sticky=W)
txtReference = Entry(f1a, font=('arial',16, 'bold'), textvariable=rand, bd=10, justify='right', bg='cadet blue')
txtReference.grid(row=0, column=1)

chkIskender = Checkbutton(f1a, text="Iskender", variable=var1, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=hesapIskender ).grid(row=1, column=0, sticky=W)
txtIskender = Entry(f1a, font=('arial',16, 'bold'), textvariable=Iskender, bd=10, insertwidth=4, justify='right',
                    bg='cadet blue', state=DISABLED)
txtIskender.grid(row=1, column=1)

chkManti = Checkbutton(f1a, text="Manti", variable=var2, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=hesapManti).grid(row=2, column=0, sticky=W)
txtManti = Entry(f1a, font=('arial',16, 'bold'), textvariable=Manti, bd=10, insertwidth=4, justify='right',
                 bg='cadet blue', state=DISABLED)
txtManti.grid(row=2, column=1)

chkBurger = Checkbutton(f1a, text="Burger", variable=var3, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=hesapBurger).grid(row=3, column=0, sticky=W)
txtBurger = Entry(f1a, font=('arial',16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, justify='right',
                  bg='cadet blue', state=DISABLED)
txtBurger.grid(row=3, column=1)

chkFajita = Checkbutton(f1a, text="Fajita", variable=var4, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=hesapFajita).grid(row=4, column=0, sticky=W)
txtFajita = Entry(f1a, font=('arial',16, 'bold'), textvariable=Fajita, bd=10, insertwidth=4, justify='right',
                  bg='cadet blue', state=DISABLED)
txtFajita.grid(row=4, column=1)

chkNachos = Checkbutton(f1a, text="Nachos", variable=var5, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=hesapNachos).grid(row=5, column=0, sticky=W)
txtNachos = Entry(f1a, font=('arial',16, 'bold'), textvariable=Nachos, bd=10, insertwidth=4, justify='right',
                   bg='cadet blue', state=DISABLED)
txtNachos.grid(row=5, column=1)

chkIcecekler = Checkbutton(f1a, text="Icecekler", variable=var6, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=hesapIcecekler).grid(row=0, column=2, sticky=W, pady=5)
txtIcecekler = Entry(f1a, font=('arial',16, 'bold'), textvariable=Icecekler, bd=10, insertwidth=4, justify='right',
                     bg='cadet blue', state=DISABLED)
txtIcecekler.grid(row=0, column=3, pady=5)

lblHesap = Label(f1a, font=('arial',16, 'bold'), text="Yemek Ucreti", bd=2, anchor='w')
lblHesap.grid(row=1, column=2, sticky=W, pady=5)
txtHesap = Entry(f1a, font=('arial',16, 'bold'), textvariable=Hesap, bd=10, insertwidth=4, justify='right')
txtHesap.grid(row=1, column=3, pady=5)

lblServis = Label(f1a, font=('arial',16, 'bold'), text="ServisUcreti", bd=2, anchor='w')
lblServis.grid(row=2, column=2, sticky=W, pady=5)
txtServis = Entry(f1a, font=('arial',16, 'bold'), textvariable=Servis_Ucreti, bd=10, insertwidth=4, justify='right')
txtServis.grid(row=2, column=3, pady=5)

lblVergi = Label(f1a, font=('arial',16, 'bold'), text="Vergi Ucreti", bd=2, anchor='w')
lblVergi.grid(row=3, column=2, sticky=W, pady=5)
txtVergi = Entry(f1a, font=('arial',16, 'bold'), textvariable=Vergi, bd=10, insertwidth=4, justify='right')
txtVergi.grid(row=3, column=3, pady=5)

lblAraToplam = Label(f1a, font=('arial',16, 'bold'), text="Ara Toplam", bd=2, anchor='w')
lblAraToplam.grid(row=4, column=2, sticky=W, pady=5)
txtAraToplam = Entry(f1a, font=('arial',16, 'bold'), textvariable=AraToplam, bd=10, insertwidth=4, justify='right')
txtAraToplam.grid(row=4, column=3, pady=5)

lblToplam = Label(f1a, font=('arial',16, 'bold'), text="Toplam Ucret", bd=2, anchor='w')
lblToplam.grid(row=5, column=2, sticky=W, pady=5)
txtToplam = Entry(f1a, font=('arial',16, 'bold'), textvariable=Toplam, bd=10, insertwidth=4, justify='right')
txtToplam.grid(row=5, column=3, pady=5)

btnToplam = Button(f1b, padx=16, pady=8, bd=2, fg='white', font=('arial', 17, 'bold'), width=17, text="Toplam", bg='cadet blue', command=ToplamHesap).grid(row=0, column=0, pady=5, padx=5)

btnReset = Button(f1b, padx=16, pady=8, bd=2, fg='white', font=('arial', 17, 'bold'), width=17, text="Reset", bg='cadet blue', command=Reset).grid(row=0, column=1, pady=5, padx=5)

btnCikis = Button(f1b, padx=16, pady=8, bd=2, fg='white', font=('arial', 17, 'bold'), width=17, text="Cikis", bg='cadet blue', command=iCikis).grid(row=0, column=2, pady=5, padx=5)


root.mainloop()