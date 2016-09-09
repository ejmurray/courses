from tkinter import *
import backend import Database

database=Database("books.db")

def get_selected_row(event):
   if list1.size() <= 0:
      return -1
      
   global selected_tuple
   index=list1.curselection()[0]   
   selected_tuple=list1.get(index)
   eTitle.delete(0, END)
   eTitle.insert(END, selected_tuple[1])
   eAuthor.delete(0, END)
   eAuthor.insert(END, selected_tuple[2])
   eYear.delete(0, END)
   eYear.insert(END, selected_tuple[3])
   eisbn.delete(0, END)
   eisbn.insert(END, selected_tuple[4])

def view_command():
   list1.delete(0,END)
   for row in database.view():
      list1.insert(END, row)
      
def search_command():
   list1.delete(0,END)   
   for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
      list1.insert(END,row)

def add_command():
   database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())   
   search_command()
   list1.delete(0, list1.size()-2)
   

def update_command():
   database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
   view_command()
   
def delete_command():
   database.delete(selected_tuple[0])
   view_command()   
   
window=Tk()

window.wm_title("Bookstore")

lTitle= Label(window, text="Title")
lTitle.grid(row=0,column=0)

lAuthor= Label(window, text="Author")
lAuthor.grid(row=0,column=2)

lYear= Label(window, text="Year")
lYear.grid(row=1,column=0)

lisbn= Label(window, text="ISBN")
lisbn.grid(row=1,column=2)

title_text=StringVar()
eTitle = Entry(window, textvariable=title_text)
eTitle.grid(row=0, column=1)

author_text=StringVar()
eAuthor = Entry(window, textvariable=author_text)
eAuthor.grid(row=0, column=3)

year_text=StringVar()
eYear = Entry(window, textvariable=year_text)
eYear.grid(row=1, column=1)

isbn_text=StringVar()
eisbn = Entry(window, textvariable=isbn_text)
eisbn.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)


b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()