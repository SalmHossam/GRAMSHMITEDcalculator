from tkinter import *
from statistics import *
from tkinter import messagebox
from math import *
import os

root = Tk()
root.title("Gram Shemdit")
LARGEFONT = ("Arial Bold", 80)
LARGEFONT2 = ("Arial Bold", 40)
root.geometry('4000x1920')
wlcMsg = Label(root, text="WELCOME TO Gram Shemdit ", font=(("Arial Bold", 71)), bg='red4')
wlcMsg.place(x=3, y=0)


def dist():
    root.destroy()


def rest():
    root.destroy()
    os.startfile("stat.py")

    def clear():
        root.destroy()
        os.startfile("stat.py")

    clear_but = Button(root, text="Restart Program", command=clear, bg='gray12', font=("Arial Bold", 15), fg='snow',
                       width=15, height=2)
    clear_but.place(x=522, y=400)
    clear_but = Button(root, text="Exit", command=dist, bg='gray12', font=("Arial Bold", 15), fg='snow', width=15,
                       height=2)
    clear_but.place(x=722, y=400)
    eqcalc_bt.destroy()
    operation_button.destroy()
    wlcMsg.destroy()
    eqcalc_bt1.destroy()
def Operations():
        Label(root, text="Vector 1:", font=LARGEFONT2).place(x=0, y=150)
        sz_box1 = Entry(root, width=30, bg='gray12', fg='snow', font=("Arial Bold", 30))
        sz_box1.place(x=300, y=155)
        Label(root, text="Vector 2:", font=LARGEFONT2).place(x=0, y=200)
        sz_box2 = Entry(root, width=30, bg='gray12', fg='snow', font=("Arial Bold", 30))
        sz_box2.place(x=300, y=210)
        Label(root, text="Vector 3:", font=LARGEFONT2).place(x=0, y=250)
        sz_box3 = Entry(root, width=30, bg='gray12', fg='snow', font=("Arial Bold", 30))
        sz_box3.place(x=300, y=270)




        def Validation():
            try:
                arr1 = list(map(float, sz_box1.get().strip().split()))
                arr2= list(map(float, sz_box2.get().strip().split()))
                arr3= list(map(float, sz_box3.get().strip().split()))
            except ValueError:
                messagebox.askretrycancel("INVALID INPUT", "Please enter a valid value")

            Label(root, text=f'The elements you have entered are : {arr1}', bg='red4',
                  font=("Arial Bold", 20)).place(x=5, y=400)
            arr1.sort(reverse=1)
            Label(root, text=f'The elements you have entered are : {arr2}', bg='red4',
                  font=("Arial Bold", 20)).place(x=5, y=450)
            arr2.sort(reverse=1)
            Label(root, text=f'The elements you have entered are : {arr3}', bg='red4',
                  font=("Arial Bold", 20)).place(x=5, y=500)
            arr3.sort(reverse=1)

            Label(root, text=f'The sum of elements is :  {sum(arr1)}', bg='red4',
                  font=("Arial Bold", 20)).place(x=5, y=550)
            Label(root, text=f'The sum of elements is :  {sum(arr2)}', bg='red4',
                  font=("Arial Bold", 20)).place(x=5, y=600)
            Label(root, text=f'The sum of elements is :  {sum(arr3)}', bg='red4',
                  font=("Arial Bold", 20)).place(x=5, y=650)

        ent_but = Button(root, text="Enter", command=Validation, bg='gray12', fg='snow', font=("Arial Bold", 10),
                         width=15,
                         height=2)
        ent_but.place(x=300, y=350)
        ent_but1 = Button(root, text="Restart Program", command=rest, bg='gray12', fg='snow', font=("Arial Bold", 10),
                          width=15, height=2)
        ent_but1.place(x=530, y=350)
        ent_but1 = Button(root, text="Exit", command=dist, bg='gray12', fg='snow', font=("Arial Bold", 10), width=15,
                          height=2)
        ent_but1.place(x=670, y=350)

        eqcalc_bt1.destroy()
        operation_button.destroy()
        eqcalc_bt.destroy()
        wlcMsg.destroy()


# def Operations():
#     Label(root, text="Vector 1:", font=LARGEFONT2).place(x=0, y=150)
#     sz_box = Entry(root, width=30, bg='gray12', fg='snow', font=("Arial Bold", 30))
#     sz_box.place(x=300, y=155)
#
#     def Validation():
#         try:
#             arr = list(map(float, sz_box.get().strip().split()))
#         except ValueError:
#             messagebox.askretrycancel("INVALID INPUT", "Please enter a valid value")
#
#         Label(root, text=f'The elements you have entered are : {arr}', bg='red4',
#               font=("Arial Bold", 20)).place(x=5, y=300)
#         arr.sort(reverse=1)
#
#         Label(root, text=f'The sum of elements is :  {sum(arr)}', bg='red4',
#               font=("Arial Bold", 20)).place(x=5, y=350)
#
#     ent_but = Button(root, text="Enter", command=Validation, bg='gray12', fg='snow', font=("Arial Bold", 10), width=15,
#                      height=2)
#     ent_but.place(x=300, y=230)
#     ent_but1 = Button(root, text="Restart Program", command=rest, bg='gray12', fg='snow', font=("Arial Bold", 10),
#                       width=15, height=2)
#     ent_but1.place(x=830, y=230)
#     ent_but1 = Button(root, text="Exit", command=dist, bg='gray12', fg='snow', font=("Arial Bold", 10), width=15,
#                       height=2)
#     ent_but1.place(x=670, y=230)
#
#     eqcalc_bt1.destroy()
#     operation_button.destroy()
#     eqcalc_bt.destroy()
#     wlcMsg.destroy()


operation_button = Button(root, text="Start", command=Operations, bg='gray12', font=("Arial Bold", 15), fg='snow',
                          width=15, height=2)
operation_button.place(x=400, y=200)
eqcalc_bt1 = Button(root, text="Exit", command=dist, bg='gray12', font=("Arial Bold", 15), fg='snow', width=15,
                    height=2)
eqcalc_bt1.place(x=600, y=200)
root.mainloop()