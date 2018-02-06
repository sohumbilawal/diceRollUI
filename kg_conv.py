from tkinter import *

window = Tk()

def kg_conv():
    grams = float(inpKg.get()) * 1000
    lbs = float(inpKg.get()) * 2.20462
    oz = float(inpKg.get()) * 35.274

    gramT.insert(END, grams)
    lbsT.insert(END, lbs)
    ozT.insert(END, oz)

kg = Label(window, text = "kg:")
kg.grid(row = 0, column = 0)

inpKg = StringVar()
kgEn = Entry(window, textvariable = inpKg)
kgEn.grid(row = 0, column = 1)

kgConv = Button(window, text = "Convert", command = kg_conv)
kgConv.grid(row = 0, column = 2)

gramT = Text(window, height = 1, width = 20)
gramT.grid(row = 1, column = 0)

lbsT = Text(window, height = 1, width = 20)
lbsT.grid(row = 1, column = 1)

ozT = Text(window, height = 1, width = 20)
ozT.grid(row = 1, column = 2)

window.mainloop()
