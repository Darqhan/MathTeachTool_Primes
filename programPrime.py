# -*- coding: ISO-8859-2 -*-
'''
MATH TEACHER'S HELP I: PRIMES 
This program asks two numbers, no more than 6 digits.
- first number input field (Elso vizsgalt szam)
- second number input field (Masodik vizsgalt szam)
You can ask the program to count:
- prime factors (Primtenyezos alak)
- smallest common multiple (LKKT)
- largest common divisor (LNKO)
Other buttons:
- Exit (Kilepes)
- delete fields (Torles)
- Help (Sugo)
'''
from tkinter import *
# this prompt is for the label name aside of the input field
prompt = 'kérek egy számot'
TEXT_MAXINPUTSIZE = 6

def validateTextInputSize(event):
    """
    Method to Validate Entry text input size, see mezo1, mezo2, key
    If more than 6 digits you try to give, it dels the last digit
    """
    global TEXT_MAXINPUTSIZE
    if (event.widget.index(END) >= TEXT_MAXINPUTSIZE - 1):
        event.widget.delete(TEXT_MAXINPUTSIZE - 1)
# MAIN METHODS 
def prim(a,b):
    '''
    returns prime factors distribution
    you  have to add two number, or it not works
    or give one number and 0 for the second
    '''
    number = []
    a = int(mezo1.get())
    b = int(mezo2.get())
    number.append(a)
    number.append(b)
    c = []
    for j in range(2):
        n, prime_list = 1, []
        while number[j]>1: 
            n +=1
            if number[j] % n == 0:
                prime_list.append(n)
                number[j] = number[j] / n
                n =1
        c.append(prime_list)
    return c
def prim_ertek ():
    '''
    gives back the primes to the GUI
    the prime method results are coming here
    from the numbers of input fields writes out to the label fields
    '''
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = prim (a,b)
    cimke6.config(text=c[0], width = 18)
    cimke6.update_idletasks()
    cimke7.config(text=c[1], width = 18)
    cimke7.update_idletasks()
def lnko(a,b):
    "greatest common divisor method"
    while b:
        a, b = b, a%b
    return a
def lkkt(a,b):
    "smallest common multiplicator method"
    return a*b //lnko(a,b)

def lnko_ertek ():
    "write out the result of gcd (lnko) to GUI"
    a = int(mezo1.get())
    b = int(mezo2.get())
    messagebox.showinfo("lnko",lnko(a,b))
def lkkt_ertek():
    "write out the result scm (lkkt) to GUI"
    a = int(mezo1.get())
    b = int(mezo2.get())
    messagebox.showinfo("lkkt",lkkt(a,b))

def sugo():
    '''
    Help button method
    Tis method is a short description of the program into a messagebox
    '''
    messagebox.showinfo("Súgó, mert az is kell","Prímes felbontáshoz maximum hatjegyű számot adhatunk meg \n\n LNKO/LKKT esetén a két megadott számot hasonlítja össze \n\n Törlés: a beviteli mezők törlése \n\n Üdv, Ati42" )


def torles():
    '''
    Delete labels method
    This method initializes the two labels, and two input fields
    '''
    mezo1.delete (0,END)
    mezo2.delete (0,END)
    
    cimke6.config(text = prompt)
    cimke7.config(text = prompt)


# frame starts here
ablak1 = Tk()
ablak1.title("Prímtényezős alak")
# Labels definition
cimke1 = Label (ablak1, text = "Első vizsgált szám:", anchor=W, justify=LEFT, padx=2)
cimke1.grid(row=0, column=0, sticky=E)
cimke2 = Label(ablak1, text = "Második vizsgált szám:", anchor=W, justify=LEFT, padx=2)
cimke2.grid(row=1, column=0, sticky=E)
# fields declaration
mezo1 = Entry(ablak1, bg='light blue', font = "14")
mezo1.bind("<Key>", validateTextInputSize)
mezo1.grid(row=0,column=1)
mezo2 = Entry(ablak1, bg='light blue', font = "14")
mezo2.bind("<Key>", validateTextInputSize)
mezo2.grid(row=1,column=1)


cimke6 = Label(ablak1, text=prompt, anchor=W, justify = LEFT, padx=2)
cimke6.grid(row=0, column=2)
cimke7 = Label(ablak1, text = prompt, anchor=W, justify=LEFT, padx=2)
cimke7.grid(row=1, column=2)


# 6 buttons: one for prime distribution, one for clean all cells, one for exit, two for LCD, SCM, one for help
gomb1 = Button(ablak1, text='Prímtényezős alak', command=prim_ertek, fg= "navy",activebackground='yellow',width=25, height = 3)
gomb1.grid(row=5, column=2, sticky=E)

gomb2 = Button(ablak1, text = "Törlés", command=torles, fg="maroon", activebackground='yellow',width=25, height = 3)
gomb2.grid(row=6, column=0, sticky = W+E+N+S)

gomb3 = Button(ablak1, text='Kilépés', command = ablak1.destroy, fg="red", activebackground='yellow',width=25, height = 3)
gomb3.grid(row=5, column=0)

gomb4 = Button (ablak1, text = 'LNKO', command = lnko_ertek,fg='navy',activebackground='yellow',width=25, height = 3)
gomb4.grid(row=6, column=1)

gomb5 = Button (ablak1, text = 'LKKT', command = lkkt_ertek, fg='navy',activebackground='yellow',width=25, height = 3)
gomb5.grid(row=5, column=1)

gomb6 = Button (ablak1, text = 'Súgó', command = sugo, fg = 'purple', activebackground='yellow',width=25, height = 3)
gomb6.grid(row=6, column=2)

ablak1.mainloop()
