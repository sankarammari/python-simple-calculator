from tkinter import *
window=Tk()
window.title('Simple Calculator')
window.iconbitmap('.\output.ico')
window.geometry('326x375')
def ButtonClick(number):
    current = input1.get()
    if number == ".":
        if "." in current.split()[-1]:
            return 
    input1.delete(0, END)
    input1.insert(END, str(current) + str(number))

def ButtonAdd():
    global fnum,m
    m=1
    first_number=input1.get()
    fnum=float(first_number)
    input1.delete(0,END)

def ButtonSub():
    global fnum,m
    m=2
    first_number=input1.get()
    fnum=float(first_number)
    input1.delete(0,END)

def ButtonMul():
    global fnum,m
    m=3
    first_number=input1.get()
    fnum=float(first_number)
    input1.delete(0,END)

def ButtonDiv():
    global fnum,m
    m=4
    first_number=input1.get()
    fnum=float(first_number)
    input1.delete(0,END)

def ButtonPer():
    global fnum,m
    m=5
    first_number=input1.get()
    fnum=float(first_number)
    input1.delete(0,END)

def ButtonEqual():
    second_number = input1.get()
    snum = float(second_number)
    input1.delete(0, END)
    
    if m == 1:
        input1.insert(END, fnum + snum)
    elif m == 2:
        input1.insert(END, fnum - snum)
    elif m == 3:
        input1.insert(END, fnum * snum)
    elif m == 4:
        try:
            input1.insert(END, fnum / snum)
        except ZeroDivisionError:
            input1.insert(END, "Error")
    elif m == 5:
        input1.insert(END, fnum % snum)

def ButtonClear():
    input1.delete(0,END)

def clear_last():
    current = input1.get()
    input1.delete(len(current) - 1, END)

input1=Entry(width=50,borderwidth=8)
input1.grid(row=0,column=0,columnspan=4,ipady=10)
mybuttonAllClear=Button(text='AC',fg='black',bg='orange',padx=30,pady=20,command=ButtonClear).grid(row=1,column=0)
myButtonDiv=Button(text='/',fg='black',bg='aqua',padx=32.5,pady=20,command=ButtonDiv).grid(row=1,column=1)
myButtonclear=Button(text='C',fg='black',bg='orange',padx=31,pady=20,command=clear_last).grid(row=1,column=2)
myButtonDot=Button(text='.',fg='black',bg='aqua',padx=31,pady=20,command=lambda:ButtonClick('.')).grid(row=1,column=3)
myButton7=Button(text='7',fg='white',bg='gray',padx=35,pady=20,command=lambda:ButtonClick(7)).grid(row=2,column=0)
myButton8=Button(text='8',fg='white',bg='gray',padx=33,pady=20,command=lambda:ButtonClick(8)).grid(row=2,column=1)
myButton9=Button(text='9',fg='white',bg='gray',padx=32,pady=20,command=lambda:ButtonClick(9)).grid(row=2,column=2)
myButtonMul=Button(text='*',fg='black',bg='aqua',padx=30,pady=20,command=ButtonMul).grid(row=2,column=3)
myButton4=Button(text='4',fg='white',bg='gray',padx=35,pady=20,command=lambda:ButtonClick(4)).grid(row=3,column=0)
myButton5=Button(text='5',fg='white',bg='gray',padx=33,pady=20,command=lambda:ButtonClick(5)).grid(row=3,column=1)
myButton6=Button(text='6',fg='white',bg='gray',padx=32,pady=20,command=lambda:ButtonClick(6)).grid(row=3,column=2)
myButtonSub=Button(text='-',fg='black',bg='aqua',padx=30,pady=20,command=ButtonSub).grid(row=3,column=3)
myButton1=Button(text='1',fg='white',bg='gray',padx=35,pady=20,command=lambda:ButtonClick(1)).grid(row=4,column=0)
myButton2=Button(text='2',fg='white',bg='gray',padx=33,pady=20,command=lambda:ButtonClick(2)).grid(row=4,column=1)
myButton3=Button(text='3',fg='white',bg='gray',padx=32,pady=20,command=lambda:ButtonClick(3)).grid(row=4,column=2)
myButtonAdd=Button(text='+',fg='black',bg='aqua',padx=28,pady=20,command=ButtonAdd).grid(row=4,column=3)
myButton00=Button(text='00',fg='white',bg='gray',padx=32,pady=20,command=lambda:ButtonClick('00')).grid(row=5,column=0)
myButton0=Button(text='0',fg='white',bg='gray',padx=33,pady=20,command=lambda:ButtonClick(0)).grid(row=5,column=1)
myButtonEqual=Button(text='=',fg='white',bg='green',padx=69,pady=20,command=ButtonEqual).grid(row=5,column=2,columnspan=2)

window.mainloop()
