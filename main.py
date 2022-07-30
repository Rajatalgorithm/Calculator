from tkinter import *
root = Tk()

def printval():
    try:
        v=int(var.get())
        if (v == 1):
            s = int(n1.get()) + int(n2.get())
        elif (v == 2):
            s = int(n1.get()) - int(n2.get())
        elif (v == 3):
            s = int(n1.get()) / int(n2.get())
        elif (v == 4):
            s = int(n1.get()) * int(n2.get())
        else:
            s=0
        label_4 = Label(root, text=f"{s}", width=30, font=("bold", 30))
        label_4.place(x=-200, y=400)
    except ZeroDivisionError:
        label_5 = Label(root, text="wrong input", width=50, font=("bold", 40))
        label_5.place(x=-500, y=400)
    except ValueError:
        label_6 = Label(root, text="algebra nai hai (noob) -_-", width=50, font=("bold", 40))
        label_6.place(x=-500, y=400)

root.geometry("600x800")
root.title("Calculator")
root.resizable(False,False)

n1=StringVar()
label_0=Label(root,text='Num 1:', width=30,font=("bold",30))
label_0.place(x=-200,y=30)
entry_0=Entry(root,textvariable=n1)
entry_0.place(x=250,y=50)

n2=StringVar()
label_1=Label(root,text='Num 2:', width=30,font=("bold",30))
label_1.place(x=-200,y=100)
entry_1=Entry(root,textvariable=n2)
entry_1.place(x=250,y=120)

var=IntVar()
Radiobutton(root,text='+',padx=5,variable=var,value=1,font=(40)).place(x=100,y=200)
Radiobutton(root,text='-',padx=5,variable=var,value=2,font=(40)).place(x=200,y=200)
Radiobutton(root,text='/',padx=5,variable=var,value=3,font=(40)).place(x=300,y=200)
Radiobutton(root,text='*',padx=5,variable=var,value=4,font=(40)).place(x=400,y=200)


Button(root,text="Calculate",font=(60),command=printval).place(x=100,y=300)


root.mainloop()