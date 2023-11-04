#library_getter
from owlready2 import *
from tkinter import *
from functools import partial
owlready2.JAVA_EXE = "C:\Program Files\Java\jdk-18.0.2.1\\bin\java.exe"

def color_config(widget, color, event):
    widget.configure(foreground=color)

root = Tk()
root.geometry("600x600")
frm = root

title = Frame(frm)
title.pack(padx=20, pady=20)

text = Label(title, text="Welcome to the zoo library app!", font=("Helvetica", 16))
text.pack()

bod = Frame(frm, width=600, highlightbackground="black", highlightthickness=1)
bod.pack(padx=20, pady=20, fill="x")

side = Frame(bod,highlightbackground="black", highlightthickness=1 )
side.grid(column = 0, row = 0, sticky=NW)

books = Frame(side)
books.pack(anchor="nw", padx=5, pady=10)
animals = Frame(side)
animals.pack(anchor="nw", padx=5, pady=10)

right = Frame(bod)
right.grid(column=1, row=0, sticky=NW)


onto = get_ontology("./onto.owl").load()
library = onto.get_namespace("http://test.org/onto.owl")

sync_reasoner()

info = Frame (right, )
info.grid(column=0,row=0, padx=10, pady=5,sticky=NW)


def showBook(book):
    for widget in info.winfo_children():
        widget.destroy()

    Label(info, text=book.name, font=("Helvetica", 11), justify="left").pack( anchor="nw")

    for c in book.is_a:
        try:
            Label(info, text="-" + c.label[0], justify="left").pack( anchor="nw")
        except:
            pass

    for prop in book.get_properties():
        Label(info, text= prop.label[0] + ": ", justify="left").pack( anchor="nw")
        for value in prop[book]:
            Label(info, text="- " +  value.name , justify="left").pack( anchor="nw", padx=10)

    
text1 = Label(books, text="Books we have:", font=("Helvetica", 11))
text1.pack(anchor="nw")

for book in library.Book.instances():
    text = Label(books, text=book.name, font=("Helvetica", 11), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "green"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, book=book:showBook(book))

text2 = Label(animals, text="Animals we have:", font=("Helvetica", 11))
text2.pack(anchor="nw")

for book in library.Animal.instances():
    text = Label(animals, text=book.name, font=("Helvetica", 11), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "green"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, book=book:showBook(book))


root.mainloop()




