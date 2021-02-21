from tkinter import *


root = Tk()
root.geometry("344x600")
root.title("Calculator by Paritosh...")
root.wm_iconbitmap("workspace1_122059.ico")


def click(event):
    global scvalue
    text =  event.widget.cget(("text"))    
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f1 = Frame(root, bg="grey")

b = Button(f1, text="9",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="8",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="7",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)



f1.pack(fill="both", padx=20)



f1 = Frame(root, bg="grey")

b = Button(f1, text="6",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="5",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="4",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)



f1.pack(fill="both", padx=20)



f1 = Frame(root, bg="grey")

b = Button(f1, text="3",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="2",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="1",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)



f1.pack(fill="both", padx=20)



f1 = Frame(root, bg="grey")

b = Button(f1, text="0",padx=10, pady= 10, font="lucida 21 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="-",padx=10, pady= 10, font="lucida 24 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="*",padx=10, pady= 10, font="lucida 24 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)



f1.pack(fill="both", padx=20)


f1 = Frame(root, bg="grey")

b = Button(f1, text="/",padx=10, pady= 10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="%",padx=10, pady= 10, font="lucida 19 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="=",padx=10, pady= 10, font="lucida 24 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)



f1.pack(fill="both", padx=20)

f1 = Frame(root, bg="grey")

b = Button(f1, text="C",padx=28, pady= 22, font="lucida 20 bold")
b.pack(side=LEFT, padx=5, pady=12)
b.bind("<Button-1>", click)




f1.pack(fill="both", padx=20)








root.mainloop()