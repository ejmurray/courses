from tkinter import *

window=Tk()

lTitle= Label(window, text="Title")
lTitle.grid(row=0,column=0)

lAuthor= Label(window, text="Author")
lAuthor.grid(row=0,column=2)

lYear= Label(window, text="Year")
lYear.grid(row=1,column=0)

lISBN= Label(window, text="ISBN")
lISBN.grid(row=1,column=2)

title_text=StringVar()
eTitle = Entry(window, textvariable=title_text)
eTitle.grid(row=0, column=1)

author_text=StringVar()
eAuthor = Entry(window, textvariable=author_text)
eAuthor.grid(row=0, column=3)

year_text=StringVar()
eYear = Entry(window, textvariable=year_text)
eYear.grid(row=1, column=1)

ISBN_text=StringVar()
eISBN = Entry(window, textvariable=ISBN_text)
eISBN.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window, text="View all", width=12)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()

