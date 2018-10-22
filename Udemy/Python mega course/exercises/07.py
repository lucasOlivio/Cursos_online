from tkinter import *

window = Tk()

def kg_to_gpo():
    value_grams = float(e1_value.get())*1000
    grams.delete("1.0",END)
    grams.insert(INSERT,value_grams)

    value_pounds = float(e1_value.get())*2.20462
    pounds.delete("1.0",END)
    pounds.insert(INSERT,value_pounds)

    value_ounces = float(e1_value.get())*35.274
    ounces.delete("1.0",END)
    ounces.insert(INSERT,value_ounces)

l1 = Label(window, anchor=CENTER, text="Kg")
l1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

b1 = Button(window, text="Convert", command=kg_to_gpo)
b1.grid(row=0, column=2)

grams = Text(window, height=1, width=20)
grams.grid(row=1,column=0)

pounds = Text(window, height=1, width=20)
pounds.grid(row=1,column=1)

ounces = Text(window, height=1, width=20)
ounces.grid(row=1,column=2)

window.mainloop()
