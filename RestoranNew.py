from tkinter import *
import tkinter.messagebox
import random
from datetime import datetime

root = Tk()
root.geometry("1600x800+0+0")
space = " "
root.title(190*space + "Restaurant Managment")

coverFrame = Frame(root, bd=10, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame, bd=10, pady=2, bg='cadet blue', relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame(root, bd=5, pady=2, width=1920, height=1080, relief=RIDGE)
MainFrame.grid()

Tops = Frame(MainFrame, width=1920, height=1080, bg='cadet blue', bd=10, relief=SUNKEN)
Tops.grid(row=0, column=0)

Tops2 = Frame(MainFrame, width=1920, height=1080, bg='cadet blue', bd=10, relief=SUNKEN)
Tops2.grid(row=1, column=0)

f1 = Frame(Tops2, width=1920, height=1080, bd=10, relief=SUNKEN)
f1.grid(row=0, column=0)

f1a = Frame(f1, width=1920, height=1080, bd=10, relief=SUNKEN)
f1a.grid(row=0, column=0)

f1b = Frame(f1, width=900, height=100, relief=SUNKEN)
f1b.grid(row=1, column=0)

lblTitle = Label(Tops, font=('arial',16, 'bold'), text="Restaunrant Managment", fg='white', bg='cadet blue', bd=10)
lblTitle.grid(row=0, column=0, padx=270)

rand = StringVar()
Food1 = StringVar()
Food2 = StringVar()
Food3 = StringVar()
Food4 = StringVar()
Food5 = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Fee = StringVar()
Drinks = StringVar()
Tax = StringVar()
Account = StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

Food1.set("0")
Food2.set("0")
Food3.set("0")
Food4.set("0")
Food5.set("0")

def Reset():
    Food1.set("0")
    Food2.set("0")
    Food3.set("0")
    Food4.set("0")
    Food5.set("0")
    Subtotal.set("")
    Total.set("")
    Service_Fee.set("")
    Tax.set("")
    Account.set("")

    txtFood1.configure(state=DISABLED)
    txtFood2.configure(state=DISABLED)
    txtFood3.configure(state=DISABLED)
    txtFood4.configure(state=DISABLED)
    txtFood5.configure(state=DISABLED)
    txtDrinks.configure(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)

def iExit():
    iExit = tkinter.messagebox.askyesno("Want to Check Out?")
    if iExit>= 1:
        root.destroy()
        return


def TotalAccount():
    x = random.randint(9023, 490857)
    randomRef = str(x)
    rand.set(randomRef)

    HeFood1 = float(Food1.get())
    HeFood2 = float(Food2.get())
    HeFood3 = float(Food3.get())
    HeFood4 = float(Food4.get())
    HeFood5 = float(Food5.get())
    HeDrinks = float(Drinks.get())

    Food1Account = HeFood1 * 50
    Food2Account = HeFood2 * 30
    Food3Account = HeFood3 * 35
    Food4Account = HeFood4 * 65
    Food5Account = HeFood5 * 45
    DrinksAccount = HeDrinks * 5

    MealAccount = str('₺%.2f' % (Food1Account + Food2Account + Food3Account + Food4Account + Food5Account + DrinksAccount))
    Tax_Fee = ((Food1Account + Food1Account + Food2Account + Food3Account + Food4Account + Food5Account) * 0.1)
    Service_Fee = str('₺%.2f' % ((Food1Account + Food2Account + Food3Account + Food4Account + Food5Account + DrinksAccount) / 99))
    Subtotal = str('₺%.2f' % (Food1Account + Food2Account + Food3Account + Food4Account + Food5Account + DrinksAccount))
    Total_Data = (Food1Account + Food2Account + Food3Account + Food4Account + Food5Account + DrinksAccount)
    Service_Fee.set(Service_Fee)
    Account.set(MealAccount)
    Subtotal.set(Subtotal)
    Tax.set(str('₺%.2f' %(Tax_Fee)))
    TotalAccount = str('₺%.2f' %(Tax_Fee + Total_Data))
    Total.set(TotalAccount)

def AccountFood1():
    if(var1.get() == 1):
        txtFood1.configure(state=NORMAL)
        txtFood1.focus()
        txtFood1.delete('0', END)
        Food1.set("")
    elif(var1.get() == 1):
        txtFood1.configure(state=DISABLED)
        Food1.set("0")

def AccountFood2():
    if(var2.get() == 1):
        txtFood2.configure(state=NORMAL)
        txtFood2.focus()
        txtFood2.delete('0', END)
        Food2.set("")
    elif(var2.get() == 1):
        txtFood2.configure(state=DISABLED)
        Food2.set("0")

def AccountFood3():
    if(var3.get() == 1):
        txtFood3.configure(state=NORMAL)
        txtFood3.focus()
        txtFood3.delete('0', END)
        Food3.set("")
    elif(var3.get() == 1):
        txtFood3.configure(state=DISABLED)
        Food3.set("0")

def AccountFood4():
    if(var4.get() == 1):
        txtFood4.configure(state=NORMAL)
        txtFood4.focus()
        txtFood4.delete('0', END)
        Food4.set("")
    elif(var4.get() == 1):
        txtFood4.configure(state=DISABLED)
        Food4.set("0")

def AccountFood5():
    if(var5.get() == 1):
        txtFood5.configure(state=NORMAL)
        txtFood5.focus()
        txtFood5.delete('0', END)
        Food5.set("")
    elif(var5.get() == 1):
        txtFood5.configure(state=DISABLED)
        Food5.set("0")

def AccountDrinks():
    if(var6.get() == 1):
        txtDrinks.configure(state=NORMAL)
        txtDrinks.focus()
        txtDrinks.delete('0', END)
        Drinks.set("")
    elif(var6.get() == 1):
        txtDrinks.configure(state=DISABLED)
        Drinks.set("0")

lblRef = Label(f1a, font=('arial',16, 'bold'), text="Reference", fg='black', bd=10)
lblRef.grid(row=0, column=0, sticky=W)
txtReference = Entry(f1a, font=('arial',16, 'bold'), textvariable=rand, bd=10, justify='right', bg='cadet blue')
txtReference.grid(row=0, column=1)

chkFood1 = Checkbutton(f1a, text="Food1", variable=var1, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=AccountFood1).grid(row=1, column=0, sticky=W)
txtFood1 = Entry(f1a, font=('arial',16, 'bold'), textvariable=Food1, bd=10, insertwidth=4, justify='right',
                    bg='cadet blue', state=DISABLED)
txtFood1.grid(row=1, column=1)

chkFood2 = Checkbutton(f1a, text="Food2", variable=var2, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=AccountFood2).grid(row=2, column=0, sticky=W)
txtFood2 = Entry(f1a, font=('arial',16, 'bold'), textvariable=Food2, bd=10, insertwidth=4, justify='right',
                 bg='cadet blue', state=DISABLED)
txtFood2.grid(row=2, column=1)

chkFood3 = Checkbutton(f1a, text="Food3", variable=var3, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=AccountFood3).grid(row=3, column=0, sticky=W)
txtFood3 = Entry(f1a, font=('arial',16, 'bold'), textvariable=Food3, bd=10, insertwidth=4, justify='right',
                  bg='cadet blue', state=DISABLED)
txtFood3.grid(row=3, column=1)

chkFood4 = Checkbutton(f1a, text="Food4", variable=var4, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=AccountFood4).grid(row=4, column=0, sticky=W)
txtFood4 = Entry(f1a, font=('arial',16, 'bold'), textvariable=Food4, bd=10, insertwidth=4, justify='right',
                  bg='cadet blue', state=DISABLED)
txtFood4.grid(row=4, column=1)

chkFood5 = Checkbutton(f1a, text="Food5", variable=var5, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=AccountFood5).grid(row=5, column=0, sticky=W)
txtFood5 = Entry(f1a, font=('arial',16, 'bold'), textvariable=Food5, bd=10, insertwidth=4, justify='right',
                   bg='cadet blue', state=DISABLED)
txtFood5.grid(row=5, column=1)

chkDrinks = Checkbutton(f1a, text="Drinks", variable=var6, onvalue=1, offvalue=0, font=('arial',16, 'bold'), command=AccountDrinks).grid(row=0, column=2, sticky=W, pady=5)
txtDrinks = Entry(f1a, font=('arial',16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, justify='right',
                     bg='cadet blue', state=DISABLED)
txtDrinks.grid(row=0, column=3, pady=5)

lblAccount = Label(f1a, font=('arial',16, 'bold'), text="Meal Account", bd=2, anchor='w')
lblAccount.grid(row=1, column=2, sticky=W, pady=5)
txtAccount = Entry(f1a, font=('arial',16, 'bold'), textvariable=Account, bd=10, insertwidth=4, justify='right')
txtAccount.grid(row=1, column=3, pady=5)

lblService = Label(f1a, font=('arial',16, 'bold'), text="Service Fee", bd=2, anchor='w')
lblService.grid(row=2, column=2, sticky=W, pady=5)
txtService = Entry(f1a, font=('arial',16, 'bold'), textvariable=Service_Fee, bd=10, insertwidth=4, justify='right')
txtService.grid(row=2, column=3, pady=5)

lblTax = Label(f1a, font=('arial',16, 'bold'), text="Tax Fee", bd=2, anchor='w')
lblTax.grid(row=3, column=2, sticky=W, pady=5)
txtTax = Entry(f1a, font=('arial',16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, justify='right')
txtTax.grid(row=3, column=3, pady=5)

lblSubtotal = Label(f1a, font=('arial',16, 'bold'), text="Sub total", bd=2, anchor='w')
lblSubtotal.grid(row=4, column=2, sticky=W, pady=5)
txtSubtotal = Entry(f1a, font=('arial',16, 'bold'), textvariable=Subtotal, bd=10, insertwidth=4, justify='right')
txtSubtotal.grid(row=4, column=3, pady=5)

lblTotal = Label(f1a, font=('arial',16, 'bold'), text="Total Fee", bd=2, anchor='w')
lblTotal.grid(row=5, column=2, sticky=W, pady=5)
txtTotal = Entry(f1a, font=('arial',16, 'bold'), textvariable=Total, bd=10, insertwidth=4, justify='right')
txtTotal.grid(row=5, column=3, pady=5)

btnTotal = Button(f1b, padx=16, pady=8, bd=2, fg='white', font=('arial', 17, 'bold'), width=17, text="Total", bg='cadet blue', command=TotalAccount).grid(row=0, column=0, pady=5, padx=5)

btnReset = Button(f1b, padx=16, pady=8, bd=2, fg='white', font=('arial', 17, 'bold'), width=17, text="Reset", bg='cadet blue', command=Reset).grid(row=0, column=1, pady=5, padx=5)

btnExit= Button(f1b, padx=16, pady=8, bd=2, fg='white', font=('arial', 17, 'bold'), width=17, text="Exit", bg='cadet blue', command=iExit).grid(row=0, column=2, pady=5, padx=5)


root.mainloop()
